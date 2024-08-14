import os
import speech_recognition as sr


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        query = 'None'

    return query


while True:

    wake_up = takecommand()

    if 'hey March' or 'March' in wake_up:
        os.startfile('F:\\March\\March.py')

    else:
        print("Nothing...")