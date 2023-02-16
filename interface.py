import logging
import sys

import constants
import envelope
import sequencer
import waveforms


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


def GetMore():
  return str(input("Add more notes? y | n\n:"))


def GetBpm():
  bpm_int = int(input("BPM? 30 - 400\n:") or constants.DEFAULT_BPM)
  assert 30 <= bpm_int <= 400
  return bpm_int


def GetMeasure():
  beats_per_measure_f = float(input("Beats per measure? 3 - 8 \n:") or constants.DEFAULT_MEASURE)
  assert 3 <= beats_per_measure_f <= 8
  return beats_per_measure_f


def GetAmplitude():
  amp_ratio_f = float(input("Amplitude? 0.1 - 1.0\n:") or constants.DEFAULT_AMP)
  assert 0 < amp_ratio_f <= 1
  amp_f = amp_ratio_f * constants.TWO_BIT_AMP_MAX
  return amp_f


def GetNoteFreq():
  note_name = str(input("Note? eg, A4 \n:") or constants.DEFAULT_NOTE)
  freq_f = constants.KEYBOARD[note_name]
  return note_name, freq_f


def GetMeasureRatio():
  measure_ratio_int = int(input("Note length? 1: whole | 2: half | 4: quarter | 8: eighth | 16: sixteenth | 32: thirtysecond \n:") or constants.DEFAULT_NOTE_LENGTH)
  return measure_ratio_int


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

  elif mode == 'notes':
    form = GetWaveForm()
    wavefunc = waveforms.WAVEFORMS_DICT[form]
    bpm_int = GetBpm()
    beats_per_measure_f = GetMeasure()
    amp_f = GetAmplitude()
    total_list = sequencer.NoteSequence(
      bpm_int, beats_per_measure_f, amp_f, wavefunc, GetNoteFreq, GetMeasureRatio, GetMore)

  return total_list
