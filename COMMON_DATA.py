# ==============================================================================
# COMMON DATA MODULE
# ==============================================================================
# Centralized configuration and constants for the Hugo 2.0 AI Assistant
# Provides shared file paths and system-wide configuration values
# ==============================================================================

# ==============================================================================
# FILE SYSTEM CONSTANTS
# ==============================================================================

# API Commands File - Storage for hardware control commands
# Used by lowlevel_api.py for motor control and robotic movement commands
# Format: Text file with timestamped command strings
API_FILENAME = "api_commands.api"

# Work Process Log File - System activity and event logging
# Used by logger.py for debugging, monitoring, and audit trails
# Format: Text file with timestamped log entries
LOG_FILENAME = "work_process.log"

# ==============================================================================
# USAGE NOTES
# ==============================================================================
# This module serves as a centralized configuration point for file paths
# and system constants. By defining these values here, the Hugo system
# maintains consistency across all modules and allows for easy configuration
# changes without modifying multiple files.
#
# Files managed by these constants:
# - api_commands.api: Hardware control command queue
# - work_process.log: System activity log and debugging information
# ==============================================================================
