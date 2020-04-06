import eel
eel.init('interface')

from playsound import playsound
from time import sleep
from random import randint

@eel.expose 
def play_sound():
    for i in range(10):
        eel.face_2()
        playsound(str(i+1) + ".wav")
        eel.face_1()
        sleep(randint (3, 5))

eel.start('main.html', cmdline_args=['--start-fullscreen', '--browser-startup-dialog'], geometry={'size': (1920, 1080), 'position': (0, 0)})
