# ==============================================================================
# LOGGING MODULE
# ==============================================================================
# Simple logging utility for recording system events and debugging information
# ==============================================================================

from datetime import datetime  # Date and time handling

def log_event(event_description):
    """
    Log an event with timestamp to the work process log file
    
    Args:
        event_description (str): Description of the event to log
        
    Features:
        - Automatic timestamp generation
        - Append-only logging to prevent data loss
        - Simple text format for easy reading
    """
    # Generate current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write event to log file with timestamp
    with open("work_process.log", "a") as log_file:
        log_file.write(f"[{current_time}] {event_description}\n")
