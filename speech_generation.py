import get_system
import json
import eel

system_type = get_system.get_system()

with open('config.cfg') as json_file:
      data = json.load(json_file)
      lang = data['settings']['speech_language']
      print("Speech Generation Language: " + lang)

def global_speech(phrase):
  if system_type == "Windows":
    eel.face_2()
    windows_speech(phrase)
    eel.face_1()
  elif system_type == "Linux":
    eel.face_2()
    linux_speech(phrase)
    eel.face_1()
  else:
    print("Error 1#001. Look like you run unknown system.")

def windows_speech(phrase):
  global lang
  import pyttsx3

  tts = pyttsx3.init()

  voices = tts.getProperty('voices')
  tts.setProperty('voice', lang)

  # Попробовать установить предпочтительный голос
  for voice in voices:
      if voice.name == 'Aleksandr':
          tts.setProperty('voice', voice.id)

  tts.say(phrase)
  tts.runAndWait()

def linux_speech(phrase):
  global lang
  import speechd

  tts_d = speechd.SSIPClient('test')

  tts_d.set_output_module('rhvoice')

  tts_d.set_language(lang)

  tts_d.set_rate(50)

  tts_d.set_punctuation(speechd.PunctuationMode.SOME)

  tts_d.speak(phrase)

  tts_d.close()

