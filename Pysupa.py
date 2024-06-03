# -----------
# import 
# -----------
from flask import Flask
import webbrowser
import threading
from tkinter import filedialog
import os
import whisper

# -----------
# import 
# -----------
app = Flask(__name__)

filetype = [("Audiofile",".mp3 .wav")]
path = os.path.abspath(os.path.dirname(__file__))
cap_filepath = filedialog.askopenfilename(filetype = filetype, initialdir = path)

model = whisper.load_model("base")
result = model.transcribe(cap_filepath)
# file_object = open("audio_to_textfile","base")

print(result["text"])

# @app.route('./')



