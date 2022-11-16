import os
import pyautogui







if __name__ == '__main__':
    candidPic = pyautogui.screenshot()

    i = 0
    while os.path.exists("D:/documents/pic/spy/candidPic%s.png" % i):
        i += 1

    #fh = open("D:/documents/pic/candidPic%s.png" % i, "w")
    candidPic.save('D:/documents/pic/spy/candidPic%s.png' % i)








"""

'''3600 = hr'''

How to Take and Save a Screenshot in Python
http://www.learningaboutelectronics.com/Articles/Screenshot-in-Python.php

How do I create a incrementing filename in Python?
https://stackoverflow.com/questions/17984809/how-do-i-create-a-incrementing-filename-in-python



"""