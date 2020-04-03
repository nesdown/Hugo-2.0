# -*- coding: utf-8 -*-

import json

def provide_response(phrase):
  with open('phrases.json', encoding="utf-8") as json_file:
      data = json.load(json_file)

      print("=============\nDICTIONARY OF ANSWERS:\n")
      print(json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))
      print("=============")

      phrase_process = phrase.lower()
      print("Question to be taken: " + phrase_process)

      answer = data[phrase_process]

      print("Answer to be provided: " + answer)

      return answer
