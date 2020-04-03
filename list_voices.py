import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')
for voice in voices:

    print('=======')

    print('Имя: %s' % voice.name)

    print('ID: %s' % voice.id)

    print('Язык(и): %s' % voice.languages)

    print('Пол: %s' % voice.gender)

    print('Возраст: %s' % voice.age)
