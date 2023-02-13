import logging
import sys

import constants
import envelope
import note
import sequencer
import waveforms


def MasterInterface():
  modes = ['pure', 'notes']
  mode = str(ShortForm(input(
    "Pure waveform or note sequence? [p]ure | [n]otes \n:")) or constants.DEFAULT_SOUND_TYPE)
  if mode not in modes:
    sys.exit("Unsupported mode!")

  total_list = []
  if mode == 'pure':
    total_list = PureMode()
  elif mode == 'notes':
    total_list = NoteSequencer()

  return total_list


def ShortForm(cmd):
  return constants.SHORTFORMS[cmd]


def PureMode():
  total_list = []

  form = str(ShortForm(input(
    "Waveform type? [s]ine | [sq]uare | [w]hite \n:")) or constants.DEFAULT_WAVEFORM_TYPE)
  if form not in waveforms.WAVEFORMS_DICT.keys():
    sys.exit("Unsupported waveform!")
  sec_f = int(input("Seconds?\n:") or constants.DEFAULT_DURATION)

  if form == "sine":
    freq_f = float(input("Freq? eg, 220\n:") or constants.DEFAULT_FREQ)
    spec = waveforms.WaveformSpec(freq_f, constants.TWO_BIT_AMP_MAX, sec_f, envelope.Envelope())
    total_list = waveforms.Sine(spec)

  elif form == "square":
    freq_f = float(input("Freq? eg, 220\n:") or constants.DEFAULT_FREQ)
    spec = waveforms.WaveformSpec(freq_f, constants.TWO_BIT_AMP_MAX, sec_f, envelope.Envelope())
    total_list = waveforms.Square(spec)

  elif form == "white":
    freq_f = float(input("Median freq? eg, 20000\n:") or constants.DEFAULT_WHITENOISE_FREQ)
    deviation_f = float(input("Deviation? eg, 10000\n:") or constants.DEFAULT_WHITENOISE_DEVIATION)

    # I think this always stays at 1.0, because we're not generating sine waves
    # from radians, just absolute amplitudes.
    amp_f = 1.0
    spec = waveforms.WaveformSpec(freq_f, amp_f, sec_f, envelope.Envelope(), deviation_f)
    total_list = waveforms.WhiteNoise(spec)

  return total_list


def NoteSequencer():
  total_list = []
  more = "y"
  note_list = note.NoteList()
  note_seq = []

  bpm_int = int(input("BPM? 30 - 400\n:") or constants.DEFAULT_BPM)
  assert 30 <= bpm_int <= 400

  beats_per_measure_f = float(input("Beats per measure? 3 - 8 \n:") or constants.DEFAULT_MEASURE)
  assert 3 <= beats_per_measure_f <= 8

  func_name = str(ShortForm(input(
    "Waveform type? [s]ine | [sq]uare | [w]hite \n:")) or constants.DEFAULT_WAVEFORM_TYPE)
  if func_name not in waveforms.WAVEFORMS_DICT.keys():
    sys.exit("Unsupported waveform!")
  else:
    func = waveforms.WAVEFORMS_DICT[func_name]

  amp_ratio_f = float(input("Amplitude? 0.1 - 1.0\n:") or constants.DEFAULT_AMP)
  assert 0 < amp_ratio_f <= 1
  amp_f = amp_ratio_f * constants.TWO_BIT_AMP_MAX

  while more == "y":
    note_name = str(input("Note? eg, A4 \n:") or constants.DEFAULT_NOTE)
    freq_f = constants.KEYBOARD[note_name]
    measure_ratio_int = int(input("Note length? 1: whole | 2: half | 4: quarter | 8: eighth | 16: sixteenth | 32: thirtysecond \n:") or constants.DEFAULT_NOTE_LENGTH)
    sec_f = sequencer.NotesPerMeasureToSec(measure_ratio_int, beats_per_measure_f, bpm_int)

    spec = waveforms.WaveformSpec(freq_f, amp_f, sec_f, envelope.Envelope())

    new_note = note.Note(func, spec)
    note_list.Append(new_note)

    note_seq.append((note_name, measure_ratio_int))
    print(note_seq)
    more = str(input("Add more notes? y | n\n:"))

  total_list = note.GenerateAmplitudeList(note_list)
  return total_list
