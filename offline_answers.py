# ==============================================================================
# OFFLINE ANSWERS MODULE
# ==============================================================================
# Offline response system that provides predefined answers from a local JSON
# database without requiring internet connectivity for basic conversations
# ==============================================================================

# -*- coding: utf-8 -*-

import json  # JSON data handling for phrase database

def provide_response(phrase):
    """
    Provide an offline response from the predefined phrases database
    
    Args:
        phrase (str): User input phrase to match against database
        
    Returns:
        str: Corresponding response from the phrases.json database
        
    Features:
        - Works without internet connection
        - Fast response time using local database
        - Case-insensitive phrase matching
        - Comprehensive logging for debugging
        - Fallback system for unknown phrases
        
    Database Structure:
        - phrases.json contains key-value pairs
        - Keys: User input phrases (lowercase)
        - Values: Corresponding AI responses
    """
    # Load predefined phrases and responses from JSON database
    with open('phrases.json', encoding="utf-8") as json_file:
        data = json.load(json_file)

        # Debug output: Display entire phrases dictionary
        print("=============\nDICTIONARY OF ANSWERS:\n")
        print(json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))
        print("=============")

        # Convert input phrase to lowercase for case-insensitive matching
        phrase_process = phrase.lower()
        print("Question to be taken: " + phrase_process)

        # Retrieve corresponding answer from database
        answer = data[phrase_process]

        print("Answer to be provided: " + answer)

        return answer
