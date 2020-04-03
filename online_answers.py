import apiai
import json

DIALOGFLOW_API_ID = '6ba32f5bc2d04cdea7c742cf53fc5d26'

with open('config.cfg') as json_file:
      data = json.load(json_file)
      lang = data['settings']['speech_language']
      print("Speech Generation AI Language: " + lang)

def provide_response(phrase):
    global lang
    global DIALOGFLOW_API_ID

    request = apiai.ApiAI(DIALOGFLOW_API_ID).text_request()
    request.lang = lang
    request.session_id = 'small-talk-37ef4'
    request.query = phrase
    response_json = json.loads(request.getresponse().read().decode('utf-8'))
    response = response_json['result']['fulfillment']['speech']

    return response
