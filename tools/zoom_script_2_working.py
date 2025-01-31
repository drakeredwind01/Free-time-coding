import time
import win32clipboard
import pyautogui
import keyboard  # Use keyboard library for key detection
from pynput.mouse import Listener, Button
'''
works in windows 11
'''



# Function to zoom in (Windows + '+')
def zoom_in():
    pyautogui.keyDown('win')
    pyautogui.press('+')
    pyautogui.keyUp('win')

# Function to zoom out (Windows + '-')
def zoom_out():
    pyautogui.keyDown('win')
    pyautogui.press('-')
    pyautogui.keyUp('win')


def main_loop():
    while True:
        # Check if 'shift+q' is pressed for voice speaking
        if keyboard.is_pressed('shift+q'):
            zoom_in()
        if keyboard.is_pressed('shift+w'):
            time.sleep(0.5)
            zoom_out()
            time.sleep(0.5)
        # if keyboard.is_pressed('xbutton1'):
        #     zoom_out()
        # if keyboard.is_pressed('xbutton2'):
        #     zoom_in()

if __name__ == "__main__":
    main_loop()
