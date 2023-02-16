import constants
import envelope
import note
import waveforms

COMMON_TIME = 4


def NoteSequence(bpm_int, beats_per_measure_f, amp_f, wavefunc, GetNoteFreq, GetMeasureRatio, GetMore):
  total_list = []
  more = "y"
  note_list = note.NoteList()
  # just for representation
  note_seq = []

  while more == "y":
    note_name, freq_f = GetNoteFreq()
    measure_ratio_int = GetMeasureRatio()

    sec_f = NotesPerMeasureToSec(measure_ratio_int, beats_per_measure_f, bpm_int)
    spec = waveforms.WaveformSpec(freq_f, amp_f, sec_f, envelope.Envelope())

    new_note = note.Note(wavefunc, spec)
    note_list.Append(new_note)

    note_seq.append((note_name, measure_ratio_int))
    print(note_seq)
    more = GetMore()

  total_list = note.GenerateAmplitudeList(note_list)
  return total_list


def NotesPerMeasureToSec(measure_ratio_int, beats_per_measure_f, bpm_int):
  # In common time 4/4:
  # 1 measure_ratio = 4 beat_ratio
  # 2 measure_ratio = 2 beat_ratio
  # 4 measure_ratio = 1 beat_ratio
  # 8 measure_ratio = 0.5 beat_ratio
  # 16 measure_ratio = 0.25 beat_ratio
  beat_ratio_f = beats_per_measure_f / measure_ratio_int
  sec_per_beat_f = float(60.0 / bpm_int)
  sec_f  = sec_per_beat_f * beat_ratio_f
  return sec_f


def ArpeggiatorSequence(
    amp_f,
    sec_f,
    wavefunc,
    keyscale):
  total_list = []
  note_list = note.NoteList()
  # just for representation
  # note_seq = []

  for freq_f in keyscale:
    spec = waveforms.WaveformSpec(freq_f, amp_f, sec_f, envelope.Envelope())

    new_note = note.Note(wavefunc, spec)
    note_list.Append(new_note)

  total_list = note.GenerateAmplitudeList(note_list)
  return total_list
