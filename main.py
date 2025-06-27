# ==============================================================================
# HUGO 2.0 - AI Personal Assistant
# ==============================================================================
# Main application entry point that initializes the web interface and exposes
# Python functions to JavaScript using the Eel library. This creates a bridge
# between the backend AI functionality and the frontend user interface.
# ==============================================================================

# ==============================================================================
# IMPORTS
# ==============================================================================

# Global libraries
import eel  # Web app framework for Python desktop apps with web technologies

# Local libraries - Core AI functionality modules
import audio_recognition      # Speech-to-text conversion using Google API
import speech_generation     # Text-to-speech synthesis (Windows/Linux compatible)
import offline_answers       # Offline response generation from predefined phrases
import online_answers        # Online AI-powered response generation
import object_analyzis       # Computer vision for object detection and analysis
import friendship            # Face recognition and user database management
import weather_parser        # Weather information retrieval and display
import deals_parser          # Shopping deals aggregation and parsing
import events_parser         # Event information collection and parsing
import dialog_launcher       # Main dialog flow controller

# Standard libraries
import json                  # JSON data handling
from random import *         # Random number generation for varied responses

# ==============================================================================
# APPLICATION INITIALIZATION
# ==============================================================================

# Initialize Eel with the interface directory containing HTML/CSS/JS files
eel.init('interface')

# ==============================================================================
# EXPOSED FUNCTIONS - JavaScript Interface
# ==============================================================================
# These functions are exposed to the frontend JavaScript and can be called
# directly from the web interface to trigger backend functionality

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    """Test function for JavaScript-Python communication"""
    print('Hello from %s' % x)

@eel.expose
def object_analysis_mode():
    """Activate object analysis mode using computer vision"""
    object_analyzis.provide_dialog()

@eel.expose
def deals_parser_mode():
    """Activate shopping deals parsing and display mode"""
    deals_parser.provide_dialog()

@eel.expose
def friendship_mode():
    """Activate friendship mode with face recognition and user registration"""
    friendship.recognition_dialog()

@eel.expose
def weather_mode():
    """Activate weather information retrieval and display mode"""
    weather_parser.provide_dialog()

@eel.expose
def events_mode():
    """Activate events information parsing and display mode"""
    events_parser.provide_dialog()

@eel.expose
def start_speech():
    """
    Main speech processing function with error handling
    Initiates the voice interaction dialog flow
    """
    try:
        dialog_launcher.speech_process()
    except Exception as e:
        # Log error and provide user feedback in case of failure
        print(str(e))
        speech_generation.global_speech("Обратитесь к консультанту, мне чего-то плоховато")

# ==============================================================================
# APPLICATION STARTUP
# ==============================================================================

# Start the Eel application with fullscreen mode and custom window geometry
# Uses loader.html as the initial page with responsive design for 1920x1080
eel.start('loader.html', 
          cmdline_args=['--start-fullscreen', '--browser-startup-dialog'], 
          geometry={'size': (1920, 1080), 'position': (0, 0)})
