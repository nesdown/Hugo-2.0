# global libraries
import eel

# local libraries
import audio_recognition
import speech_generation
import offline_answers
import online_answers
import object_analyzis
import friendship
import weather_parser
import deals_parser
import events_parser
import dialog_launcher

import json
from random import *

eel.init('interface')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

@eel.expose
def object_analysis_mode():
  object_analyzis.provide_dialog()

@eel.expose
def deals_parser_mode():
  deals_parser.provide_dialog()

@eel.expose
def friendship_mode():
  friendship.recognition_dialog()

@eel.expose
def weather_mode():
  weather_parser.provide_dialog()

@eel.expose
def events_mode():
  events_parser.provide_dialog()

@eel.expose
# def start_speech():
#   dialog_launcher.speech_process()
def start_speech():
  try:
    dialog_launcher.speech_process()
  except Exception as e:
    print(str(e))
    speech_generation.global_speech("Обратитесь к консультанту, мне чего-то плоховато")

eel.start('launcher.html', cmdline_args=['--start-fullscreen', '--browser-startup-dialog'], geometry={'size': (1920, 1080), 'position': (0, 0)})
