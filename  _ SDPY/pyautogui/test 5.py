
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

if __name__ == '__main__':


    #shell.ShellExecuteEx(lpFile=r"D:/documents/ahk/crosshair.ahk")
    #shell.ShellExecuteEx(lpFile=r"D:/Program Files (x86)/Steam/Steam.exe")
    time.sleep(5)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    keyboard.type("hello")
    # pynput.keyboard.KeyCode
    mouse.position = (960, 540)
    mouse.press(Button.left)
    mouse.release(Button.left)





'''
#shell.ShellExecuteEx(lpVerb='runas', lpFile=r"D:/documents/ahk/0 WARFRAME.ahk")
#shell.ShellExecuteEx(lpVerb='runas', lpFile=r'D:/Program Files (x86)/Steam/steamapps/common/Warframe/Warframe.x64.exe')
#shell.ShellExecuteEx("D:/documents/ahk/0 WARFRAME .ahk")
#shell.ShellExecuteEx('D:/Program Files (x86)/Steam/steamapps/common/Warframe/Warframe.x64.exe')
keyboard.type("Black")
keyboard.press(enter)
keyboard.release(enter)

hello



'''
