import pyautogui
import cv2

while 1:

    im1 = pyautogui.screenshot()
    cv2.imshow('window', cv2.cvtColor(im1, cv2.COLOR_BGR2RGB ))







