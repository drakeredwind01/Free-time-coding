import cv2
import pyautogui
import datetime
from grabscreen import grab_screen
from ahk import AHK
import numpy as np
from PIL import ImageGrab
import win32api
import time
from pynput.mouse import Button, Controller
mouse = Controller()

# going back to 3 and seeeeing if weeeee can go furtheeree from theeree
# /td
# 2020.01.01.16.38.14.818
# make it work for left side youtube for entertainment
# as fast as possible
# run on 2 different processes so that it will detect when the right mouse is down
# if global RButton down
# DO IT if global down
# [X] move mouse to

# [ ] move center to
# global down exit
# done

face_front_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
#mon = (957, 537, 962, 542)  #958, 540
mon = (1516, 278, 1910, 1018)  #958, 540
print(mon)


def cookieclicker1():
    if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker1.png',
                                 confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker1.png', confidence=0.8)
        print('hit cookieclicker1')
        pyautogui.click(hit)

def cookieclicker2():
    if (pyautogui.locateOnScreen('D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker2.png',
                                 confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker2.png', confidence=0.8)
        print('hit cookieclicker2')
        pyautogui.click(hit)

def cookieclicker3():
    if (pyautogui.locateOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker3.png',
            confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker3.png', confidence=0.8)
        print('hit cookieclicker3')
        pyautogui.click(hit)

def cookieclicker4():
    if (pyautogui.locateOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker4.png',
            confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker4.png', confidence=0.8)
        print('hit cookieclicker4')
        pyautogui.click(hit)

def cookieclicker5():
    if (pyautogui.locateOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker5.png',
            confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker5.png', confidence=0.8)
        print('hit cookieclicker5')
        pyautogui.click(hit)

def cookieclicker6():
    if (pyautogui.locateOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker6.png',
            confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker6.png', confidence=0.8)
        print('hit cookieclicker6')
        pyautogui.click(hit)

def cookieclicker7():
    if (pyautogui.locateOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker7.png',
            confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker7.png', confidence=0.8)
        print('hit cookieclicker7')
        pyautogui.click(hit)

def cookieclicker8():
    if (pyautogui.locateOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker8.png',
            confidence=0.8) is not None):
        hit = pyautogui.locateCenterOnScreen(
            'D:\\documents\\ai\\python\\my-first-conda-project\\pic\\cookieclicker8.png', confidence=0.8)
        print('hit cookieclicker8')
        pyautogui.click(hit)




if __name__ == '__main__':
    while 1:
        screen = grab_screen(region=mon)

        cookieclicker1()
        cookieclicker2()
        cookieclicker3()
        cookieclicker4()
        cookieclicker5()
        cookieclicker6()
        cookieclicker7()
        cookieclicker8()

        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        k = cv2.waitKey(30) & 0xff  # = esc
        if k == 27:
            break

cv2.destroyAllWindows()
