#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on janeiro 03, 2023, at 12:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'brainplayback_quadrants'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '1', 'trigger': False}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_run-%s' % (expInfo['participant'], expName, expInfo['date'], expInfo['session'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\direi\\Documents\\GitHub\\brainplayback_project\\fMRI_stim\\brainplayback_quadrants_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1512, 982], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='retina', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# Initialize components for Routine "RandomSelection"
RandomSelectionClock = core.Clock()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
WelcomeMessage = visual.TextStim(win=win, name='WelcomeMessage',
    text='Hello!\nWaiting for trigger...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "WaitForTrigger"
WaitForTriggerClock = core.Clock()

# Initialize components for Routine "Baseline_Noise"
Baseline_NoiseClock = core.Clock()
Baseline1 = visual.TextStim(win=win, name='Baseline1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Noise = sound.Sound('music/noise.wav', secs=-1, stereo=True, hamming=True,
    name='Noise')
Noise.setVolume(1.0)
Baseline2 = visual.TextStim(win=win, name='Baseline2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "MusicExcerptPresentation"
MusicExcerptPresentationClock = core.Clock()
MusicExcerpt = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='MusicExcerpt')
MusicExcerpt.setVolume(1.0)
ISI = visual.TextStim(win=win, name='ISI',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "IncreaseMusicIdx"
IncreaseMusicIdxClock = core.Clock()

# Initialize components for Routine "BaselineFinal"
BaselineFinalClock = core.Clock()
Baseline3 = visual.TextStim(win=win, name='Baseline3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text='Goodbye!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "RandomSelection"-------
continueRoutine = True
# update component parameters for each repeat
import random
import numpy as np

nExcerpts = 225 # total number of excerpts per quadrant
nMusics = 3 # number of musics that will be played during one trial per quadrant

random.seed(expInfo['participant'])

partName=expInfo['participant']

A = np.random.RandomState(seed=round(random.random()*10)).permutation(np.arange(0,nExcerpts-nMusics*2))

numMusicsPerSes = 6
firstIdx = (int(expInfo['session'])-1) * numMusicsPerSes 
musicIdxs = A[firstIdx:firstIdx+numMusicsPerSes]

currentIdx = 0


print("musicIdxs = " + str(musicIdxs))
# keep track of which components have finished
RandomSelectionComponents = []
for thisComponent in RandomSelectionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RandomSelectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RandomSelection"-------
while continueRoutine:
    # get current time
    t = RandomSelectionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RandomSelectionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RandomSelectionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RandomSelection"-------
for thisComponent in RandomSelectionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "RandomSelection" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
WelcomeScreenComponents = [WelcomeMessage]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeMessage* updates
    if WelcomeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeMessage.frameNStart = frameN  # exact frame index
        WelcomeMessage.tStart = t  # local t and not account for scr refresh
        WelcomeMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeMessage, 'tStartRefresh')  # time at next scr refresh
        WelcomeMessage.setAutoDraw(True)
    if WelcomeMessage.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > WelcomeMessage.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            WelcomeMessage.tStop = t  # not accounting for scr refresh
            WelcomeMessage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(WelcomeMessage, 'tStopRefresh')  # time at next scr refresh
            WelcomeMessage.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeMessage.started', WelcomeMessage.tStartRefresh)
thisExp.addData('WelcomeMessage.stopped', WelcomeMessage.tStopRefresh)

# ------Prepare to start Routine "WaitForTrigger"-------
continueRoutine = True
# update component parameters for each repeat
if expInfo['trigger']:
    
    print('Checking trigger to start experiment.')
    from psychopy import core, parallel
    import serial
    
    #initialise ports
    serialPort = serial.Serial("COM5", baudrate=57600, bytesize=8, parity='N', stopbits=1, timeout=0.0001)

    serialPort.flushInput();
    serialPort.flushOutput()


    #time out period
    timer = core.CountdownTimer(30)

    print('Checking trigger to start experiment.')

    while timer.getTime() > 0:
      nCharsToGet = serialPort.inWaiting()
      if (nCharsToGet)>0:
          # number of incoming bytes.
          message = serialPort.read(nCharsToGet)
          #read the current characters
          print(message)
          break
          
    if (nCharsToGet)==0:
      print("*** TRIGGER NOT FOUND ***")
      core.quit()
# keep track of which components have finished
WaitForTriggerComponents = []
for thisComponent in WaitForTriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitForTriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WaitForTrigger"-------
while continueRoutine:
    # get current time
    t = WaitForTriggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitForTriggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitForTriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitForTrigger"-------
for thisComponent in WaitForTriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "WaitForTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('MusicListSelect.csv'),
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Baseline_Noise"-------
        continueRoutine = True
        routineTimer.add(36.000000)
        # update component parameters for each repeat
        Noise.setSound('music/noise.wav', secs=12, hamming=True)
        Noise.setVolume(1.0, log=False)
        # keep track of which components have finished
        Baseline_NoiseComponents = [Baseline1, Noise, Baseline2]
        for thisComponent in Baseline_NoiseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Baseline_NoiseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Baseline_Noise"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Baseline_NoiseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Baseline_NoiseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Baseline1* updates
            if Baseline1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Baseline1.frameNStart = frameN  # exact frame index
                Baseline1.tStart = t  # local t and not account for scr refresh
                Baseline1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Baseline1, 'tStartRefresh')  # time at next scr refresh
                Baseline1.setAutoDraw(True)
            if Baseline1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Baseline1.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    Baseline1.tStop = t  # not accounting for scr refresh
                    Baseline1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Baseline1, 'tStopRefresh')  # time at next scr refresh
                    Baseline1.setAutoDraw(False)
            # start/stop Noise
            if Noise.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
                # keep track of start time/frame for later
                Noise.frameNStart = frameN  # exact frame index
                Noise.tStart = t  # local t and not account for scr refresh
                Noise.tStartRefresh = tThisFlipGlobal  # on global time
                Noise.play(when=win)  # sync with win flip
            if Noise.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Noise.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    Noise.tStop = t  # not accounting for scr refresh
                    Noise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Noise, 'tStopRefresh')  # time at next scr refresh
                    Noise.stop()
            
            # *Baseline2* updates
            if Baseline2.status == NOT_STARTED and tThisFlip >= 24-frameTolerance:
                # keep track of start time/frame for later
                Baseline2.frameNStart = frameN  # exact frame index
                Baseline2.tStart = t  # local t and not account for scr refresh
                Baseline2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Baseline2, 'tStartRefresh')  # time at next scr refresh
                Baseline2.setAutoDraw(True)
            if Baseline2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Baseline2.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    Baseline2.tStop = t  # not accounting for scr refresh
                    Baseline2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Baseline2, 'tStopRefresh')  # time at next scr refresh
                    Baseline2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Baseline_NoiseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Baseline_Noise"-------
        for thisComponent in Baseline_NoiseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blocks.addData('Baseline1.started', Baseline1.tStartRefresh)
        blocks.addData('Baseline1.stopped', Baseline1.tStopRefresh)
        Noise.stop()  # ensure sound has stopped at end of routine
        blocks.addData('Noise.started', Noise.tStartRefresh)
        blocks.addData('Noise.stopped', Noise.tStopRefresh)
        blocks.addData('Baseline2.started', Baseline2.tStartRefresh)
        blocks.addData('Baseline2.stopped', Baseline2.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        trialsMusics = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(MusicsSelect, selection=musicIdxs[currentIdx:currentIdx+nMusics]),
            seed=None, name='trialsMusics')
        thisExp.addLoop(trialsMusics)  # add the loop to the experiment
        thisTrialsMusic = trialsMusics.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsMusic.rgb)
        if thisTrialsMusic != None:
            for paramName in thisTrialsMusic:
                exec('{} = thisTrialsMusic[paramName]'.format(paramName))
        
        for thisTrialsMusic in trialsMusics:
            currentLoop = trialsMusics
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsMusic.rgb)
            if thisTrialsMusic != None:
                for paramName in thisTrialsMusic:
                    exec('{} = thisTrialsMusic[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "MusicExcerptPresentation"-------
            continueRoutine = True
            routineTimer.add(12.000000)
            # update component parameters for each repeat
            MusicExcerpt.setSound(musics, secs=11.5, hamming=True)
            MusicExcerpt.setVolume(1.0, log=False)
            # keep track of which components have finished
            MusicExcerptPresentationComponents = [MusicExcerpt, ISI]
            for thisComponent in MusicExcerptPresentationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            MusicExcerptPresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "MusicExcerptPresentation"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = MusicExcerptPresentationClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=MusicExcerptPresentationClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop MusicExcerpt
                if MusicExcerpt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    MusicExcerpt.frameNStart = frameN  # exact frame index
                    MusicExcerpt.tStart = t  # local t and not account for scr refresh
                    MusicExcerpt.tStartRefresh = tThisFlipGlobal  # on global time
                    MusicExcerpt.play(when=win)  # sync with win flip
                if MusicExcerpt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > MusicExcerpt.tStartRefresh + 11.5-frameTolerance:
                        # keep track of stop time/frame for later
                        MusicExcerpt.tStop = t  # not accounting for scr refresh
                        MusicExcerpt.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(MusicExcerpt, 'tStopRefresh')  # time at next scr refresh
                        MusicExcerpt.stop()
                
                # *ISI* updates
                if ISI.status == NOT_STARTED and tThisFlip >= 11.5-frameTolerance:
                    # keep track of start time/frame for later
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.tStart = t  # local t and not account for scr refresh
                    ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                    ISI.setAutoDraw(True)
                if ISI.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI.tStop = t  # not accounting for scr refresh
                        ISI.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ISI, 'tStopRefresh')  # time at next scr refresh
                        ISI.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MusicExcerptPresentationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "MusicExcerptPresentation"-------
            for thisComponent in MusicExcerptPresentationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            MusicExcerpt.stop()  # ensure sound has stopped at end of routine
            trialsMusics.addData('MusicExcerpt.started', MusicExcerpt.tStartRefresh)
            trialsMusics.addData('MusicExcerpt.stopped', MusicExcerpt.tStopRefresh)
            trialsMusics.addData('ISI.started', ISI.tStartRefresh)
            trialsMusics.addData('ISI.stopped', ISI.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trialsMusics'
        
        # get names of stimulus parameters
        if trialsMusics.trialList in ([], [None], None):
            params = []
        else:
            params = trialsMusics.trialList[0].keys()
        # save data for this loop
        trialsMusics.saveAsExcel(filename + '.xlsx', sheetName='trialsMusics',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        trialsMusics.saveAsText(filename + 'trialsMusics.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'blocks'
    
    # get names of stimulus parameters
    if blocks.trialList in ([], [None], None):
        params = []
    else:
        params = blocks.trialList[0].keys()
    # save data for this loop
    blocks.saveAsExcel(filename + '.xlsx', sheetName='blocks',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    blocks.saveAsText(filename + 'blocks.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "IncreaseMusicIdx"-------
    continueRoutine = True
    # update component parameters for each repeat
    currentIdx=currentIdx+nMusics
    
    print('currentIdx = ' + str(currentIdx) )
    # keep track of which components have finished
    IncreaseMusicIdxComponents = []
    for thisComponent in IncreaseMusicIdxComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    IncreaseMusicIdxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "IncreaseMusicIdx"-------
    while continueRoutine:
        # get current time
        t = IncreaseMusicIdxClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=IncreaseMusicIdxClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IncreaseMusicIdxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "IncreaseMusicIdx"-------
    for thisComponent in IncreaseMusicIdxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "IncreaseMusicIdx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "BaselineFinal"-------
continueRoutine = True
routineTimer.add(25.000000)
# update component parameters for each repeat
# keep track of which components have finished
BaselineFinalComponents = [Baseline3, text]
for thisComponent in BaselineFinalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BaselineFinalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BaselineFinal"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BaselineFinalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BaselineFinalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Baseline3* updates
    if Baseline3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Baseline3.frameNStart = frameN  # exact frame index
        Baseline3.tStart = t  # local t and not account for scr refresh
        Baseline3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Baseline3, 'tStartRefresh')  # time at next scr refresh
        Baseline3.setAutoDraw(True)
    if Baseline3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Baseline3.tStartRefresh + 24-frameTolerance:
            # keep track of stop time/frame for later
            Baseline3.tStop = t  # not accounting for scr refresh
            Baseline3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Baseline3, 'tStopRefresh')  # time at next scr refresh
            Baseline3.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 24-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BaselineFinalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BaselineFinal"-------
for thisComponent in BaselineFinalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Baseline3.started', Baseline3.tStartRefresh)
thisExp.addData('Baseline3.stopped', Baseline3.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
if expInfo['trigger']:
    serialPort.close()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
