import itertools

import constants
import scales


def GetKeyScale(keyboard, scale, root):
  """Creates a list of frequencies as float values, representing notes along a
  scale. The frequencies are provided by the keyboard dict, while the scale
  enum provides the interval distance from the root.
  """
  if len(keyboard.keys()) < 12:
    raise IndexError('keyboard is too small')

  # this feels too hacky. probably shouldn't be an OrderedDict if I want indexing.
  root_i = list(keyboard.keys()).index(root)
  allkeys = list(keyboard.keys())[root_i:]
  freqscale = []

  i, tonic_i = 0, 0
  for interval in itertools.cycle(scale):
    if not tonic_i <= i + interval < len(allkeys):
      break

    # if at octave, we set the next tonic and begin again
    if interval.name == 'octave':
      tonic_i += interval
      i = tonic_i
      continue

    # current tonic index, plus the interval of the scale
    i = tonic_i + interval

    freq = keyboard[allkeys[i]]
    freqscale.append(freq)

  return freqscale


if __name__ == '__main__':

  # print(list(constants.KEYBOARD.keys()).index('C4'))

  keyscale = GetKeyScale(constants.KEYBOARD, scales.Pentatonic, 'A0')
  print(keyscale)
