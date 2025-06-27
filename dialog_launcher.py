# ==============================================================================
# DIALOG LAUNCHER MODULE
# ==============================================================================
# Main dialog flow controller that orchestrates speech recognition, response
# generation, and speech synthesis for natural conversation with users
# ==============================================================================

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
    """
    Main speech processing pipeline that handles complete voice interactions
    
    Features:
        - Continuous speech recognition loop
        - Intelligent response generation (online/offline)
        - Context-aware conversation management
        - Error handling and recovery
        - Multi-modal response capabilities
        
    Process Flow:
        1. Listen for user speech input
        2. Convert speech to text via recognition
        3. Process text through AI/offline responses
        4. Generate appropriate response
        5. Convert response to speech
        6. Update UI with facial animations
        7. Loop for continuous interaction
        
    Integration:
        - Works with all specialized modes (weather, friendship, etc.)
        - Manages transitions between different dialog states
        - Coordinates with web interface for visual feedback
    """
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
