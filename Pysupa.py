# -----------
# import 
# -----------
from flask import Flask
import webbrowser
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import whisper

# -----------
# import 
# -----------
app = Flask(__name__)

def recoded_serect():
  filetype = [("Audiofile",".mp3 .wav")]
  path = os.path.abspath(os.path.dirname(__file__))
  # cap_filepath = filedialog.askopenfilename(filetype = filetype, initialdir = path)
  cap_filepath = filedialog.askopenfilename(filetype = filetype, initialdir = path)
  #model = whisper.load_model("base")
  #result = model.transcribe(cap_filepath)
  # file_object = open("audio_to_textfile","base")

#rootウィンドウの設定
root = tk.Tk()
root.title("PySUPA")
root.geometry("512x256")

#メインフレーム
frame = ttk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)

#インスタンスを格納する変数
real_timebutton_text = tk.StringVar(frame)
recorded_data_text = tk.StringVar(frame)
real_timebutton_text.set("リアルタイム出力")
recorded_data_text.set("録音済みデータ")


real_timebutton = tk.Button(frame,textvariable = real_timebutton_text, )
recorded_button = tk.Button(frame,textvariable = recorded_data_text, command = recoded_serect)
#配置
real_timebutton.pack()
recorded_button.pack()

root.attributes("-topmost", True)
root.mainloop()



#print(result["text"])

# @app.route('./')