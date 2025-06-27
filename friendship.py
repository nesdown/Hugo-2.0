# ==============================================================================
# FRIENDSHIP MODULE - Face Recognition & User Database
# ==============================================================================
# Advanced friendship system that uses computer vision for face recognition,
# maintains a user database, and provides personalized interactions with known users
# ==============================================================================

from cv2 import *                      # OpenCV for camera operations
import face_recognition                # Face recognition and encoding
from time import sleep                 # Timing controls
from shutil import copyfile           # File operations
import os                             # Operating system interface

# Local modules
from recognize import identify_faces   # Custom face identification functions
from speech_generation import global_speech  # Text-to-speech output
from audio_recognition import audio_recognition  # Speech-to-text input

# ==============================================================================
# FACE RECOGNITION DATABASE SYSTEM
# ==============================================================================
# Global variables for storing known faces and their encodings
# TODO: This system needs refactoring to use a proper database structure

known_face_names = []      # List of known user names
known_face_encodings = []  # List of face encodings for comparison

def load_known_people():
    """
    Load all known faces from the database directory
    
    Features:
        - Scans 'database' directory for face images
        - Generates face encodings for each known person
        - Populates global arrays for face comparison
        
    Database Structure:
        - Each person has one image file in /database/
        - Filename (without extension) becomes the person's name
        - Supports standard image formats (jpg, png, etc.)
    """
    global known_face_names
    global known_face_encodings
    
    # Get list of all files in database directory
    known_face_names = list(os.listdir("database"))

    # Generate face encodings for each known person
    for face_name in known_face_names:
        # Load image file from database
        face_img = face_recognition.load_image_file("database" + "/" + face_name)
        # Generate 128-dimensional face encoding
        face_enc = face_recognition.face_encodings(face_img)[0]
        known_face_encodings.append(face_enc)

    # Remove file extensions from names (e.g., "john.jpg" becomes "john")
    known_face_names = list(map(lambda x: os.path.splitext(x)[0], known_face_names))

# Initialize known faces database on module import
load_known_people()

# ==============================================================================
# CAMERA AND PHOTO CAPTURE SYSTEM
# ==============================================================================

def take_new_photo(camera_number):
    """
    Capture a photo using the specified camera
    
    Args:
        camera_number (int): Camera index (0 for default camera, 1 for external)
        
    Features:
        - Captures single frame from camera
        - Shows preview to user for 3 seconds
        - Saves temporary image for face recognition processing
        - Handles camera initialization and cleanup
    """
    # Initialize camera (0 = default system camera, 1 = external camera)
    cam = VideoCapture(camera_number)
    s, img = cam.read()  # Capture single frame
    
    if s:  # Check if frame was captured successfully
        # Display photo preview to user
        namedWindow("Here is your photo")
        imshow("Here is your photo", img)
        waitKey(delay=3000)  # Show for 3 seconds

        # Clean up display window
        destroyWindow("Here is your photo")
        # Save temporary image for processing
        imwrite("temporary.jpg", img)

# ==============================================================================
# FACE RECOGNITION AND IDENTIFICATION
# ==============================================================================

def recognize_person():
    """
    Identify a person from the temporary photo using face recognition
    
    Returns:
        str: Name of recognized person or "Unknown" if not in database
        
    Process:
        1. Load temporary photo captured by camera
        2. Generate face encoding from the photo
        3. Compare against all known face encodings
        4. Return name if match found, "Unknown" otherwise
        
    Uses face_recognition library's 128-dimensional face encoding system
    with tolerance-based comparison for reliable identification
    """
    global known_face_names
    global known_face_encodings

    # Load the unknown person's photo
    unknown_image = face_recognition.load_image_file("temporary.jpg")
    # Generate face encoding for comparison
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Compare against all known faces in database
    results = face_recognition.compare_faces(known_face_encodings, unknown_encoding)

    # Check if any matches were found
    if any(results):
        # Find index of the matching face
        name_index = results.index(True)
        print(known_face_names[name_index])
        return known_face_names[name_index]
    else:
        return "Unknown"

# ==============================================================================
# MAIN FRIENDSHIP DIALOG SYSTEM
# ==============================================================================

def recognition_dialog():
    """
    Main friendship interaction flow combining speech, camera, and face recognition
    
    Features:
        - Interactive voice communication
        - Automatic photo capture with user notification
        - Face recognition against known users database
        - New user registration with voice input
        - Personalized greetings for returning users
        
    Workflow:
        1. Request permission and take photo
        2. Attempt to recognize the person
        3a. If known: Welcome back with personalized greeting
        3b. If unknown: Register new friend with voice name input
    """
    # Initiate photo capture with friendly interaction
    global_speech("Я только за! Позволь сфоткаю тебя... Сейчас вылетит птичка!")
    sleep(2)  # Give user time to prepare
    
    # Capture photo using external camera (camera index 1)
    take_new_photo(1)
    global_speech("Отличный кадр! Сохраню...")

    # Attempt face recognition
    friend_name = recognize_person()
    
    if friend_name == "Unknown":
        # NEW USER REGISTRATION FLOW
        global_speech("Я буду искренне рад с тобой подружиться! А как тебя зовут?")
        
        # Get user's name via voice input
        new_friend_name = audio_recognition()
        global_speech("Приятно познакомиться! Сейчас запишу информацию в блокнотик.")
        
        # Save user's photo to database with their name
        copyfile("temporary.jpg", "database")
        os.rename('database/temporary.jpg', 'database/' + new_friend_name + '.jpg')
        
        # Clean up temporary file
        os.remove("temporary.jpg")
        global_speech("Готово! Уверен, мы станем отличными друзьями!")

    else:
        # RETURNING USER GREETING FLOW
        global_speech("Узнал тебя! Да мы ведь уже давно дружим! " + friend_name + ", сколько лет, сколько зим!")
        
        # Clean up temporary file
        os.remove("temporary.jpg")
