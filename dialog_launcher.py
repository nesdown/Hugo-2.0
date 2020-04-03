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

from random import *
import json

online_mode = False

with open('config.cfg') as json_file:
      data = json.load(json_file)
      online_mode = data['settings']['online_mode']
      print("Online Mode: " + online_mode)
      online_mode = bool(online_mode)

def speech_process():
  global online_mode
  phrases = ["Я слушаю!", "Да-да?", "Я тута!", "Чем могу быть полезен?", "К вашим услугам!"]

  speech_generation.global_speech(choice(phrases))
  question = audio_recognition.audio_recognition()

  if "анализ" in question:
    object_analyzis.provide_dialog()
  elif "дружить" in question:
    friendship.recognition_dialog()
  elif "погода" in question:
    weather_parser.provide_dialog()
  elif "события" in question:
    events_parser.provide_dialog()
  elif "скидки" in question:
    deals_parser.provide_dialog()
  else:
    if online_mode:
      response = online_answers.provide_response(question)
      speech_generation.global_speech(response)
    else:
      response = offline_answers.provide_response(question)
      speech_generation.global_speech(response)
