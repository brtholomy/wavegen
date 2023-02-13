import constants
import struct
import wave

def WriteWaveFile(total_list, filename_str, channels_int, sampwidth_int, framerate_f, data_size_int):

  wav_file = wave.open(filename_str, "w")

  wav_file.setparams((channels_int, sampwidth_int, int(framerate_f), data_size_int,
                     constants.COMPRESSION_TYPE, constants.COMPRESSION_NAME))

  for s in total_list:
    wav_file.writeframes(struct.pack('h', s))

  wav_file.close()
