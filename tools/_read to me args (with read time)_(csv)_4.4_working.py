import time
import win32clipboard
import pyautogui
import keyboard  # Use keyboard library for key detection

# Voice stuff (optional)
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(f"{len(voices)=}")
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 600)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def print_simple():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    # engine.setProperty('voice', voices[0].id)
    # speak(data)
    engine.setProperty('voice', voices[1].id)
    speak(data)

def main_loop():
    while True:
        # Check if 'q' is pressed
        if keyboard.is_pressed('shift+q'):
            time.sleep(0.5)
            keyboard.press('ctrl+c')
            keyboard.release('c')
            keyboard.release('ctrl')
            keyboard.release('c')
            keyboard.release('ctrl')
            print_simple()
            # Add a small delay to avoid multiple triggers from a single press
            time.sleep(0.5)
        if keyboard.is_pressed('shift+w'):
            time.sleep(0.5)
            pyautogui.press('backspace')
            pyautogui.typewrite("(have isabella and emily speak) ")
            # Add a small delay to avoid multiple triggers from a single press
            time.sleep(0.5)

if __name__ == "__main__":
    main_loop()
