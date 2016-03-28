"""
String constants and colors used across the graphs.
"""

from __future__ import division
import os

import datetime
import pyqtgraph as pg

#String constants used in the graphs
CORRECT_DISCRIMINATION_RATE = "Discrimination Rate"
SPLUS_RESPONSE_RATE = "S+ Response Rate"
SMINUS_REJECT_RATE = "S- Reject Rate"
TASK_ERROR_RATE = "Task Error Rate"

TOTAL_ML = "Total mL"
ML_PER_HOUR = "mL / Hour"
NUM_TRIALS = "Trials (x10)"
TRAINING_MINUTES = "Training Time (Minutes)"

TRIALS_PER_HOUR = "Trials (x10) / Hour"

CHANGES = "Changes"

LICK = "Lick"
TAP = "Tap"
STATE = "State"
HINT = "Hint"
REWARD = "Reward"

SESSION_START_TIME = "Session Start Time"

#These are state descriptions used only in graphing context for now
GRAPH_MEMORY_DELAY = "Memory Delay"
GRAPH_TIMING_DELAY = "Timing Delay"
GRAPH_SMINUS_GRATING = "S- Grating"
GRAPH_SPLUS_GRATING = "S+ Grating"
GRAPH_NON_REWARD = "Non-reward"
GRAPH_REWARD = "Reward"

STATE_MAX_DURATIONS = "State Max Durations"
LICK_INFO = "Lick Info"


DATA_DIR = os.getcwd()
#Find the ShrewData dir and assign it to DATA_DIR.
for i in range(10):
    if os.path.isdir(DATA_DIR + os.sep + "ShrewData"):
        DATA_DIR = DATA_DIR + os.sep + "ShrewData"
        break
    else:
        DATA_DIR += os.sep + ".."

def get_color(name):
    """Colors for each name."""
    if name == TAP:
        return 0,255,0  # green
    elif name == LICK or name == CHANGES:
        return 255,0,0  # red
    elif name == STATE:
        return 128,128,128  # gray
    elif name == HINT:
        return 255,255,0  # yellow
    elif name == REWARD or name == TOTAL_ML:
        return 0,128,255  # friendly blue
    elif name == CORRECT_DISCRIMINATION_RATE:
        return 0,255,255,  # cyan
    elif name == SPLUS_RESPONSE_RATE:
        return 255,0,128  # neon pink
    elif name == SMINUS_REJECT_RATE:
        return 255,0,255  # magenta
    elif name == TASK_ERROR_RATE:
        return 255,128,0  # orange
    elif name == TOTAL_ML:
        return 0,0,255  # blue
    elif name == ML_PER_HOUR:
        return 128,0,255  # ultramarine or something
    elif name == NUM_TRIALS:
        return 255,128,128  # peach
    elif name == TRAINING_MINUTES:
        return 0,255,0  # green
    elif name == CHANGES:
        return 255,64,0  # redsy
    else:
        return 255,255,255  # white

