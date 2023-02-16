import logging
import sys

import constants
import envelope
import sequencer
import waveforms


def MasterInterface():
  modes = ['pure', 'notes']
  mode = str(constants.ShortForm(input(
    "Pure waveform, manual sequence\n" +
    "[p]ure | [n]otes | [a]rp \n:")
                                 ) or constants.DEFAULT_SOUND_TYPE)
  if mode not in modes:
    sys.exit("Unsupported mode!")

  total_list = []
  if mode == 'pure':
    form = GetWaveForm()
    sec_f = GetDuration()

    if form == "sine":
      freq_f = GetFreq()
      spec = waveforms.WaveformSpec(freq_f, constants.TWO_BIT_AMP_MAX, sec_f, envelope.Envelope())
      total_list = waveforms.Sine(spec)

    elif form == "square":
      freq_f = GetFreq()
      spec = waveforms.WaveformSpec(freq_f, constants.TWO_BIT_AMP_MAX, sec_f, envelope.Envelope())
      total_list = waveforms.Square(spec)

    elif form == "white":
      freq_f = GetWhiteFreq()
      deviation_f = GetWhiteDeviation()
      # I think this always stays at 1.0, because we're not generating sine waves
      # from radians, just absolute amplitudes.
      amp_f = 1.0
      spec = waveforms.WaveformSpec(freq_f, amp_f, sec_f, envelope.Envelope(), deviation_f)
      total_list = waveforms.WhiteNoise(spec)

  elif mode == 'notes':
    total_list = sequencer.NoteSequence()

  return total_list


def GetWaveForm():
  form = str(constants.ShortForm(input(
    "Waveform type? [s]ine | [sq]uare | [w]hite \n:")) or constants.DEFAULT_WAVEFORM_TYPE)
  if form not in waveforms.WAVEFORMS_DICT.keys():
    sys.exit("Unsupported waveform!")
  return form


def GetDuration():
  return int(input("Seconds?\n:") or constants.DEFAULT_DURATION)


def GetFreq():
  return float(input("Freq? eg, 220\n:") or constants.DEFAULT_FREQ)


def GetWhiteFreq():
  return float(input("Median freq? eg, 20000\n:") or constants.DEFAULT_WHITENOISE_FREQ)


def GetWhiteDeviation():
  return float(input("Deviation? eg, 10000\n:") or constants.DEFAULT_WHITENOISE_DEVIATION)
