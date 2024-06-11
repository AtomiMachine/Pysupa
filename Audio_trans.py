# ---------
# import 
# ---------
import asyncio
import queue
from concurrent.futures import ThreadPoolExecutor

from transfromers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

import numpy as np
import sounddevice as sd
import time


# ---------
# import 
# ---------

running_status = True

print("利用可能デバイスを表示します。")
print(sd.query_devices())

# 無音チェックする
def silentcheck(data, threshold = 0.01):
  return np.max(np.abs(data)) < threshold

# 音がなっているかチェック
def in_voicedheck(data, threshold = 0.02):
  return np.max(np.abs(data)) > threshold

# 録音する
def recordingaudio(q, max_record_duration, silence_duration, device_index):
  global running_status
  while sd.InputStream(samplerate=16000, channels=3, callback=None , dtype= 'float64', device=device_index):
    while running_status:
      audio_data = sd.rec(int(max_record_duration * 16000),samplerate=16000, channels=3)
      # 録音終了するまで待機する
      sd.wait()
      audio_data = np.squeeze(audio_data)

      #録音データに音声が含まれていない場合の処理
      if not in_voicedheck(audio_data):
        continue

      for i in range(0, len(audio_data), int(16000 * silence_duration)):
        window = audio_data[i:i + int(16000 * silence_duration)]
        if silentcheck(window):
          audio_data = audio_data[:i]
          break

    q.put(audio_data)
    del audio_data      
def transcribe_audio(q,pipe,output_buff,max_buffer_time, max_buffer_size):
  global running_status
  buffer_content = ""
  last_output_time = time.time()

  while running_status:
    try:
      audio_data = q.get(timeout=1)  #timeout = キューから取得する秒数を決めている
    except queue.Empty:
      continue
    
    result = pipe(audio_data)
    text = result("text")
    buffer_content += text + " "
    current_time = time.time()

    if (current_time -last_output_time > max_buffer_time) or (len(buffer_content) >= max_buffer_size):
      output_buff.put(buffer_content.strip())
      buffer_content = ""
      last_output_time = current_time
    del audio_data

def output_transcription(output_buffer, filename):
    global running
    while running:
        try:
            text = output_buffer.get(timeout=1)  # 1秒間待ってからキューから取得
        except queue.Empty:
            continue

        with open(filename, "a") as file:
            file.write(text + "\n")

def main():
    global running
    # モデルとプロセッサの設定
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model_id = "distil-whisper/distil-small.en"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True)
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)