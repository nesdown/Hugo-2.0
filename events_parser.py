import configparser
import requests
import sys

from bs4 import BeautifulSoup
from speech_generation import global_speech

PROMOS_URL = 'https://life.bodo.ua/afisha'

def parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    events = []

    for div in soup.find_all("div", {"class": "caption"}):
        current_event = div.find('a').find('h3')

        if current_event is not None:
            events.append(current_event.text)

    return 'Вот мероприятия, которые в ближайшие дни будут в городе: ' + \
           events[0] + '. ' + events[1] + '. ' + events[2] + '. ' + events[3] + '.'

def provide_dialog():
  global_speech("Собираю данные о мероприятиях... Подождите пару секунд...")
  events_info = parse(PROMOS_URL)
  global_speech(events_info)
  global_speech("На этом вся информация...")

