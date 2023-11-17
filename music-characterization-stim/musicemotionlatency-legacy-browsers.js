/**************************** 
 * Musicemotionlatency Test *
 ****************************/


// store info about the experiment session:
let expName = 'musicemotionlatency';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'


// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(startblockRoutineBegin());
flowScheduler.add(startblockRoutineEachFrame());
flowScheduler.add(startblockRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(endblockRoutineBegin());
flowScheduler.add(endblockRoutineEachFrame());
flowScheduler.add(endblockRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Russells-emotion-model.jpg', 'path': 'Russells-emotion-model.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.3';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var startblockClock;
var starttext;
var quads;
var num_musics;
var musics_list;
var musicrusselquadClock;
var russellsQuad;
var music;
var mouse;
var musictext;
var ISIClock;
var fixCross;
var endblockClock;
var goodbyetext;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "startblock"
  startblockClock = new util.Clock();
  starttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'starttext',
    text: 'Ouve a música. Tenta definir a sua posição em termos de valência e arousal clickando no rato.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  /* Randomize array in-place using Durstenfeld shuffle algorithm */
  function shuffleArray(array) {
      for (var i = array.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var temp = array[i];
          array[i] = array[j];
          array[j] = temp;
      }
  }
  
  var filenames, fn, fs, musics_list, num_musics, quads;
  quads = ["Q1", "Q2", "Q3", "Q4"];
  num_musics = 2;
  musics_list = [];
  
  console.log("hello")
  
  for (var q, _pj_c = 0, _pj_a = quads, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      q = _pj_a[_pj_c];
      fs = require('fs');
      filenames = fs.readdirSync((("./music/" + q) + "/"));
      console.log(filenames)
      
      shuffleArray(filenames);
      for (var m, _pj_f = 0, _pj_d = util.range(num_musics), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
          m = _pj_d[_pj_f];
          fn = ((("./music/" + q) + "/") + filenames[m]);
          musics_list.push(fn);
      }
  }
  shuffleArray(musics_list);
  console.log(musics_list);
  
  
  // Initialize components for Routine "musicrusselquad"
  musicrusselquadClock = new util.Clock();
  russellsQuad = new visual.ImageStim({
    win : psychoJS.window,
    name : 'russellsQuad', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.9, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  music = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  music.setVolume(1.0);
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  musictext = new visual.TextStim({
    win: psychoJS.window,
    name: 'musictext',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  fixCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixCross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "endblock"
  endblockClock = new util.Clock();
  goodbyetext = new visual.TextStim({
    win: psychoJS.window,
    name: 'goodbyetext',
    text: 'Terminado.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var startblockComponents;
function startblockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'startblock'-------
    t = 0;
    startblockClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    startblockComponents = [];
    startblockComponents.push(starttext);
    
    startblockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function startblockRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'startblock'-------
    // get current time
    t = startblockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *starttext* updates
    if (t >= 0.0 && starttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      starttext.tStart = t;  // (not accounting for frame time here)
      starttext.frameNStart = frameN;  // exact frame index
      
      starttext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (starttext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      starttext.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startblockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startblockRoutineEnd() {
  return async function () {
    //------Ending Routine 'startblock'-------
    startblockComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(musicrusselquadRoutineBegin(snapshot));
      trialsLoopScheduler.add(musicrusselquadRoutineEachFrame());
      trialsLoopScheduler.add(musicrusselquadRoutineEnd());
      trialsLoopScheduler.add(ISIRoutineBegin(snapshot));
      trialsLoopScheduler.add(ISIRoutineEachFrame());
      trialsLoopScheduler.add(ISIRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var mouse_locs;
var target;
var gotValidClick;
var musicrusselquadComponents;
function musicrusselquadRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'musicrusselquad'-------
    t = 0;
    musicrusselquadClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    mouse.clickReset();
    mouse_locs = [];
    target = musics_list.pop(0);
    
    russellsQuad.setImage('Russells-emotion-model.jpg');
    music = new sound.Sound({
    win: psychoJS.window,
    value: target,
    secs: 20.0,
    });
    music.secs=20.0;
    music.setVolume(1.0);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    gotValidClick = false; // until a click is received
    mouse.mouseClock.reset();
    musictext.setText(target);
    // keep track of which components have finished
    musicrusselquadComponents = [];
    musicrusselquadComponents.push(russellsQuad);
    musicrusselquadComponents.push(music);
    musicrusselquadComponents.push(mouse);
    musicrusselquadComponents.push(musictext);
    
    musicrusselquadComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var mouse_loc;
var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function musicrusselquadRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'musicrusselquad'-------
    // get current time
    t = musicrusselquadClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (mouse.isPressedIn(russellsQuad)) {
        mouse_loc = mouse.getPos();
        mouse_locs.push(mouse_loc);
        logging.log({"level": logging.DATA, "msg": mouse_loc});
        continueRoutine = false;
    }
    
    
    // *russellsQuad* updates
    if (t >= 0.0 && russellsQuad.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      russellsQuad.tStart = t;  // (not accounting for frame time here)
      russellsQuad.frameNStart = frameN;  // exact frame index
      
      russellsQuad.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (russellsQuad.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      russellsQuad.setAutoDraw(false);
    }
    // start/stop music
    if (t >= 0.0 && music.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      music.tStart = t;  // (not accounting for frame time here)
      music.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ music.play(); });  // screen flip
      music.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 20.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (music.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (20.0 > 0.5) {
        music.stop();  // stop the sound (if longer than duration)
      }
      music.status = PsychoJS.Status.FINISHED;
    }
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
        }
      }
    }
    
    // *musictext* updates
    if (t >= 0.0 && musictext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      musictext.tStart = t;  // (not accounting for frame time here)
      musictext.frameNStart = frameN;  // exact frame index
      
      musictext.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    musicrusselquadComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function musicrusselquadRoutineEnd() {
  return async function () {
    //------Ending Routine 'musicrusselquad'-------
    musicrusselquadComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    music.stop();  // ensure sound has stopped at end of routine
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    
    // the Routine "musicrusselquad" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var ISIComponents;
function ISIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'ISI'-------
    t = 0;
    ISIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ISIComponents = [];
    ISIComponents.push(fixCross);
    
    ISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ISIRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'ISI'-------
    // get current time
    t = ISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixCross* updates
    if (t >= 0.0 && fixCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixCross.tStart = t;  // (not accounting for frame time here)
      fixCross.frameNStart = frameN;  // exact frame index
      
      fixCross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixCross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixCross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ISIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISIRoutineEnd() {
  return async function () {
    //------Ending Routine 'ISI'-------
    ISIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var endblockComponents;
function endblockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'endblock'-------
    t = 0;
    endblockClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endblockComponents = [];
    endblockComponents.push(goodbyetext);
    
    endblockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endblockRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'endblock'-------
    // get current time
    t = endblockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *goodbyetext* updates
    if (t >= 0.0 && goodbyetext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goodbyetext.tStart = t;  // (not accounting for frame time here)
      goodbyetext.frameNStart = frameN;  // exact frame index
      
      goodbyetext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (goodbyetext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      goodbyetext.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endblockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endblockRoutineEnd() {
  return async function () {
    //------Ending Routine 'endblock'-------
    endblockComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
