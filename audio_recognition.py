# ==============================================================================
# AUDIO RECOGNITION MODULE
# ==============================================================================
# Speech-to-text conversion module using Google's speech recognition API
# Supports multiple recognition engines with configurable language settings
# ==============================================================================

import json                    # Configuration file handling
import speech_recognition as sr # Speech recognition library

# ==============================================================================
# INITIALIZATION AND CONFIGURATION
# ==============================================================================

# Initialize speech recognition engine
r = sr.Recognizer()

# Load speech recognition configuration from config file
with open('config.cfg') as json_file:
      data = json.load(json_file)
      lang = data['settings']['recognition_language']  # Get configured language (e.g., 'ru-RU')
      print("Speech Recognition Language: " + lang)

# ==============================================================================
# MAIN AUDIO RECOGNITION FUNCTION
# ==============================================================================

def audio_recognition():
    """
    Convert speech from microphone input to text using Google's API
    
    Returns:
        str: Transcribed text from speech input
        
    Features:
        - Uses system default microphone
        - Configurable language support (set in config.cfg)
        - Multiple recognition engine options (Google, Sphinx, Wit.AI)
        - Real-time audio processing with automatic silence detection
        
    Recognition Engines Available:
        - Google (Online): High accuracy, requires internet connection
        - Sphinx (Offline): Lower accuracy, works without internet
        - Wit.AI (Online): Alternative online service (not recommended)
    """
    global lang

    # Use system default microphone as audio source
    with sr.Microphone() as source:
       print("Waiting for voice input...")
       # Listen for audio input with automatic silence detection
       audio = r.listen(source)

       # PRIMARY: Google Speech Recognition (Online) - High accuracy
       result = r.recognize_google(audio, language=lang)

       # ALTERNATIVE: Sphinx Speech Recognition (Offline) - Lower accuracy
       # Uncomment the line below to use offline recognition
       #result = r.recognize_sphinx(audio, lang)

       # ALTERNATIVE: Wit.AI Speech Recognition (Online) - Not recommended
       # Requires API key and has limitations
       # result = r.recognize_wit(audio, key="K6Z4HOUNB72P4RAL5CYOAMB23DOMYI2C", show_all=True)

       # Output recognized text and return result
       print(result)
       return result
