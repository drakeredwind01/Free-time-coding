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
mon = (1516, 278, 1910, 1018)  #958, 540
print(mon)
if __name__ == '__main__':
    while 1:

        screen = grab_screen(region=mon)

        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        k = cv2.waitKey(30) & 0xff  # = esc
        if k == 27:
            break

cv2.destroyAllWindows()
