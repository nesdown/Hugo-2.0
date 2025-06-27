#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cv2 import *
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from googletrans import Translator

import collections
from time import sleep

from speech_generation import global_speech

translator = Translator()

# ==============================================================================
# OBJECT ANALYSIS MODULE
# ==============================================================================
# Computer vision system for real-time object detection and analysis
# Uses camera input to identify and describe objects in the environment
# ==============================================================================

def take_photo(camera_number):
  # initialize the camera
  cam = VideoCapture(camera_number)   # 0 -> index of camera
  s, img = cam.read()
  if s:    # frame captured without any errors
      namedWindow("Here is your photo")
      imshow("Here is your photo", img)
      waitKey(delay=3000)

      destroyWindow("Here is your photo")
      imwrite("temporary.jpg", img) #save image

def recognize_objects(image_name):
    im = cv2.imread(image_name)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)

    return label
    # plt.imshow(output_image)
    # plt.show()

def generate_results(label):
  global translator
  my_dict = {i:label.count(i) for i in label}
  result = "Анализ завершен. Я увидел: "

  for key, value in my_dict.items():
    object_name = translator.translate(key, dest='ru').text
    result = result + object_name + ". Количество: " + str(value) + ". "

  return result


def provide_dialog():
    """
    Main object analysis dialog function combining computer vision and speech
    
    Features:
        - Real-time camera-based object detection
        - AI-powered object identification and classification
        - Natural language description of detected objects
        - Voice interaction for analysis requests
        
    Workflow:
        1. Capture image from camera
        2. Process image through object detection models
        3. Identify and classify detected objects
        4. Generate descriptive text about the scene
        5. Deliver analysis via text-to-speech synthesis
        
    Technologies:
        - OpenCV for image processing
        - Computer vision models for object detection
        - Natural language generation for descriptions
    """
    global_speech("Приступаю к анализу окружающей обстановки через 3...")
    sleep(1)
    global_speech("два...")
    sleep(1)
    global_speech("один...")
    take_photo(1)
    global_speech("Анализирую фотографию...")

    data = recognize_objects("temporary.jpg")
    result = generate_results(data)

    global_speech(result)
    os.remove("temporary.jpg")
