import keyboard  # Use keyboard library for key detection
import win32clipboard     # only for windows
import tkinter as tk
import time
import pyautogui

'''
for ms. diane because she doesn't have windows
so i'm hardcoding the "data"
'''

def check_space(argv):
    return argv.count(" ")

def process_clipboard(starttime):
    """Reads clipboard content, calculates reading times, saves data to CSV."""
    try:
        win32clipboard.OpenClipboard()            # only for windows
        data = win32clipboard.GetClipboardData()  # only for windows
        win32clipboard.CloseClipboard()           # only for windows
        data = "woot it worked"

        # starttime = time.time()

        arg_characters = len(data)
        word_count = check_space(data) + 1  # Count words by counting spaces + 1


        print(data)
        print(f"Number of characters: {arg_characters}")
        print(f"Number of words: {word_count}")

        output_file = "remembering.csv"
        with open(output_file, "a") as csvfile:
            csvfile.write(f"{data}\n")
        return data

    except KeyboardInterrupt:
        print("Script interrupted by user.")
        return data

import tkinter as tk

def show_subscribe_window(text):
    window = tk.Tk()
    window.overrideredirect(True)  # Remove title bar and borders

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    label = tk.Label(window, text=text, font=("Arial", 12, "bold"))
    label.pack()

    label.update_idletasks()  # Update the label to calculate its size
    label_width = label.winfo_reqwidth() + 20  # Add padding
    label_height = label.winfo_reqheight() + 20  # Add padding

    window_x = screen_width - label_width - 55
    window_y = screen_height - label_height - 55
    window.geometry(f"{label_width}x{label_height}+{window_x}+{window_y}")

    label.pack(padx=10, pady=10)

    window.after(3000, window.destroy)

    window.mainloop()


def main_loop():
    '''remove start after debug'''
    data = "testing"
    '''remove end after debug'''

    #to be replaced#
    # if data:  # only do this once
    #     # Check if 'q' is pressed
    #     # if keyboard.is_pressed('shift+q'):
    #     if data:  # do not mess up alignment, so I put in a noop if

    # replace with
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                # Wait for 'shift+q' hotkey to be pressed
                time.sleep(1)  # More time to see the first label
                starttime = time.time()
                process_clipboard(starttime) # working
                data = process_clipboard(starttime) # not working
                show_subscribe_window(data)  # Pass the retrieved data
                time.Qsleep(1)  # wait some to see what happened
        except pyautogui.FailSafeException:
          print("Fail-safe triggered. Exiting.")
          break

if __name__ == "__main__":
    main_loop()
