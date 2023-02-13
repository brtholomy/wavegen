import collections
import logging

# what do I want the interface to be?
# I want to generate notes, with:
# 1. waveform
# 2. freq
# 3. amp
# 3. duration


class Note(object):
  def __init__(self, waveform_func, waveform_spec):
    self._waveform_func = waveform_func
    self._waveform_spec = waveform_spec

  def GetFunc(self):
    return self._waveform_func

  def GetSpec(self):
    return self._waveform_spec


class NoteList(object):
  def __init__(self):
    self._notes = []

  def Append(self, note):
    self._notes.append(note)

  def GetList(self):
    return self._notes

# How do I want to generate amplitude lists? A separate function? I envision
# adding notes on the fly, then processing to produce the file?

def GenerateAmplitudeList(notes):
  assert isinstance(notes, NoteList)
  amp_list = []

  for note in notes.GetList():
    func = note.GetFunc()
    amp = func(note.GetSpec())
    # logging.debug("amp: %f", amp)
    amp_list.extend(amp)

  return amp_list
