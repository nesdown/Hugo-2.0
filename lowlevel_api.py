# ==============================================================================
# LOW-LEVEL API MODULE
# ==============================================================================
# Hardware abstraction layer for motor control and robotic movement commands
# Provides API command generation and logging for physical robot interactions
# ==============================================================================

from datetime import datetime   # Timestamp generation for commands

from logger import log          # Logging system for command tracking
from COMMON_DATA import API_FILENAME  # Shared constants for file paths

# ==============================================================================
# CONSTANTS AND CONFIGURATION
# ==============================================================================

LINE = "--"  # Command separator (currently unused)

# ==============================================================================
# MOTOR CONTROL FUNCTIONS
# ==============================================================================

def start_motors(processing, timing, avg_speed):
    """
    Generate START command for motor control system
    
    Args:
        processing (int): Processing mode identifier
        timing (int): Timing parameter for motor operation
        avg_speed (int): Average speed setting for motors
        
    Features:
        - Generates timestamped motor start commands
        - Writes commands to API file for hardware processing
        - Comprehensive logging for debugging and audit
        - Parameterized motor control for flexible operation
        
    Command Format:
        START:P[processing]:T[timing]:A[avg_speed]:D[timestamp]
        
    Use Cases:
        - Robot movement initiation
        - Motor system activation
        - Hardware interface communication
    """
    # Write motor start command to API file
    with open(API_FILENAME, 'a') as f:
        # Generate current timestamp for command tracking
        current_time = datetime.now().strftime("%H-%M-%S/%d-%m-%Y")
        
        # Format command with parameters and timestamp
        command_content = "START:P" + str(processing) + ":T" + str(timing) + ":A" + str(avg_speed) + ":D" + current_time + "\n"

        # Write command to API file for hardware processing
        f.write(command_content)

    # Log command generation for debugging and audit trail
    log("START MOTORS SENT", "w")

def stop_motors(processing, timing):
    """
    Generate STOP command for motor control system
    
    Args:
        processing (int): Processing mode identifier
        timing (int): Timing parameter for motor operation
        
    Features:
        - Generates timestamped motor stop commands
        - Emergency stop capability for safety
        - Command logging for system monitoring
        - Hardware-agnostic command interface
        
    Command Format:
        STOP:P[processing]:T[timing]:D[timestamp]
        
    Use Cases:
        - Robot movement termination
        - Emergency stop procedures
        - Motor system deactivation
        - Safety shutdowns
    """
    # Write motor stop command to API file
    with open(API_FILENAME, 'a') as f:
        # Generate current timestamp for command tracking
        current_time = datetime.now().strftime("%H-%M-%S/%d-%m-%Y")
        
        # Format stop command with parameters and timestamp
        command_content = "STOP:P" + str(processing) + ":T" + str(timing) + ":D" + current_time + "\n"

        # Write command to API file for hardware processing
        f.write(command_content)

    # Log command generation for debugging and audit trail
    log("STOP MOTORS SENT", "w")
