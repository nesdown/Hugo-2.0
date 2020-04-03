import json
import speech_recognition as sr
r = sr.Recognizer()

with open('config.cfg') as json_file:
      data = json.load(json_file)
      lang = data['settings']['recognition_language']
      print("Speech Recognition Language: " + lang)

def audio_recognition():
    global lang

    with sr.Microphone() as source:
       print("Waiting for voice input...")
       audio = r.listen(source)

       # recognition via Google ONLINE
       result = r.recognize_google(audio, language=lang)

       # recognition via Sphinx OFFLINE
       #result = r.recognize_sphinx(audio, lang)

       # recognition via WitAI ONLINE - NOT RECOMMENDED!
       # result = r.recognize_wit(audio, key="K6Z4HOUNB72P4RAL5CYOAMB23DOMYI2C", show_all=True)

       print(result)
       return result
