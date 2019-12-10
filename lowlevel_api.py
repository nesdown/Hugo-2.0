from datetime import datetime

from logger import log
from COMMON_DATA import API_FILENAME

LINE = "--"

def start_motors(processing, timing, avg_speed):
  with open(API_FILENAME, 'a') as f:
    current_time = datetime.now().strftime("%H-%M-%S/%d-%m-%Y")
    command_content = "START:P" + str(processing) + ":T" + str(timing) + ":A" + str(avg_speed) + ":D" + current_time + "\n"

    f.write(command_content)


  log("START MOTORS SENT", "w")


def stop_motors(processing, timing):
  with open(API_FILENAME, 'a') as f:
    current_time = datetime.now().strftime("%H-%M-%S/%d-%m-%Y")
    command_content = "STOP:P" + str(processing) + ":T" + str(timing) + ":D" + current_time + "\n"

    f.write(command_content)


  log("STOP MOTORS SENT", "w")
