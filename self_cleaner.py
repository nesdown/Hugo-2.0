# ==============================================================================
# SELF CLEANER MODULE
# ==============================================================================
# Automated file maintenance system that cleans up API command files based on
# date stamps to prevent accumulation of outdated commands and maintain system performance
# ==============================================================================

from COMMON_DATA import API_FILENAME  # Shared filename constants
import os, time, datetime, logger      # System and logging utilities

def check_api_commands():
    """
    Check API commands file modification date and clean if outdated
    
    Features:
        - Automatic file cleanup based on modification date
        - Prevents accumulation of old API commands
        - Maintains system performance and storage efficiency
        - Comprehensive logging of cleanup operations
        
    Process:
        1. Get file modification timestamp
        2. Compare with current date
        3. Clear file if not modified today
        4. Log cleanup action for audit trail
        
    File Management:
        - Monitors api_commands.api file
        - Clears outdated commands automatically
        - Preserves system resources
    """
    # Get file modification time in human-readable format
    time_modified = time.ctime(os.path.getmtime(API_FILENAME))
    # print("last modified: %s" % time_modified)

    # Parse modification time string into components
    time_array = time_modified.split(" ")
    # print(time_array[1] + " " + time_array[2] + " " + time_array[4])
    
    # Extract date components: Month Day Year
    file_time_stamp = time_array[1] + " " + time_array[2] + " " + time_array[4]

    # Get current date in same format for comparison
    current_time_stamp = datetime.datetime.now().strftime("%b %d %Y")
    #print(current_time_stamp)

    # Compare file date with current date
    if (current_time_stamp != file_time_stamp):
        # File is from previous day(s) - clear it
        open(API_FILENAME, "w").close()  # Truncate file to empty
        logger.log("ERASED", "c")  # Log cleanup action
    else:
        # File is current - no cleanup needed
        logger.log("NOT ERASED", "c")  # Log no-action status
