import collections
from enum import Enum

import scales


LOG_FILE_STR = "./output/log/wave_log.txt"

################################################################################
# these all get passed into the "wave" module, via write_wave_file.py:

# amplitude is peak deviation from zero
TWO_BIT_AMP_MAX = 32767.0

MONO = 1
STEREO = 2

COMPRESSION_TYPE = "NONE"
COMPRESSION_NAME = "not compressed"

FRAMERATE_F = 11025.0
SAMPWIDTH_INT = 2
FILENAME_STR = "output/output.wav"

################################################################################
# user interface strings

MODES = Enum('modes', ['simple', 'notes', 'arpeggiator', 'log'])

SCALES = {
  'pentatonic' : scales.Pentatonic,
  'bhairavi' : scales.Bhairavi,
  'major' : scales.Major,
  'minor' : scales.Minor,
}

# TODO: fix this duplication, get rid of ShortForm(). Use Enums everywhere.
SHORTFORMS = {
  '' : None,
  's' : 'simple',
  'n' : 'notes',
  'a' : 'arpeggiator',
  'l' : 'log',
  'sin' : 'sine',
  'sq' : 'square',
  'w' : 'white',
  'p' : 'pentatonic',
  'b' : 'bhairavi',
  'maj' : 'major',
  'min' : 'minor',
}

def ShortForm(cmd):
  return SHORTFORMS[cmd]

################################################################################
# used in our wave generation functions

DEFAULT_SOUND_TYPE = "simple"
DEFAULT_WAVEFORM_TYPE = "sine"
DEFAULT_DURATION = 3
DEFAULT_FREQ = 220.0
DEFAULT_WHITENOISE_FREQ = 20000.0
DEFAULT_WHITENOISE_DEVIATION = 10000.0
DEFAULT_BPM = 90
DEFAULT_MEASURE = 4
DEFAULT_NOTE = 'A4'
DEFAULT_AMP = 0.3
DEFAULT_NOTE_LENGTH = 4
DEFAULT_SCALE = 'pentatonic'
DEFAULT_ATTACK = 0.2
DEFAULT_DECAY = 0.2
DEFAULT_RELEASE = 0.4
DEFAULT_LIMITN = 100

################################################################################
# Frequency constants

DEFAULT_MAX_FREQ = 40000.0

# tempered chromatic scale. 'name' : Hz
KEYBOARD = collections.OrderedDict()
KEYBOARD['rest'] = 0.0
KEYBOARD['C0'] = 16.35
KEYBOARD['Db0'] = 17.32
KEYBOARD['D0'] = 18.35
KEYBOARD['Eb0'] = 19.45
KEYBOARD['E0'] = 20.6
KEYBOARD['F0'] = 21.83
KEYBOARD['Gb0'] = 23.12
KEYBOARD['G0'] = 24.5
KEYBOARD['Ab0'] = 25.96
KEYBOARD['A0'] = 27.5
KEYBOARD['Bb0'] = 29.14
KEYBOARD['B0'] = 30.87
KEYBOARD['C1'] = 32.7
KEYBOARD['Db1'] = 34.65
KEYBOARD['D1'] = 36.71
KEYBOARD['Eb1'] = 38.89
KEYBOARD['E1'] = 41.2
KEYBOARD['F1'] = 43.65
KEYBOARD['Gb1'] = 46.25
KEYBOARD['G1'] = 49
KEYBOARD['Ab1'] = 51.91
KEYBOARD['A1'] = 55
KEYBOARD['Bb1'] = 58.27
KEYBOARD['B1'] = 61.74
KEYBOARD['C2'] = 65.41
KEYBOARD['Db2'] = 69.3
KEYBOARD['D2'] = 73.42
KEYBOARD['Eb2'] = 77.78
KEYBOARD['E2'] = 82.41
KEYBOARD['F2'] = 87.31
KEYBOARD['Gb2'] = 92.5
KEYBOARD['G2'] = 98
KEYBOARD['Ab2'] = 103.83
KEYBOARD['A2'] = 110
KEYBOARD['Bb2'] = 116.54
KEYBOARD['B2'] = 123.47
KEYBOARD['C3'] = 130.81
KEYBOARD['Db3'] = 138.59
KEYBOARD['D3'] = 146.83
KEYBOARD['Eb3'] = 155.56
KEYBOARD['E3'] = 164.81
KEYBOARD['F3'] = 174.61
KEYBOARD['Gb3'] = 185
KEYBOARD['G3'] = 196
KEYBOARD['Ab3'] = 207.65
KEYBOARD['A3'] = 220
KEYBOARD['Bb3'] = 233.08
KEYBOARD['B3'] = 246.94
KEYBOARD['C4'] = 261.63
KEYBOARD['Db4'] = 277.18
KEYBOARD['D4'] = 293.66
KEYBOARD['Eb4'] = 311.13
KEYBOARD['E4'] = 329.63
KEYBOARD['F4'] = 349.23
KEYBOARD['Gb4'] = 369.99
KEYBOARD['G4'] = 392
KEYBOARD['Ab4'] = 415.3
KEYBOARD['A4'] = 440
KEYBOARD['Bb4'] = 466.16
KEYBOARD['B4'] = 493.88
KEYBOARD['C5'] = 523.25
KEYBOARD['Db5'] = 554.37
KEYBOARD['D5'] = 587.33
KEYBOARD['Eb5'] = 622.25
KEYBOARD['E5'] = 659.25
KEYBOARD['F5'] = 698.46
KEYBOARD['Gb5'] = 739.99
KEYBOARD['G5'] = 783.99
KEYBOARD['Ab5'] = 830.61
KEYBOARD['A5'] = 880
KEYBOARD['Bb5'] = 932.33
KEYBOARD['B5'] = 987.77
KEYBOARD['C6'] = 1046.5
KEYBOARD['Db6'] = 1108.73
KEYBOARD['D6'] = 1174.66
KEYBOARD['Eb6'] = 1244.51
KEYBOARD['E6'] = 1318.51
KEYBOARD['F6'] = 1396.91
KEYBOARD['Gb6'] = 1479.98
KEYBOARD['G6'] = 1567.98
KEYBOARD['Ab6'] = 1661.22
KEYBOARD['A6'] = 1760
KEYBOARD['Bb6'] = 1864.66
KEYBOARD['B6'] = 1975.53
KEYBOARD['C7'] = 2093
KEYBOARD['Db7'] = 2217.46
KEYBOARD['D7'] = 2349.32
KEYBOARD['Eb7'] = 2489.02
KEYBOARD['E7'] = 2637.02
KEYBOARD['F7'] = 2793.83
KEYBOARD['Gb7'] = 2959.96
KEYBOARD['G7'] = 3135.96
KEYBOARD['Ab7'] = 3322.44
KEYBOARD['A7'] = 3520
KEYBOARD['Bb7'] = 3729.31
KEYBOARD['B7'] = 3951.07
KEYBOARD['C8'] = 4186.01
KEYBOARD['Db8'] = 4434.92
KEYBOARD['D8'] = 4698.63
KEYBOARD['Eb8'] = 4978.03
KEYBOARD['E8'] = 5274.04
KEYBOARD['F8'] = 5587.65
KEYBOARD['Gb8'] = 5919.91
KEYBOARD['G8'] = 6271.93
KEYBOARD['Ab8'] = 6644.88
KEYBOARD['A8'] = 7040
KEYBOARD['Bb8'] = 7458.62
KEYBOARD['B8'] = 7902.13
