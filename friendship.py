from cv2 import *
import face_recognition
from time import sleep
from shutil import copyfile
import os

from recognize import identify_faces
from speech_generation import global_speech
from audio_recognition import audio_recognition

# ==============================================
# HERE WE TRAIN THE DATABASE. NEEDS REFACTORING.
# ==============================================
known_face_names = []
known_face_encodings = []

def load_known_people():
  global known_face_names
  global known_face_encodings
  known_face_names = list(os.listdir("database"))

  for face_name in known_face_names:
    face_img = face_recognition.load_image_file("database" + "/" + face_name)
    face_enc = face_recognition.face_encodings(face_img)[0]
    known_face_encodings.append(face_enc)

  known_face_names = list(map(lambda x: os.path.splitext(x)[0], known_face_names))

load_known_people()

def take_new_photo(camera_number):
  # initialize the camera
  cam = VideoCapture(camera_number)   # 0 -> index of camera
  s, img = cam.read()
  if s:    # frame captured without any errors
      namedWindow("Here is your photo")
      imshow("Here is your photo", img)
      waitKey(delay=3000)

      destroyWindow("Here is your photo")
      imwrite("temporary.jpg", img) #save image


def recognize_person():
  global known_face_names
  global known_face_encodings

  unknown_image = face_recognition.load_image_file("temporary.jpg")
  unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

  results = face_recognition.compare_faces(known_face_encodings, unknown_encoding)

  if any(results):
    name_index = results.index(True)
    print(known_face_names[name_index])
    return known_face_names[name_index]

  else:
    return "Unknown"


def recognition_dialog():
  global_speech("Я только за! Позволь сфоткаю тебя... Сейчас вылетит птичка!")
  sleep(2)
  take_new_photo(1)
  global_speech("Отличный кадр! Сохраню...")

  friend_name = recognize_person()
  if friend_name == "Unknown":
    global_speech("Я буду искренне рад с тобой подружиться! А как тебя зовут?")
    new_friend_name = audio_recognition()
    global_speech("Приятно познакомиться! Сейчас запишу информацию в блокнотик.")
    copyfile("temporary.jpg", "database")
    os.rename('database/temporary.jpg', 'database/' + new_friend_name + '.jpg')
    os.remove("temporary.jpg")
    global_speech("Готово! Уверен, мы станем отличными друзьями!")

  else:
    global_speech("Узнал тебя! Да мы ведь уже давно дружим! " + friend_name + ", сколько лет, сколько зим!")
    os.remove("temporary.jpg")
