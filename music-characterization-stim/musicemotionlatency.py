#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on junho 22, 2022, at 16:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import os
import random

quads=['Q1','Q2','Q3','Q4']
num_musics=4
musics_list=[]

for q in quads:
    filenames=os.listdir('./music/'+q+'/')
    random.shuffle(filenames)
    for m in range(num_musics):
        fn='./music/'+q+'/'+filenames[m]
        musics_list.append(fn)
    
random.shuffle(musics_list)
print(musics_list)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'musicemotionlatency'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\direi\\Documents\\Projects\\BrainMusic\\stimuli\\music_emot_lat\\musicemotionlatency.py',
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
    size=[1200, 800], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "startblock"
startblockClock = core.Clock()
starttext = visual.TextStim(win=win, name='starttext',
    text='Ouve a música. Tenta definir a sua posição em termos de valência e arousal clickando no rato.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "musicrusselquad"
musicrusselquadClock = core.Clock()
russellsQuad = visual.ImageStim(
    win=win,
    name='russellsQuad', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.9, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
music = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='music')
music.setVolume(1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixCross = visual.TextStim(win=win, name='fixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "endblock"
endblockClock = core.Clock()
goodbyetext = visual.TextStim(win=win, name='goodbyetext',
    text='Terminado.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "startblock"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
startblockComponents = [starttext]
for thisComponent in startblockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startblockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = startblockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startblockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *starttext* updates
    if starttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        starttext.frameNStart = frameN  # exact frame index
        starttext.tStart = t  # local t and not account for scr refresh
        starttext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(starttext, 'tStartRefresh')  # time at next scr refresh
        starttext.setAutoDraw(True)
    if starttext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > starttext.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            starttext.tStop = t  # not accounting for scr refresh
            starttext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(starttext, 'tStopRefresh')  # time at next scr refresh
            starttext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startblock"-------
for thisComponent in startblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('starttext.started', starttext.tStartRefresh)
thisExp.addData('starttext.stopped', starttext.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=16.0, method='random', 
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
    
    # ------Prepare to start Routine "musicrusselquad"-------
    continueRoutine = True
    # update component parameters for each repeat
    mouse.clickReset()
    mouse_locs=[]
    target=musics_list.pop(0)  
    music.id=target
    print(target)
    russellsQuad.setImage('Russells-emotion-model.jpg')
    music.setSound(target, secs=30.0, hamming=True)
    music.setVolume(1.0, log=False)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    musicrusselquadComponents = [russellsQuad, music, mouse]
    for thisComponent in musicrusselquadComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    musicrusselquadClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "musicrusselquad"-------
    while continueRoutine:
        # get current time
        t = musicrusselquadClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=musicrusselquadClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if mouse.isPressedIn(russellsQuad):
            mouse_loc = mouse.getPos()
            mouse_locs.append(mouse_loc)
            logging.log(level=logging.DATA, msg=mouse_loc)
            continueRoutine = False
        
        
        # *russellsQuad* updates
        if russellsQuad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            russellsQuad.frameNStart = frameN  # exact frame index
            russellsQuad.tStart = t  # local t and not account for scr refresh
            russellsQuad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(russellsQuad, 'tStartRefresh')  # time at next scr refresh
            russellsQuad.setAutoDraw(True)
        if russellsQuad.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > russellsQuad.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                russellsQuad.tStop = t  # not accounting for scr refresh
                russellsQuad.frameNStop = frameN  # exact frame index
                win.timeOnFlip(russellsQuad, 'tStopRefresh')  # time at next scr refresh
                russellsQuad.setAutoDraw(False)
        # start/stop music
        if music.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            music.frameNStart = frameN  # exact frame index
            music.tStart = t  # local t and not account for scr refresh
            music.tStartRefresh = tThisFlipGlobal  # on global time
            music.play(when=win)  # sync with win flip
        if music.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > music.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                music.tStop = t  # not accounting for scr refresh
                music.frameNStop = frameN  # exact frame index
                win.timeOnFlip(music, 'tStopRefresh')  # time at next scr refresh
                music.stop()
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in musicrusselquadComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "musicrusselquad"-------
    for thisComponent in musicrusselquadComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('russellsQuad.started', russellsQuad.tStartRefresh)
    trials.addData('russellsQuad.stopped', russellsQuad.tStopRefresh)
    music.stop()  # ensure sound has stopped at end of routine
    trials.addData('music.started', music.tStartRefresh)
    trials.addData('music.stopped', music.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    # the Routine "musicrusselquad" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [fixCross]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixCross* updates
        if fixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixCross.frameNStart = frameN  # exact frame index
            fixCross.tStart = t  # local t and not account for scr refresh
            fixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCross, 'tStartRefresh')  # time at next scr refresh
            fixCross.setAutoDraw(True)
        if fixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixCross.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fixCross.tStop = t  # not accounting for scr refresh
                fixCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixCross, 'tStopRefresh')  # time at next scr refresh
                fixCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixCross.started', fixCross.tStartRefresh)
    trials.addData('fixCross.stopped', fixCross.tStopRefresh)
    thisExp.nextEntry()
    
# completed 16.0 repeats of 'trials'


# ------Prepare to start Routine "endblock"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endblockComponents = [goodbyetext]
for thisComponent in endblockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endblockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "endblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endblockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endblockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbyetext* updates
    if goodbyetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbyetext.frameNStart = frameN  # exact frame index
        goodbyetext.tStart = t  # local t and not account for scr refresh
        goodbyetext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbyetext, 'tStartRefresh')  # time at next scr refresh
        goodbyetext.setAutoDraw(True)
    if goodbyetext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > goodbyetext.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            goodbyetext.tStop = t  # not accounting for scr refresh
            goodbyetext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(goodbyetext, 'tStopRefresh')  # time at next scr refresh
            goodbyetext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endblock"-------
for thisComponent in endblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goodbyetext.started', goodbyetext.tStartRefresh)
thisExp.addData('goodbyetext.stopped', goodbyetext.tStopRefresh)

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
