import win32api
import time
from pynput.mouse import Button, Controller
mouse = Controller()

while True:

    if (win32api.GetAsyncKeyState(0x01)&0x8000 > 0):
        flag = True
        checked = 0
        while flag == True:
               checked + 1
               checked = checked + 1
               #mouse.click(Button.left, 1)
               #time.sleep(0.1)
               print("held")
               if (checked == 5):
                   flag = False


