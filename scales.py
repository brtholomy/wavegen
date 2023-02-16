from enum import IntEnum


class Pentatonic(IntEnum):
  # enum value is interval distance from tonic. Would be easier in looping to
  # specify the interval from previous note, but that's not typically how
  # musicians think of a scale.
  root = 0
  third = 3
  fourth = 5
  fifth = 7
  seventh = 10
  octave = 12


class Bhairavi(IntEnum):
  root = 0
  second = 1
  third = 4
  fourth = 5
  fifth = 7
  sixth = 8
  seventh = 11
  octave = 12

class Major(IntEnum):
  root = 0
  second = 2
  third = 4
  fourth = 5
  fifth = 7
  sixth = 9
  seventh = 11
  octave = 12

class Minor(IntEnum):
  root = 0
  second = 2
  third = 3
  fourth = 5
  fifth = 7
  sixth = 8
  seventh = 10
  octave = 12
