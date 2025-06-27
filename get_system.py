# ==============================================================================
# SYSTEM DETECTION MODULE
# ==============================================================================
# Cross-platform system detection utility for determining the operating system
# Used to select appropriate libraries and configurations for different platforms
# ==============================================================================

import platform  # Standard library for system information

def get_system():
    """
    Detect the current operating system
    
    Returns:
        str: Operating system name ('Windows', 'Linux', or specific system name)
        
    Purpose:
        - Enables cross-platform compatibility for TTS engines
        - Allows selection of OS-specific libraries and configurations
        - Used by speech_generation.py to choose appropriate TTS backend
    """
    system = platform.system() # Вернет тип системы.
    bit = platform.architecture() # Вернет кортеж, где разрядность — нулевой элемент

    print(system)
    print(bit[0])

    return system
