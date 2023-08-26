import time
import os
import webbrowser
import pyautogui
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

#voice stuff
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
speak('speach online')



# COUNT DOWN (warning)
speak('staring in 3')
speak('2')
speak('1')


# enter info and hit enter
webbrowser.open('https://mycourses.tesu.edu/login/index.php')
time.sleep(2)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("brandon.thompson2")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("Iribribr8")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)

#cos111
webbrowser.open('https://mycourses.tesu.edu/')
time.sleep(.1)

#cos111
webbrowser.open('https://mycourses.tesu.edu/course/view.php?id=48315')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2537166')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2537167')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2537168')
time.sleep(.1)

#cos213
webbrowser.open('https://mycourses.tesu.edu/course/view.php?id=48321')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2537453')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2537454')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2537455')
time.sleep(.1)

#cos270
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/course/view.php?id=48523')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2549900')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2549901')
time.sleep(.1)
webbrowser.open('https://mycourses.tesu.edu/mod/forum/view.php?id=2549902')



speak('Seras will opening extra resources')
webbrowser.open('https://www.chegg.com/study/qa')

# bartleby sign in
webbrowser.open('https://www.bartleby.com/login?referrer=%2Fquestions-and-answers%2F26.-estimate-the-error-in-using-the-indicated-partial-sum-to-approximate-the-sum-of-the-series.-sigm%2Fe8c4bd3d-3f8f-43e8-ba40-45438439e143')
time.sleep(3)
for x in range(11): # 1-11 = 10
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
keyboard.type('cyber_station@hotmail.com')
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type('Iribrib$8')
keyboard.press(Key.enter)
keyboard.release(Key.enter)




webbrowser.open('https://services.smarthinking.com/student/services/')
