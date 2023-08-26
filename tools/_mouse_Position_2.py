from tkinter import *
from pyautogui import position
from time import sleep
from keyboard import is_pressed

window = Tk()
w = 200
h = 40
a = 1
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
window.wm_attributes('-topmost', 'true')
text = Text(window, font=("Helvetica", 20), borderwidth=2, relief="solid")
p = 1

while True:
    x, y = position()
    posStrx = str(x).rjust(4)
    posStry = str(y).rjust(4)
    mousepos = 'X: ' + posStrx + ' Y: ' + posStry
    text.insert(INSERT, mousepos)
    text.pack()
    sleep(0.0005)
    x = int(posStrx) + 15
    y = int(posStry) + 15

    if is_pressed('ctrl+shift+b'):
        a = 0
    elif is_pressed('ctrl+shift+k'):
        a = 1
    elif is_pressed('ctrl+shift+x'):
        a = 2

    if a == 1:
        window.wm_overrideredirect(1)
        if 0 < x <= (6 * ws / 8) and 0 < y <= (7 * hs / 8):
            window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        elif (6 * ws / 8) <= x and 0 < y <= (7 * hs / 8):
            window.geometry('%dx%d+%d+%d' % (w, h, (x - (w + 30 + 10)), y))
        elif 0 < x <= (6 * ws / 8) and (7 * hs / 8) <= y:
            window.geometry('%dx%d+%d+%d' % (w, h, x, (y - (h + 30 + 10))))
        else:
            window.geometry('%dx%d+%d+%d' % (w, h, (x - (w + 30 + 10)), (y - (h + 30 + 10))))

    elif a == 0:
        if p == 1:
            window.wm_overrideredirect(0)
            window.geometry('%dx%d+%d+%d' % (w, h * 2, (ws - w - 20), (h - (h / 2))))
            p = p + 1
        else:
            window.wm_overrideredirect(0)
            window.geometry('%dx%d' % (w * 1.2, h))

    window.update()
    text.delete(1.0, END)
    text.pack()

    if a == 2:
        break

window.destroy()
