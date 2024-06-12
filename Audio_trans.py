import sounddevice as sd
import numpy as np


class Audio():

  samplerate =44100
  channels = 2
  frame = 1024
  # しきい値
  threshold = 0.01  

  device_list = sd.query_devices()
  print(device_list)

  sd.default.device = [1, 4]

  if (=0.1)