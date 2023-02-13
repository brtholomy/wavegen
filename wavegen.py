import datetime
import math
import logging
import sys

import constants
import interface
import waveforms
import write_wave_file


logging.basicConfig(filename=constants.LOG_FILE_STR, level=logging.DEBUG, format='%(message)s')
logging.info("\n----------------\n" + "filename: " + constants.FILENAME_STR)
logging.info("Run at: %s", datetime.datetime.now())
logging.info("frame rate: %s", constants.FRAMERATE_F)
logging.info("sample width: %s", constants.SAMPWIDTH_INT)


if __name__ == '__main__':
  total_list = interface.MasterInterface()

  write_wave_file.WriteWaveFile(
    total_list,
    constants.FILENAME_STR,
    constants.MONO,
    constants.SAMPWIDTH_INT,
    constants.FRAMERATE_F,
    len(total_list)
  )
