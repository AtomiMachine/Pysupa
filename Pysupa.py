# -----------
# import 
# -----------
from flask import Flask
import webbrowser
import threading
from tkinter import filedialog
import os
# -----------
# import 
# -----------
app = Flask(__name__)

filetype = [("Audiofile",".mp3 .wav")]
path = os.path.abspath(os.path.dirname(__file__))
cap_filepath = filedialog.askopenfilename(filetype = filetype, initialdir = path)