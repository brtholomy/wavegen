COMMON_TIME = 4

def NotesPerMeasureToSec(measure_ratio_int, beats_per_measure_f, bpm_int):
  # In common time 4/4:
  # 1 measure_ratio = 4 beat_ratio
  # 2 measure_ratio = 2 beat_ratio
  # 4 measure_ratio = 1 beat_ratio
  # 8 measure_ratio = 0.5 beat_ratio
  # 16 measure_ratio = 0.25 beat_ratio
  beat_ratio_f = beats_per_measure_f / measure_ratio_int
  print(beat_ratio_f)
  sec_per_beat_f = float(60.0 / bpm_int)
  print(sec_per_beat_f)
  sec_f  = sec_per_beat_f * beat_ratio_f
  print(sec_f)
  return sec_f
