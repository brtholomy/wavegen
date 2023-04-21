import constants


class Envelope(object):
  """
  In digital music terms, an "envelope" consists of:
  attack, decay, sustain, release

  For each we specify:
  1. target amp
  2. time

  Can assume constant slope for now. Unless logarithmic just sounds better.
  """

  def __init__(self, attack_sec_f=constants.DEFAULT_ATTACK, decay_sec_f=constants.DEFAULT_DECAY, release_sec_f=constants.DEFAULT_RELEASE):
    self._attack_sec_f = attack_sec_f
    self._decay_sec_f = decay_sec_f
    self._release_sec_f = release_sec_f

  def GetAttack(self):
    return self._attack_sec_f

  def GetDecay(self):
    return self._decay_sec_f

  def GetRelease(self):
    return self._release_sec_f


def ModulateToInt(spec, t, y):
  """
  The waveform func should call this to get the amp constant, and multiply it
  by the sine/sq result.
  """
  return int(ModulationValue(spec, t) * spec.GetAmp() * y)


def ModulationValue(spec, t):
  envelope = spec.GetEnvelope()
  sec_total = spec.GetSec()

  if t < envelope.GetAttack():
    # from 0 to 1.
    return t / envelope.GetAttack()

  elif t < envelope.GetAttack() + envelope.GetDecay():
    # 1 to 0.7
    ratio_complete = (t - envelope.GetAttack()) / envelope.GetDecay()
    return 1.0 - (0.3 * ratio_complete)

  elif t < sec_total - envelope.GetRelease():
    # Sustain 0.7
    return 0.7

  elif t > sec_total - envelope.GetRelease():
    release_beginning_pos = sec_total - envelope.GetRelease()
    ratio_complete = (t - release_beginning_pos) / envelope.GetRelease()
    # 0.7 to 0
    return 0.7 - (0.7 * ratio_complete)

  else:
    return 0.7
