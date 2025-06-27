# ==============================================================================
# GUI LAUNCHER MODULE
# ==============================================================================
# Tkinter-based graphical user interface for system initialization and startup
# Provides visual feedback with animated progress bar during system loading
# ==============================================================================

# Importing tkinter GUI framework
from tkinter import *       # Core tkinter components
from tkinter.ttk import *   # Enhanced themed widgets
  
# ==============================================================================
# MAIN APPLICATION WINDOW SETUP
# ==============================================================================

# Create main tkinter application window
root = Tk() 
  
# Initialize progress bar widget with horizontal orientation
# Length: 100 pixels, Mode: indeterminate (continuous animation)
progress = Progressbar(root, orient = HORIZONTAL, 
            length = 100, mode = 'indeterminate') 
  
# ==============================================================================
# PROGRESS BAR ANIMATION FUNCTION
# ==============================================================================

def bar(): 
    """
    Animated progress bar function that simulates system initialization
    
    Features:
        - Visual feedback during system startup
        - Smooth progress animation with timing delays
        - Bidirectional progress movement for dynamic effect
        - User-friendly loading experience
        
    Animation Sequence:
        1. Forward progress: 0% → 100%
        2. Backward progress: 100% → 0%
        3. Timed delays for realistic loading simulation
        4. GUI updates for smooth visual transitions
        
    Technical Details:
        - Uses root.update_idletasks() for GUI responsiveness
        - 0.5 second delays between progress steps
        - Percentage-based progress tracking
    """
    import time  # Time control for animation delays
    
    # Forward progress animation sequence
    progress['value'] = 20   # Set progress to 20%
    root.update_idletasks()  # Update GUI display
    time.sleep(0.5)          # Wait 0.5 seconds
  
    progress['value'] = 40   # Set progress to 40%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 50   # Set progress to 50%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 60   # Set progress to 60%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 80   # Set progress to 80%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 100  # Set progress to 100%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    # Backward progress animation sequence
    progress['value'] = 80   # Decrease to 80%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 60   # Decrease to 60%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 50   # Decrease to 50%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 40   # Decrease to 40%
    root.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 20   # Decrease to 20%
    root.update_idletasks() 
    time.sleep(0.5) 
    
    # Reset progress bar to 0%
    progress['value'] = 0
      
# ==============================================================================
# GUI LAYOUT AND CONTROLS
# ==============================================================================

# Add progress bar to window with padding
progress.pack(pady = 10) 
  
# Create start button that triggers the progress animation
# When clicked, executes the bar() function
Button(root, text = 'Start', command = bar).pack(pady = 10) 
  
# ==============================================================================
# APPLICATION MAIN LOOP
# ==============================================================================

# Start the tkinter event loop - keeps the window responsive
mainloop() 