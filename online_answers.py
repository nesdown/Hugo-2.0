# ==============================================================================
# ONLINE ANSWERS MODULE
# ==============================================================================
# AI-powered response system using DialogFlow API for intelligent conversation
# Provides natural language processing and context-aware responses
# ==============================================================================

import apiai  # DialogFlow API integration
import json   # JSON data handling for API responses

# DialogFlow API configuration
DIALOGFLOW_API_ID = '6ba32f5bc2d04cdea7c742cf53fc5d26'

# Load language configuration from settings
with open('config.cfg') as json_file:
      data = json.load(json_file)
      lang = data['settings']['speech_language']  # Get configured language
      print("Speech Generation AI Language: " + lang)

def provide_response(phrase):
    """
    Generate intelligent AI response using DialogFlow API
    
    Args:
        phrase (str): User input text to process
        
    Returns:
        str: AI-generated response from DialogFlow
        
    Features:
        - Natural language understanding
        - Context-aware conversations
        - Multi-language support
        - Intent recognition and entity extraction
        - Conversational memory across sessions
        
    API Integration:
        - Uses DialogFlow (Google Cloud AI) for NLP
        - Maintains conversation context with session ID
        - Supports multiple languages based on configuration
        - Handles complex conversational flows
    """
    global lang
    global DIALOGFLOW_API_ID

    # Initialize DialogFlow API client
    request = apiai.ApiAI(DIALOGFLOW_API_ID).text_request()
    
    # Configure request parameters
    request.lang = lang  # Set language from configuration
    request.session_id = 'small-talk-37ef4'  # Maintain conversation context
    request.query = phrase  # Set user input text
    
    # Send request to DialogFlow and parse JSON response
    response_json = json.loads(request.getresponse().read().decode('utf-8'))
    
    # Extract the AI response from the API result
    response = response_json['result']['fulfillment']['speech']

    return response
