# import keyboard  # Use keyboard library for key detection
# import win32clipboard     # only for windows
import tkinter as tk
import time
'''
for ms. diane because she doesn't have windows
so i'm hardcoding the "data"
'''
text = "This is a longer message that might require dynamic sizing."

data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 1  ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 2    "
data = "Lorem ipsum dolor sit amet, "
def check_space(argv):
    return argv.count(" ")

def process_clipboard(starttime):
    """Reads clipboard content, calculates reading times, saves data to CSV."""
    try:
        # win32clipboard.OpenClipboard()            # only for windows
        # data = win32clipboard.GetClipboardData()  # only for windows
        # win32clipboard.CloseClipboard()           # only for windows
        data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 1\nullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 2    "

        # starttime = time.time()

        arg_characters = len(data)
        word_count = check_space(data) + 1  # Count words by counting spaces + 1


        # Print results for user feedback
        print(data)
        print(f"Number of characters: {arg_characters}")
        print(f"Number of words: {word_count}")

        '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 1  ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 2    
        '''

        # Save data to CSV (append if file exists)
        output_file = "remembering.csv"
        with open(output_file, "a") as csvfile:
            csvfile.write(f"{data}\n")
        output_file = "_read_to_me_args_log.log"
        # with open(output_file, "a") as csvfile:
        #     csvfile.write(f"{word_count},{human_time},{ai_time},{speed_setting}\n")
        return data

    except KeyboardInterrupt:
        print("Script interrupted by user.")
    except (AttributeError, win32clipboard.error):
        print("Error: Clipboard access denied or necessary libraries not installed.")


import tkinter as tk

def show_subscribe_window(text):
    """
    Creates a small window anchored at the bottom right corner of the screen,
    dynamically sizing to fit the given text.

    Args:
        text: The text to display in the window.
    """
    window = tk.Tk()
    window.overrideredirect(True)  # Remove title bar and borders

    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Create a label to measure text size
    label = tk.Label(window, text=text, font=("Arial", 12, "bold"))
    label.pack()

    # Get label dimensions
    label.update_idletasks()  # Update the label to calculate its size
    label_width = label.winfo_reqwidth() + 20  # Add padding
    label_height = label.winfo_reqheight() + 20  # Add padding

    # Calculate window position and dimensions
    window_x = screen_width - label_width - 55
    window_y = screen_height - label_height - 55
    window.geometry(f"{label_width}x{label_height}+{window_x}+{window_y}")

    # Display the label in the window
    label.pack(padx=10, pady=10)

    window.after(3000, window.destroy)  # Close after 3 seconds

    window.mainloop()

    # # Example usage
    # text = "This is a longer message that might require dynamic sizing."
    # show_subscribe_window(text)

def main_loop():
    '''remove start after debug'''
    data = "testing"
    '''remove end after debug'''
    # speak("ready my master")
    # while True:
    if data:  # only do this once
        # Check if 'q' is pressed
        # if keyboard.is_pressed('shift+q'):
        if data:  # do not mess up alignment, so I put in a noop if
            time.sleep(2)  # More time to see the first label
            starttime = time.time()
            process_clipboard(starttime) # working
            data = process_clipboard(starttime) # not working
            # time.sleep(3) # tried uptting this in to wait an extended time because gemini said the "process_clipboard" function might be taking to long but i don't think this is relevant
            show_subscribe_window(data)  # Pass the retrieved data
            # Add a small delay to avoid multiple triggers from a single press
            time.sleep(10)  # wait some to see what happened
            #  This will now exit Python when sleep is done.

if __name__ == "__main__":
    show_subscribe_window(data)
    main_loop()
