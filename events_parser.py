# ==============================================================================
# EVENTS PARSER MODULE
# ==============================================================================
# Web scraping system for real-time event information collection and parsing
# Provides automated event discovery and voice-activated event announcements
# ==============================================================================

import configparser            # Configuration file handling
import requests               # HTTP requests for web scraping
import sys                    # System utilities

from bs4 import BeautifulSoup  # HTML parsing and web scraping
from speech_generation import global_speech  # Text-to-speech output

# ==============================================================================
# CONFIGURATION AND CONSTANTS
# ==============================================================================

# Target website URL for event information scraping
PROMOS_URL = 'https://life.bodo.ua/afisha'

# ==============================================================================
# WEB SCRAPING AND PARSING FUNCTIONS
# ==============================================================================

def parse(url):
    """
    Parse events from the specified website URL
    
    Args:
        url (str): Target website URL for event scraping
        
    Returns:
        str: Formatted string containing discovered events
        
    Features:
        - Real-time web scraping of event information
        - HTML parsing with BeautifulSoup
        - Event title extraction and formatting
        - Error handling for web requests
        - Natural language event descriptions
        
    Scraping Process:
        1. Send HTTP GET request to target URL
        2. Parse HTML response with BeautifulSoup
        3. Extract event information from specific HTML elements
        4. Format events into natural language description
        5. Return formatted event string for speech synthesis
    """
    # Send HTTP request to the events website
    response = requests.get(url)
    
    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Initialize list to store discovered events
    events = []

    # Scrape events from HTML div elements with "caption" class
    for div in soup.find_all("div", {"class": "caption"}):
        # Extract event title from nested anchor and h3 tags
        current_event = div.find('a').find('h3')

        # Add event title to list if found
        if current_event is not None:
            events.append(current_event.text)

    # Format events into natural language response
    # Select first 4 events for manageable speech output
    return 'Вот мероприятия, которые в ближайшие дни будут в городе: ' + \
           events[0] + '. ' + events[1] + '. ' + events[2] + '. ' + events[3] + '.'

# ==============================================================================
# MAIN DIALOG INTERFACE
# ==============================================================================

def provide_dialog():
    """
    Main events dialog function that handles voice interaction
    
    Features:
        - Voice-activated event information retrieval
        - Real-time web scraping and parsing
        - Text-to-speech event announcements
        - User-friendly conversation flow
        
    Workflow:
        1. Announce event information gathering
        2. Scrape and parse events from website
        3. Deliver event information via speech synthesis
        4. Conclude with closing message
    """
    # Announce start of event information gathering
    global_speech("Собираю данные о мероприятиях... Подождите пару секунд...")
    
    # Scrape and parse events from the configured URL
    events_info = parse(PROMOS_URL)
    
    # Deliver event information via text-to-speech
    global_speech(events_info)
    
    # Conclude with closing message
    global_speech("На этом вся информация...")

