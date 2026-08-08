
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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def clicker_cookies():
    #shell.ShellExecuteEx(lpFile=r"D:/documents/ahk/crosshair.ahk")
    #shell.ShellExecuteEx(lpFile=r"D:/Program Files (x86)/Steam/Steam.exe")
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    time.sleep(3)
    # keyboard.type("hello")
    # pynput.keyboard.KeyCode
    mouse.position = (350, 540)
    # mouse.press(Button.left)
    # mouse.release(Button.left)
    mouse.click(Button.left, 20)


def buy_cursor():
    cursorimg = pyautogui.locateCenterOnScreen(os.path.join(SCRIPT_DIR, 'images/cursorimg.png'), confidence=0.9)
    print (cursorimg)
    pyautogui.click(cursorimg)

def gran_click():
    granimg = pyautogui.locateCenterOnScreen(os.path.join(SCRIPT_DIR, 'images/granimg.png'), confidence=0.9)
    print (granimg)
    pyautogui.click(granimg)

if __name__ == '__main__':
    clicker_cookies()
    buy_cursor()
    gran_click()





'''
#shell.ShellExecuteEx(lpVerb='runas', lpFile=r"D:/documents/ahk/0 WARFRAME.ahk")
#shell.ShellExecuteEx(lpVerb='runas', lpFile=r'D:/Program Files (x86)/Steam/steamapps/common/Warframe/Warframe.x64.exe')
#shell.ShellExecuteEx("D:/documents/ahk/0 WARFRAME .ahk")
#shell.ShellExecuteEx('D:/Program Files (x86)/Steam/steamapps/common/Warframe/Warframe.x64.exe')
keyboard.type("Black")
keyboard.press(enter)
keyboard.release(enter)

hello

    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)

    mouse.press(Button.left)
    mouse.release(Button.left)

    cursorimg = pyautogui.locateCenterOnScreen(os.path.join(SCRIPT_DIR, 'images/cursorimg.png'), confidence=0.9)
    print (cursorimg)
    pyautogui.click(cursorimg)

'''
