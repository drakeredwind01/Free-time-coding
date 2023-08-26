import win32gui



hwnd = win32gui.FindWindow(None, 'Cave Story+')
x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0
h = y1 - y0
#win32gui.MoveWindow(hwnd, x0, y0, w-100, h-100, True)
win32gui.MoveWindow(hwnd, x0, y0+100, w, h, True)
