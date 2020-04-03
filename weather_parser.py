import configparser
import requests
import sys

from googletrans import Translator
from speech_generation import global_speech

WEATHER_API_ID = 'f1b7e1da0411e38c604e11a2e6f1d046'
translator = Translator()

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def parse(api_key, location):
    weather = get_weather(api_key, location)

    weather_cond = weather['weather'][0]['main']
    ru_weather_cond = translator.translate(weather_cond, dest='ru').text
    current_temperature = weather['main']['temp']
    feel_temperature = weather['main']['feels_like']
    result = "Погода - " + ru_weather_cond + ". Температура: " + str(current_temperature) + " градусов Цельсия. Чувствуется как: " + str(feel_temperature) + " градусов Цельсия."
    print(result)
    return result

def provide_dialog():
  global_speech("Собираю данные о погодных условиях...")
  weather_info = parse(WEATHER_API_ID, "Kyiv")
  global_speech(weather_info)
