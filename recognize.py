# ==============================================================================
# FACE RECOGNITION UTILITIES MODULE
# ==============================================================================
# Advanced face recognition utilities for real-time face identification
# Provides optimized algorithms for face matching and distance calculation
# ==============================================================================

import face_recognition  # Face recognition and encoding library
import numpy as np       # Numerical computations for face distance calculations

def identify_faces(small_frame, known_face_names, known_face_encodings):
    """
    Identify faces in a video frame using advanced face recognition algorithms
    
    Args:
        small_frame: Processed video frame (BGR format from OpenCV)
        known_face_names (list): List of known person names
        known_face_encodings (list): List of corresponding face encodings
        
    Returns:
        tuple: (face_locations, face_names) containing detected face positions and identities
        
    Features:
        - Real-time face detection in video streams
        - Multiple face recognition in single frame
        - Distance-based face matching for accuracy
        - Optimized for performance with small frames
        - Handles unknown faces gracefully
        
    Algorithm:
        1. Convert BGR to RGB color space for face_recognition library
        2. Detect all face locations in the frame
        3. Generate face encodings for detected faces
        4. Compare encodings against known faces database
        5. Calculate face distances for best match selection
        6. Return face locations and corresponding names
    """
    # Convert BGR (OpenCV) to RGB (face_recognition library format)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Detect all faces and generate encodings in current video frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Initialize list to store identified face names
    face_names = []
    
    # Process each detected face
    for face_encoding in face_encodings:
        # Compare current face against all known faces in database
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # Calculate distances to find the best match (smaller distance = better match)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        # Default to "Unknown" if no good match is found
        name = "Unknown"
        
        # If any matches found, select the one with smallest distance
        if face_distances.any():
            best_match_index = np.argmin(face_distances)  # Find index of minimum distance
            if matches[best_match_index]:  # Verify the match meets threshold
                name = known_face_names[best_match_index]

        # Add identified name to results
        face_names.append(name)

    return face_locations, face_names
