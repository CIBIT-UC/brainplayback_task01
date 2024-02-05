import numpy as np
import pandas as pd
from nilearn import masking
from nilearn.image import mean_img
from nilearn.glm.first_level import FirstLevelModel
from nilearn.image import concat_imgs

from bids.layout import BIDSLayout
import nibabel as nib


import nilearn
from nilearn.glm.first_level import make_first_level_design_matrix
from nilearn.glm.first_level import FirstLevelModel

import nilearn.image as nli

from nilearn import plotting
from nilearn.plotting import plot_design_matrix

import os

from src import dm, lsa, img


def create_contrasts(updated_events_df, lsa_glm):
    """
    Compute contrasts for the LSA model.

    Parameters:
    - updated_events_df: DataFrame with updated LSA events.
    - lsa_glm: First-level GLM object.

    Returns:
    - img_lsa: 4D image of beta maps for each contrast.
    """

    # Create contrast matrix
    contrast_matrix_lsa = np.eye(len(updated_events_df), len(updated_events_df) + 7)

    # Compute beta maps for each contrast
    beta_maps_lsa = [lsa_glm.compute_contrast(contrast) for contrast in contrast_matrix_lsa]

    # Concatenate beta maps into a 4D image
    img_lsa = concat_imgs(beta_maps_lsa)

    return img_lsa


def update_designmatrix(df):
    """
    Label trials for an LSA model.

    Parameters:
    - df: DataFrame containing trial information.

    Returns:
    - df: Updated DataFrame with labeled trial types.
    """

    unique_conditions = df["trial_type"].unique()

    df["class"] = df["trial_type"]
    condition_counter = {condition: 0 for condition in unique_conditions}

    for i, trial in df.iterrows():
        trial_condition = trial["class"]
        condition_counter[trial_condition] += 1
        labeled_trial_name = f"{trial_condition}_{condition_counter[trial_condition]:03d}"
        df.loc[i, "trial_type"] = labeled_trial_name

    return df



def create_lsa_featset(subject, 
                       run, 
                       task = '01', 
                       sub_block = 12, 
                       condition_suffix = 'p',
                       clean_image = True,
                       bids_dir='/Volumes/T7/datasets/BIDS-BRAINPLAYBACK-TASK1',
                       derivatives_dir='/Volumes/T7/datasets/BIDS-BRAINPLAYBACK-TASK1/derivatives/fmriprep',
                       output_dir='../data/BIDS_ds/derivatives/nilearn'):
    """
    Create a first-level featset using the LSA method.

    Parameters:
    - subject: Subject ID.
    - run: Run number.
    - task: Task name.
    - sub_block: Number of blocks per trial.
    - condition_suffix: Suffix to select events.
    - clean_image: If True, clean and smooth data.
    - bids_dir: Path to BIDS dataset.
    - derivatives_dir: Path to derivatives directory.
    - output_dir: Path to output directory.
    """

    # Get BIDS layout
    layout = dm.get_bids_layout(bids_dir, derivatives_dir)

    # Repetition time
    TR=layout.get_tr()

    # Condition and event-related parameters
    mask_threshold = '0.3'
    hrf_model_type = 'spm'

    # Output directories
    func_output_dir = os.path.join(output_dir, f'sub-{subject}/ses-01/func')
    anat_output_dir = os.path.join(output_dir, f'sub-{subject}/ses-01/anat')

    # Create necessary directories if they don't exist
    for directory in [func_output_dir, anat_output_dir]:
        os.makedirs(directory, exist_ok=True)

    # Load preprocessed functional MRI data
    fmri_image = nib.load(dm.get_pp_file(layout, subject, run))

    # Clean and smooth data if specified
    if clean_image:
        print(f'Cleaning and smoothing data for sub-{subject} run-{run}')
        fmri_image = nli.clean_img(fmri_image, standardize=True, detrend=True)

    print(f'Max: {np.max(fmri_image.get_fdata())} | Min: {np.min(fmri_image.get_fdata())}')

    # Load events data into a DataFrame
    events_df = pd.read_csv(dm.get_events_file(layout, subject, run), sep='\t')

    # Resample gray matter mask based on specified threshold
    gm_mask = img.create_mask_from_segm(dm.get_gm_mask_file(layout, subject), fmri_image, mask_threshold)
    gm_mask.to_filename(os.path.join(anat_output_dir, f'sub-{subject}_mask-gm.nii.gz'))

    # Select events based on condition suffix
    events_p = events_df[events_df.trial_type.str.endswith(tuple(condition_suffix))]

    # Update design matrix using LSA method
    lsa_events = lsa.update_designmatrix(events_p.copy())

    # Save target file for LSA events
    print(f'Creating target file for sub-{subject} run-{run}')
    target_filename = f'sub-{subject}_run-{run}_events-{condition_suffix}_duration-{sub_block}_LSA_beta_maps.csv'
    lsa_events['class'].to_csv(os.path.join(func_output_dir, target_filename), index=False)

    # Get unique trialwise conditions
    trialwise_conditions = lsa_events["trial_type"].unique()

    # Create design matrix
    lsa_design_matrix = make_first_level_design_matrix(np.arange(fmri_image.shape[3]) * TR,
                                                       lsa_events,
                                                       drift_model='polynomial',
                                                       drift_order=3,
                                                       hrf_model=hrf_model_type)

    print('Fitting a GLM')
    
    # Fit GLM model
    glm_lsa = FirstLevelModel(mask_img=gm_mask, t_r=TR)
    glm_lsa.fit(fmri_image, design_matrices=lsa_design_matrix)

    # Compute and save z-scored beta maps for each condition
    z_maps_lsa = [glm_lsa.compute_contrast(condition, output_type="z_score") for condition in trialwise_conditions]

    # Concatenate z-scored beta maps into a 4D image and save
    img_lsa = nilearn.image.concat_imgs(z_maps_lsa)
    img_filename = f'sub-{subject}_run-{run}_events-{condition_suffix}_duration-{sub_block}_LSA_beta_maps.nii.gz'
    img_lsa.to_filename(os.path.join(func_output_dir, img_filename))






