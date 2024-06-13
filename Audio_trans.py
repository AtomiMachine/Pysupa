import sounddevice as sd
import numpy as np



def Audio(rectime):
  sd.default.device = [1, 4]   
  fs = 48000 #サンプリング周波数
  # f0 = 440 #周波数
  rectime = 3 #再生時間
  audio_data = sd.rec(int(rectime * fs),fs,channels=1)
  # t = np.linspace(0, rectime, rectime * fs, endpoint=False)
  # x = np.sin(2*np.pi*f0*t)
  # sd.play(x, fs)
  sd.wait()  

  return audio_data

# device_list = sd.query_devices()
# print(device_list)
# # 無音検知関数
# def is_silent(sounddata,threshold = 0.01):
#   return np.max(np.abs(sounddata)) < threshold

# # 音声検知関数
# def in_voice(sounddata,threshold = 0.02):
#   return np. max(np.abs(sounddata)) > threshold
# sd.default.device = [1, 4]   