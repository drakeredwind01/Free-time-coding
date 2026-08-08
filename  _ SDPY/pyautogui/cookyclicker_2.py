import time
import pyautogui
import pynput
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()


import os
import sys
# import win32com.shell.shell as shell


def clicker_cookies():
    #shell.ShellExecuteEx(lpFile=r"D:/documents/ahk/crosshair.ahk")
    #shell.ShellExecuteEx(lpFile=r"D:/Program Files (x86)/Steam/Steam.exe")
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    time.sleep(3)
    keyboard.type("hello")
    # pynput.keyboard.KeyCode
    mouse.position = (340, 5460)
    # mouse.press(Button.left)
    # mouse.release(Button.left)
    mouse.click(Button.left, 10)


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def buy_cursor():
    cursorimg = pyautogui.locateCenterOnScreen(os.path.join(SCRIPT_DIR, 'images/cursorimg.png'), confidence=0.9)
    print (cursorimg)
    pyautogui.click(cursorimg)

def gran_click():
    cursorimg = pyautogui.locateCenterOnScreen(os.path.join(SCRIPT_DIR, 'images/granimg.png'), confidence=0.9)
    print (cursorimg)
    pyautogui.click(cursorimg)




if __name__ == '__main__':
    clicker_cookies()
    buy_cursor()
    gran_click()
