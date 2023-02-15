import logging
import sys

import constants
import sequencer


def MasterInterface():
  modes = ['pure', 'notes']
  mode = str(constants.ShortForm(input(
    "Pure waveform, manual note sequence, or arpeggiator? [p]ure | [n]otes | [a]rp \n:")
                       ) or constants.DEFAULT_SOUND_TYPE)
  if mode not in modes:
    sys.exit("Unsupported mode!")

  total_list = []
  if mode == 'pure':
    total_list = sequencer.PureMode()
  elif mode == 'notes':
    total_list = sequencer.NoteSequence()

  return total_list
