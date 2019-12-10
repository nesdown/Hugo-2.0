from COMMON_DATA import LOG_FILENAME

ACTIONS = {
  "w": "WRITE COMMAND",
  "r": "READ COMMAND",
  "c": "CHECK"
}

def log(content, action_letter):
  action = ACTIONS[action_letter]

  with open(LOG_FILENAME, "a") as log_file:
    log_file.write(action + ": " + content + "\n")
