# Wavegen

Interactive tool for .wav file generation.

The point is mostly to study properties of acoustics and harmonics, such as scale dynamics and irrationals in music theory.

run:

```
./wavegen.sh
```

## TODO

* Improve the interface for easier experimentation. Switch to CLI flags rather than interactive.
* Add envelope configuration to the interface. The constructs already accept arbitrary values for attack, sustain, and decay.
* Implement logarithmic distributions for frequency, amplitude, and scale interval.
* Add more exotic scales, possibly all 12 Greek + a few core Indian ragas.

## Won't do

* Play audio on the fly. Much simpler just to create files.
* Combine waveforms. The DAW can do that.
