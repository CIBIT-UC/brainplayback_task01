import os
import numpy as np

from bids.layout import BIDSLayout
import nibabel as nib

# Data management functions
def get_bids_layout(bids_dir, bids_derivatives_dir):
    """
    Get a BIDSLayout object.
    Parameters:
    - bids_dir: Path to BIDS directory.
    Returns:
    - layout: BIDSLayout object.
    """

    layout = BIDSLayout(bids_dir, derivatives=str(bids_derivatives_dir))

    return layout


def get_pp_file(layout, substr, runstr):
    """
    Get the confounds file from the fMRI preprocessing pipeline.
    Parameters:
    - layout: BIDSLayout object.
    - substr: Subject ID.
    - runstr: Run number.
    Returns:
    - pp_file: Preprocessed file.
    """

    # Select Preprocessed from fMRI preprocessing pipeline.
    pp_files = layout.get(subject=substr,
                          datatype='func',
                          run=runstr,
                          extension='nii.gz')

    pp_fn=list(map(lambda a: 'desc-preproc_bold' in a.filename, pp_files))

    idx=[i for i, x in enumerate(pp_fn) if x]

    pp_file=pp_files[idx[0]]

    print(f'Preprocessed functional data for {substr}, run {runstr}: {pp_file}')
    
    return pp_file


def get_events_file(layout, substr, runstr):
    """
    Get the events file.
    Parameters:
    - layout: BIDSLayout object.
    - substr: Subject ID.
    - runstr: Run number.
    Returns:
    - events_file: Events file.
    """

    # Select events file.
    events_files = layout.get(subject=substr,
                              datatype='func',
                              run=runstr,
                              suffix='events',
                              extension='tsv')

    events_file = events_files[0]

    print(f'Events file for {substr}, run {runstr}: {events_file}')

    return events_file


def get_mask_file(layout, substr):
    """
    Get the gray matter mask file.
    Parameters:
    - layout: BIDSLayout object.
    - substr: Subject ID.
    Returns:
    - gmmask_file: Gray matter mask file.
    """

    # Select gray matter mask file.
    gmmask_files = layout.get(subject=substr,
                           scope='derivatives',
                            datatype='anat', 
                            extension='nii.gz')

    gm_mask_fns=list(map(lambda a: 'space-MNI152NLin2009cAsym_label-GM_probseg' in a.filename, gmmask_files))
    
    idx=[i for i, x in enumerate(gm_mask_fns) if x]

    gm_mask = gmmask_files[idx[0]]

    print(f'Gray matter mask file for {substr}: {gm_mask}')

    return gm_mask



