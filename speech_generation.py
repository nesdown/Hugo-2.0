# ==============================================================================
# SPEECH GENERATION MODULE
# ==============================================================================
# Cross-platform text-to-speech synthesis module that supports both Windows
# and Linux operating systems with different TTS engines and voice configurations
# ==============================================================================

import get_system  # Custom module to detect operating system
import json        # JSON configuration file handling
import eel         # Web interface communication

# ==============================================================================
# SYSTEM DETECTION AND CONFIGURATION
# ==============================================================================

# Detect the current operating system for platform-specific TTS configuration
system_type = get_system.get_system()

# Load speech configuration from config file
with open('config.cfg') as json_file:
      data = json.load(json_file)
      lang = data['settings']['speech_language']  # Get configured language
      print("Speech Generation Language: " + lang)

# ==============================================================================
# MAIN SPEECH FUNCTION
# ==============================================================================

def global_speech(phrase):
    """
    Universal speech synthesis function that handles cross-platform TTS
    
    Args:
        phrase (str): Text to be converted to speech
        
    Features:
        - Automatically detects OS and uses appropriate TTS engine
        - Updates facial animation in web interface during speech
        - Handles errors gracefully for unsupported systems
    """
    if system_type == "Windows":
        eel.face_2()  # Switch to speaking face animation
        windows_speech(phrase)
        eel.face_1()  # Return to neutral face animation
    elif system_type == "Linux":
        eel.face_2()  # Switch to speaking face animation
        linux_speech(phrase)
        eel.face_1()  # Return to neutral face animation
    else:
        print("Error 1#001. Look like you run unknown system.")

# ==============================================================================
# WINDOWS TEXT-TO-SPEECH IMPLEMENTATION
# ==============================================================================

def windows_speech(phrase):
    """
    Windows-specific TTS implementation using pyttsx3 library
    
    Args:
        phrase (str): Text to synthesize to speech
        
    Features:
        - Uses Windows SAPI voices
        - Attempts to set Russian voice (Aleksandr) if available
        - Configurable language support
    """
    global lang
    import pyttsx3

    # Initialize Windows TTS engine
    tts = pyttsx3.init()

    # Get available system voices
    voices = tts.getProperty('voices')
    tts.setProperty('voice', lang)

    # Try to set preferred Russian voice if available
    for voice in voices:
        if voice.name == 'Aleksandr':
            tts.setProperty('voice', voice.id)

    # Synthesize and play speech
    tts.say(phrase)
    tts.runAndWait()

# ==============================================================================
# LINUX TEXT-TO-SPEECH IMPLEMENTATION
# ==============================================================================

def linux_speech(phrase):
    """
    Linux-specific TTS implementation using Speech Dispatcher
    
    Args:
        phrase (str): Text to synthesize to speech
        
    Features:
        - Uses RHVoice TTS engine for better Russian support
        - Configurable speech rate and punctuation handling
        - Speech Dispatcher integration for system compatibility
    """
    global lang
    import speechd

    # Initialize Speech Dispatcher client
    tts_d = speechd.SSIPClient('test')

    # Configure TTS engine - RHVoice provides better Russian language support
    tts_d.set_output_module('rhvoice')

    # Set language from configuration
    tts_d.set_language(lang)

    # Configure speech parameters
    tts_d.set_rate(50)  # Speech rate (moderate speed)
    tts_d.set_punctuation(speechd.PunctuationMode.SOME)  # Punctuation handling

    # Synthesize speech
    tts_d.speak(phrase)

    # Clean up resources
    tts_d.close()

