import logging
import sys
import math

import arpeggiator
import constants
import envelope
import sequencer
import scales
import waveforms


def GetMode():
  modestr = constants.ShortForm(input(
    "Simple waveform, manual sequence, or arpeggiator?\n" +
    "[s]imple | [n]otes | [a]rp | [l]og \n:")
                                 ) or constants.DEFAULT_SOUND_TYPE
  try:
    mode = constants.MODES[modestr]
  except:
    raise ValueError(f'Unsupported mode: {modestr}')
  return mode


def GetWaveForm():
  form = str(constants.ShortForm(input(
    "Waveform type? [sin]e | [sq]uare | [w]hite \n:")) or constants.DEFAULT_WAVEFORM_TYPE)
  if form not in waveforms.WAVEFORMS_DICT.keys():
    raise ValueError(f"Unsupported waveform: {form}")
  return form


def GetDuration():
  return float(input("Seconds?\n:") or constants.DEFAULT_DURATION)


def GetFreq():
  return float(input("Freq? eg, 220\n:") or constants.DEFAULT_FREQ)


def GetWhiteFreq():
  return float(input("Median freq? eg, 20000\n:") or constants.DEFAULT_WHITENOISE_FREQ)


def GetWhiteDeviation():
  return float(input("Deviation? eg, 10000\n:") or constants.DEFAULT_WHITENOISE_DEVIATION)


def GetMore():
  return str(input("Add more notes? y | n\n:"))


def GetBpm():
  bpm_int = int(input("BPM? 30 - 400\n:") or constants.DEFAULT_BPM)
  if not 30 <= bpm_int <= 400:
    raise ValueError(f"Invalid beats per minute: {bpm_int}")
  return bpm_int


def GetMeasure():
  beats_per_measure_f = float(input("Beats per measure? 3 - 16 \n:") or constants.DEFAULT_MEASURE)
  if not 3 <= beats_per_measure_f <= 16:
    raise ValueError(f"Invalid beats per measure: {beats_per_measure_f}")
  return beats_per_measure_f


def GetAmplitude():
  amp_ratio_f = float(input("Amplitude? 0.1 - 1.0\n:") or constants.DEFAULT_AMP)
  if not 0 < amp_ratio_f <= 1:
    raise ValueError(f"Invalid amplitude: {amp_ratio_f}")
  amp_f = amp_ratio_f * constants.TWO_BIT_AMP_MAX
  return amp_f


def GetNoteFreq():
  note_name = str(input("Note? eg, A4 \n:") or constants.DEFAULT_NOTE)
  if note_name not in constants.KEYBOARD:
    raise ValueError(f"Note not found in keyboard: {note_name}")
  freq_f = constants.KEYBOARD[note_name]
  return note_name, freq_f


def GetMeasureRatio():
  measure_ratio_int = int(input("Note length? 1: whole | 2: half | 4: quarter | 8: eighth | 16: sixteenth | 32: thirtysecond \n:") or constants.DEFAULT_NOTE_LENGTH)
  return measure_ratio_int


def GetScale():
  scalestr = str(constants.ShortForm(input(
    "Scale? [p]entatonic | [b]hairavi | [maj]or | [min]or \n:")) or constants.DEFAULT_SCALE)
  if scalestr not in constants.SCALES:
    raise ValueError(f"Unsupported scale: {scalestr}")
  return constants.SCALES[scalestr]

def GetLimitN():
  limitn = int(input("Limit of n? eg, 100\n:") or constants.DEFAULT_LIMITN)
  return limitn

def MasterInterface():
  mode = GetMode()
  total_list = []
  if mode is constants.MODES.simple:
    form = GetWaveForm()
    wavefunc = waveforms.WAVEFORMS_DICT[form]
    sec_f = GetDuration()

    if form in ("sine", "square"):
      freq_f = GetFreq()
      spec = waveforms.WaveformSpec(freq_f, constants.TWO_BIT_AMP_MAX, sec_f, envelope.Envelope())
      total_list = wavefunc(spec)

    elif form == "white":
      freq_f = GetWhiteFreq()
      deviation_f = GetWhiteDeviation()
      # I think this always stays at 1.0, because we're not generating sine waves
      # from radians, just absolute amplitudes.
      amp_f = 1.0
      spec = waveforms.WaveformSpec(freq_f, amp_f, sec_f, envelope.Envelope(), deviation_f)
      total_list = wavefunc(spec)

  elif mode is constants.MODES.notes:
    form = GetWaveForm()
    wavefunc = waveforms.WAVEFORMS_DICT[form]
    bpm_int = GetBpm()
    beats_per_measure_f = GetMeasure()
    amp_f = GetAmplitude()
    total_list = sequencer.NoteSequence(
      bpm_int, beats_per_measure_f, amp_f, wavefunc, GetNoteFreq, GetMeasureRatio, GetMore)

  elif mode is constants.MODES.arpeggiator:
    form = GetWaveForm()
    wavefunc = waveforms.WAVEFORMS_DICT[form]
    bpm_int = GetBpm()
    beats_per_measure_f = GetMeasure()
    measure_ratio_int = GetMeasureRatio()
    amp_f = GetAmplitude()
    # TODO: ask the user for the scale
    scale = GetScale()
    root, freq_f = GetNoteFreq()

    sec_f = sequencer.NotesPerMeasureToSec(measure_ratio_int, beats_per_measure_f, bpm_int)
    keyscale = arpeggiator.GetKeyScale(constants.KEYBOARD, scale, root)
    total_list = sequencer.ArpeggiatorSequence(amp_f, sec_f, wavefunc, keyscale)

  if mode is constants.MODES.log:
    form = GetWaveForm()
    wavefunc = waveforms.WAVEFORMS_DICT[form]
    sec_f = GetDuration()
    amp_f = GetAmplitude()
    freq_f = GetFreq()
    limitn = GetLimitN()
    # (1 + 1/n)^n
    factor_func = lambda i: (1 + 1/i)**i
    total_list = sequencer.FreqSequence(amp_f, wavefunc, freq_f, sec_f,
                                        factor_func, limitn)

  return total_list
