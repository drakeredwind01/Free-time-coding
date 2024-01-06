
#virtualenv -p C:\Users\drakeredwind01\Anaconda3\envs\firstconda


'''
https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
How to import a module given the full path?

import tkinter as tk
from importlib.machinery import SourceFileLoader
foo = SourceFileLoader("btc_2.0.py", "C:\\Users\\drakeredwind01\\Desktop\\btc_2.0.py").load_module()
foo.bitfun()

'''





'''
#for screen capture
import numpy as np
from PIL import ImageGrab
import cv2

while(True):
    printscreen_pil =  ImageGrab.grab()
    printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
    cv2.imshow('window',printscreen_numpy)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

https://pyautogui.readthedocs.io/en/latest/cheatsheet.html
import pyautogui
pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
'''





'''
#if found, used in bloons-moneyky-city
D:\\documents\\ai\\python\\my-first-conda-project\\Bloons-Monkey-City\\

if (pyautogui.locateOnScreen('zzzselenium.py.PNG') is not None):
    pyautogui.hotkey('win', 'l')

    claimnow = pyautogui.locateCenterOnScreen('C:\\Users\\drakeredwind01\\Desktop\\BTC sources\\bitfun claim now.png', confidence=0.8)
    pyautogui.click(claimnow)

'''




'''

https://www.python-course.eu/tkinter_entry_widgets.php


import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()

'''


'''
    pyautogui.moveRel(xOffset=-100, yOffset=-100, duration=3, pause=3)
    >>> pyautogui.scroll(10)   # scroll up 10 "clicks"
    >>> pyautogui.scroll(-10)  # scroll down 10 "clicks"
    >>> pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

'''




'''
# https://stackoverflow.com/questions/15777719/how-to-detect-key-press-when-the-console-window-has-lost-focus
import win32con, ctypes, ctypes.wintypes

def esc_pressed():
    print("Escape was pressed.")

ctypes.windll.user32.RegisterHotKey(None, 1, 0, win32con.VK_F1)

try:
    msg = ctypes.wintypes.MSG()
    while ctypes.windll.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            esc_pressed()
        ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
        ctypes.windll.user32.DispatchMessageA(ctypes.byref(msg))
finally:
    ctypes.windll.user32.UnregisterHotKey(None, 1)

'''




'''
#Calculator
#We are not really writing a calculator, 
#we rather provide a GUI which is capable of evaluating 
#any mathematical expression and printing the result.


import tkinter as tk
from math import *


def evaluate(event):
    res.configure(text="Result: " + str(eval(entry.get())))


w = tk.Tk()
tk.Label(w, text="Your Expression:").pack()
entry = tk.Entry(w)
entry.bind("", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()
'''




'''
#https://www.python-course.eu/tkinter_entry_widgets.php


import tkinter as tk

fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')

def monthly_payment(entries):
    # period rate:
    r = (float(entries['Annual Rate'].get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(entries['Loan Principle'].get())
    n =  float(entries['Number of Payments'].get())
    remaining_loan = float(entries['Remaining Loan'].get())
    q = (1 + r)** n
    monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
    monthly = ("%8.2f" % monthly).strip()
    entries['Monthly Payment'].delete(0, tk.END)
    entries['Monthly Payment'].insert(0, monthly )
    print("Monthly Payment: %f" % float(monthly))

def final_balance(entries):
    # period rate:
    r = (float(entries['Annual Rate'].get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(entries['Loan Principle'].get())
    n =  float(entries['Number of Payments'].get())
    monthly = float(entries['Monthly Payment'].get())
    q = (1 + r) ** n
    remaining = q * loan  - ( (q - 1) / r) * monthly
    remaining = ("%8.2f" % remaining).strip()
    entries['Remaining Loan'].delete(0, tk.END)
    entries['Remaining Loan'].insert(0, remaining )
    print("Remaining Loan: %f" % float(remaining))

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Final Balance',
           command=(lambda e=ents: final_balance(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Monthly Payment',
           command=(lambda e=ents: monthly_payment(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()


'''


'''
selenium     





Within the URL https://www.inipec.gov.it/cerca-pec/-/pecs/companies to invoke click() on the reCAPTCHA checkbox you need to:

Induce WebDriverWait for the desired frame to be available and switch to it.
Induce WebDriverWait for the desired element to be clickable.
'''