import math
import logging
import random

import constants
import envelope


class WaveformSpec(object):
  """
  Holds all information necessary to create a waveform.
  """
  def __init__(self, freq_f, amp_f, sec_f, envelope, freq_delta_f=None):
    self._freq_f = freq_f
    self._amp_f = amp_f
    self._sec_f = sec_f
    self._envelope = envelope
    self._freq_delta_f = freq_delta_f

  def GetFreq(self):
    return self._freq_f

  def GetAmp(self):
    return self._amp_f

  def GetSec(self):
    return self._sec_f

  def GetEnvelope(self):
    return self._envelope

  def GetFreqDelta(self):
    return self._freq_delta_f

  def ComputeSamplesInt(self):
    return int(constants.FRAMERATE_F * self.GetSec())


def Sine(spec):
  assert isinstance(spec, WaveformSpec)
  sine_list = []

  # omega definition:
  # y = amp * sin(2*pi * freq_f * time)
  # rate of change in radians per sec
  omega = 2 * math.pi * spec.GetFreq()
  total_samples = spec.ComputeSamplesInt()

  for x in range(total_samples):
    # t is only changing variable, if freq_f doesn't change.
    # x = frame number
    # framerate = frames per second
    # t = position in seconds, as float
    t = x / constants.FRAMERATE_F

    # radians per sec * time position = total radians -> sine function = y value.
    y_value = math.sin(omega * t)

    # multiplied by constant amp factor
    # TODO: allow constant amp for a curve
    # amp_value = int(y_value * spec.GetAmp())
    amp_value = envelope.ModulateToInt(spec, t, y_value)

    sine_list.append(amp_value)

  return sine_list


def Square(spec):
  assert isinstance(spec, WaveformSpec)
  square_list = []
  flag = False
  frames_per_oscillation = constants.FRAMERATE_F / spec.GetFreq()

  for x in range(spec.ComputeSamplesInt()):
    # on or off is a square wave
    # this tells us if we're at a boundary point
    if x % frames_per_oscillation < 1.0:
      flag = not flag
      t = x / constants.FRAMERATE_F
      amp_value = int(flag * envelope.ModulateToInt(spec, t, 1.0))

    square_list.append(amp_value)

  return square_list


def WhiteNoise(spec):
  assert isinstance(spec, WaveformSpec)
  noise_list = []

  # Deviation around the median, but 0 < range < TWO_BIT_AMP_MAX
  highest = min(spec.GetFreq() + spec.GetFreqDelta(), constants.TWO_BIT_AMP_MAX)
  lowest = max(spec.GetFreq() - spec.GetFreqDelta(), 0)

  for _ in range(spec.ComputeSamplesInt()):
    amp_value = random.uniform(lowest, highest) * spec.GetAmp()
    noise_list.append(int(amp_value))
  return noise_list


# This should live here rather than in constants.py, since it refers to functions
# defined in this file. Otherwise constants.py would have to include this
# file, which would be a circular import.
WAVEFORMS_DICT = {'sine': Sine, 'square': Square, 'white': WhiteNoise}
