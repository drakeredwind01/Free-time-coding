import pyautogui
import keyboard
import pyperclip
import tkinter as tk

def get_pixel_color(x, y):
    pixel_color = pyautogui.pixel(x, y)
    return "#{:02x}{:02x}{:02x}".format(pixel_color[0], pixel_color[1], pixel_color[2])

def update_color_display(event):
    x, y = pyautogui.position()
    color = get_pixel_color(x, y)
    color_display.config(bg=color)
    color_display.text = color  # Store color in a custom attribute

def copy_color_to_clipboard(event):
    if hasattr(color_display, 'text'):
        pyperclip.copy(color_display.text)

# Create a transparent tkinter window to display the color
root = tk.Tk()
root.attributes("-alpha", 0.7)  # Set window transparency

color_display = tk.Label(root, text="", width=10, height=2)
color_display.pack()

# Bind mouse motion event to update color display
root.bind("<Motion>", update_color_display)

# Bind keyboard shortcut Ctrl+Alt+Z to copy color to clipboard
keyboard.add_hotkey("ctrl+alt+z", copy_color_to_clipboard)

root.mainloop()
