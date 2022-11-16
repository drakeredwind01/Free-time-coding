import os
import time
import pyautogui

virtualenv -p C:\Users\drakeredwind01\Anaconda3\envs\firstconda





if __name__ == '__main__':


    while 1:
        time.sleep(30)

        candidPic = pyautogui.screenshot()
        i = 1
        while os.path.exists("D:/documents/pic/spy/candidPic%s.png" % i):
            i += 1
        candidPic.save('D:/documents/pic/spy/candidPic%s.png' % i)








"""

'''3600 = hr'''

How to Take and Save a Screenshot in Python
http://www.learningaboutelectronics.com/Articles/Screenshot-in-Python.php

How do I create a incrementing filename in Python?
https://stackoverflow.com/questions/17984809/how-do-i-create-a-incrementing-filename-in-python



"""