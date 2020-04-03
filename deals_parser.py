import configparser
import requests
import sys

from bs4 import BeautifulSoup
from speech_generation import global_speech

PROMOS_URL = 'https://allo.ua/ru/events-and-discounts/'

def parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    promos = []

    for promo_data in soup.find_all("p", {"class": "short-description"}):
        promos.append(promo_data.text)

    return 'Вот что мне удалось найти. Вариант первый: ' + promos[0] + '. Вариант второй: ' \
           + promos[1] + '. Вариант третий: ' + promos[2] + '. И, наконец, последнее: ' + promos[3] + '.'

def provide_dialog():
  global_speech("Собираю данные об акциях... Подождите пару минут...")
  events_info = parse(PROMOS_URL)
  global_speech(events_info)
  global_speech("На этом вся информация...")
