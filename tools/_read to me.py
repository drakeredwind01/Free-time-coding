import time
import os

#voice stuff
conda activate ranenv
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate', 300)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    speak('hello')
    speak('')
    speak('')
    speak('')
    speak('')
    speak('')
    speak('')
    speak('')
