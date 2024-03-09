import win32gui
import win32api
import win32con
from ctypes import windll

# Specify window title and transparency level (0-255)
window_title = "Your Window Title"
transparency = 128  # Adjust for desired level

# Get window handle
hwnd = win32gui.FindWindow(None, window_title)

# Get window dimensions
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
width, height = right - left, bottom - top

# Set extended window styles for transparency
ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_LAYERED)

# Set window layer info
layered_info = win32api.Struct('DWORD * 2')
layered_info = win32api.s
layered_info.hinstance = 0
layered_info.createversion = win32con.PSAPI_CURRENT_VERSION
layered_info.lpszcusrsrc = None
layered_info.cxcusrsrc = 0
layered_info.cycusrsrc = 0
layered_info.cxsrc = width
layered_info.cysrc = height
layered_info.flags = win32con.LWA_ALPHA
layered_info.dwAlpha = transparency

# Set transparent background
windll.user32.SetWindowEx(hwnd, win32con.LWA_ALPHA, layered_info.pack())

# Maintain transparency while window is open
while True:
    win32api.PumpMessages()
