# ==============================================================================
# VOICE LISTING UTILITY MODULE
# ==============================================================================
# System voice enumeration tool for discovering available text-to-speech voices
# Helps administrators configure optimal voice settings for the Hugo assistant
# ==============================================================================

import pyttsx3  # Text-to-speech engine for voice discovery

# ==============================================================================
# VOICE DISCOVERY AND ANALYSIS
# ==============================================================================

# Initialize text-to-speech engine to access system voices
tts = pyttsx3.init()

# Retrieve all available system voices
voices = tts.getProperty('voices')

# ==============================================================================
# VOICE INFORMATION DISPLAY
# ==============================================================================

# Iterate through each available voice and display detailed information
for voice in voices:
    
    print('=======')  # Visual separator between voices

    # Display voice name (human-readable identifier)
    print('Имя: %s' % voice.name)

    # Display voice ID (system identifier for programmatic access)
    print('ID: %s' % voice.id)

    # Display supported languages (language codes and regions)
    print('Язык(и): %s' % voice.languages)

    # Display voice gender (male/female/neutral)
    print('Пол: %s' % voice.gender)

    # Display voice age category (adult/child/elderly)
    print('Возраст: %s' % voice.age)
