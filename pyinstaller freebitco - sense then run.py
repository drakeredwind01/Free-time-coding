# virtualenv -p C:\Users\drakeredwind01\Anaconda3\envs\firstconda\python.exe
# python "C:\Users\drakeredwind01\Desktop\moonbit.py"


import time
import pyautogui



def freebitcoroll():
    freebitcorollcount = 0
    freebitcoroll = False
    print('running bit thing')
    while freebitcoroll == False:
        if (pyautogui.locateOnScreen('source\\freebitcoroll.png', confidence=0.7) is not None):
            freebitcoroll = False
            hit = pyautogui.locateCenterOnScreen('source\\freebitcoroll.png', confidence=0.7)
            freebitcorollcount + 1
            print('hit freebitcorollcount = %d' % freebitcorollcount)
            pyautogui.click(hit)
            time.sleep(3600)


if __name__ == '__main__':
    freebitcoroll()
