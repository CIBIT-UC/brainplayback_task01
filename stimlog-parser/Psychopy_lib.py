import pandas as pd
import numpy as np

import os
import glob

def Psychopy_log_to_BIDS_events_complete(log_fn):
    """
    This function converts a Psychopy log file to a BIDS events file.

    Parameters:
    log_fn (str): The filename of the Psychopy log file.

    The function performs the following steps:
    1. Extracts the participant ID and run ID from the filename.
    2. Reads the log file into a pandas DataFrame.
    3. Selects a subset of columns related to music selection, noise, and baselines.
    4. Drops rows with NaN values from the last baseline subset.
    5. Lists all files in the 'music-char-data' directory.
    6. Create a pandas DataFrame with columns required by the BIDS standard.
    7. Reads the music characterization data file for the participant and run.


    Note: The function prints out the filename, participant ID, and run ID for verification.

    Returns:
    None. The function operates in-place and does not return a value.
    """
    
    #create a new lists by parsing the string using "," delimiter
    head_tail = os.path.split(log_fn)
    print(head_tail[1])

    sub_id=head_tail[1].split("_")
    print("Participant: ",sub_id[0])

    run_id=sub_id[-1].split(".")
    print("Run id: ",run_id[0])
    
    
    # run data
    sub_id=sub_id[0]
    run_id=run_id[0]

    # default values
    sess_id='01'
    task_id='01c'
    
    
    print(f' file: {log_fn}')
    # Create pandas dataframe to read data into data structure.
    df_log=pd.read_csv(log_fn)

    # Select subset of columns
    df_log_M=df_log.loc[:,["MusicsSelect", "musics","Baseline1.started", "Noise.started","Baseline2.started", "MusicExcerpt.started", "MusicExcerpt.stopped"]]
    
    
    # Select subset of columns
    df_last_bl=df_log.loc[:,["Baseline3.started", "Baseline3.stopped"]]

    # Remove rows with NaN - nor necessary for this event files.
    df_last_bl=df_last_bl.dropna(how="any")

    full_list = os.listdir(os.path.join('..','data','music-char-data'))


    # list to store files
    csv_file = []

    # participant idx
    p = sub_id.split('-')[1]

    # run idx
    r = run_id.split('-')[1]
    r = str(r).zfill(2)

    print("Participant (idx), run (idx): ",p, r)



    # identify csv file for each run
    tok_filename = f'{p}_{r}'

    # Iterate directory
    for file in full_list:
        # check only text files
        if file.startswith(tok_filename) and file.endswith('.csv'):
            csv_file.append(file)
            
    # Create pandas dataframe with columns required by the BIDS standard.
    bids={'onset':[],'duration':[],'trial_type':[]}
    df_bids=pd.DataFrame(bids)

    
    if csv_file:
        
        df_Q = pd.read_csv(os.path.join('..','data',
                            'music-char-data',
                            csv_file[0]))

        # Last row NaN.
        df_Q = df_Q[:24]

        # Select rows of interest.
        df_Q=df_Q[['music.id','mouse.x','mouse.y']]

        # Extract position from mouse columns.
        df_Q['mouse.x'] = df_Q['mouse.x'].str[1:-1].astype(float)
        df_Q['mouse.y'] = df_Q['mouse.y'].str[1:-1].astype(float)

        # extract Q from music filename.
        df_Q['music.id_project'] = df_Q.apply(lambda row: getQ(row), axis=1)

        # Get Q from mouse click position.
        df_Q['Quadrants.participant'] = df_Q.apply(lambda row: categorise(row), axis=1)

        # select each music and look for new id
        df_log_M['musics']

        QperPart=[]

        for index, row in df_log_M.iterrows():
            #print(index, row['musics'])
            if row['musics'] == row['musics']:
                toks=row['musics'].split("\\")
                musictok=toks[2]
                # print(musictok, toks[1], index)

                #find music in classification dataframe
                musics_dfQ = df_Q.loc[df_Q['music.id'].str.contains(musictok, case=False)]

                (musics_dfQ['Quadrants.participant'].values[0])
                QperPart.append(musics_dfQ['Quadrants.participant'].values[0])
            else:
                QperPart.append(np.NaN)


        # print(QperPart)
        df_log_M['musicsQperPart'] = QperPart

        

        #number of decimals when rounding numbers
        decimals=2

        # offset of the experiment in seconds (seconds until first baseline.)
        exp_offset=df_log_M.iloc[0]["Baseline1.started"]

        # considering the log file, add rows for each event.

        # For each row:
        for i in range(len(df_log_M)-1):
            if not np.isnan(df_log_M.iloc[i]["Baseline1.started"]):
                # Add Baseline trial.
                df_bids.loc[len(df_bids.index)] = [np.round(df_log_M.iloc[i]["Baseline1.started"]-exp_offset, decimals),
                                                   np.round(df_log_M.iloc[i]["Noise.started"]-df_log_M.iloc[i]["Baseline1.started"],
                                                            decimals),
                                                  'Baseline'] 
                # Add Noise trial.
                df_bids.loc[len(df_bids.index)] = [np.round(df_log_M.iloc[i]["Noise.started"]-exp_offset, decimals),
                                                   np.round(df_log_M.iloc[i]["Baseline2.started"]-df_log_M.iloc[i]["Noise.started"],
                                                            decimals),
                                                  'Noise'] 
                # Add Baseline2 trial.
                df_bids.loc[len(df_bids.index)] = [np.round(df_log_M.iloc[i]["Baseline2.started"]-exp_offset, decimals),
                                                   np.round(df_log_M.iloc[i]["MusicExcerpt.started"]-df_log_M.iloc[i]["Baseline2.started"],
                                                            decimals),
                                                  'Baseline'] 

                # Add Music trial.
                df_bids.loc[len(df_bids.index)] = [np.round(df_log_M.iloc[i]["MusicExcerpt.started"]-exp_offset, decimals),
                                                   np.round(df_log_M.iloc[i]["MusicExcerpt.stopped"]-df_log_M.iloc[i]["MusicExcerpt.started"], decimals),
                                                   df_log_M.iloc[i]["musicsQperPart"]+ '_p'] 

                # Add Music trial.
                df_bids.loc[len(df_bids.index)] = [np.round(df_log_M.iloc[i]["MusicExcerpt.started"]-exp_offset, decimals),
                                                   np.round(df_log_M.iloc[i]["MusicExcerpt.stopped"]-df_log_M.iloc[i]["MusicExcerpt.started"], decimals),
                                                   df_log_M.iloc[i]["MusicsSelect"][-6:-4] + '_db'] 


            elif not np.isnan(df_log_M.iloc[i]["MusicExcerpt.started"]):

                # Add Music trial.
                df_bids.loc[len(df_bids.index)] = [np.round(df_log_M.iloc[i]["MusicExcerpt.started"]-exp_offset, decimals),
                                                   np.round(df_log_M.iloc[i]["MusicExcerpt.stopped"]-df_log_M.iloc[i]["MusicExcerpt.started"], decimals),
                                                   df_log_M.iloc[i]["musicsQperPart"]+ '_p'] 

                # Add Music trial.
                df_bids.loc[len(df_bids.index)] = [np.round(df_log_M.iloc[i]["MusicExcerpt.started"]-exp_offset, decimals),np.round(df_log_M.iloc[i]["MusicExcerpt.stopped"]-df_log_M.iloc[i]["MusicExcerpt.started"], decimals),df_log_M.iloc[i]["MusicsSelect"][-6:-4] + '_db'] 

    return df_bids

def getQ(row):  
    """
    This function extracts the quadrant from the music filename.
    """

    t = row['music.id'].split('/')
    return (f'{t[3]}')

def categorise(row):  
    """
    This function categorises the quadrant based on the mouse click position.
    """

    if row['mouse.x'] > 0 and row['mouse.y'] > 0:
        return 'Q1'
    elif row['mouse.x'] < 0 and row['mouse.y'] > 0:
        return 'Q2'
    elif row['mouse.x'] < 0  and row['mouse.y'] < 0:
        return 'Q3'
    return 'Q4'


