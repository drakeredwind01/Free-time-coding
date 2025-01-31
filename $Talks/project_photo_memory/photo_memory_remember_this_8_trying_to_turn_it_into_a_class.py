'''
it's insane I tried to write down a file only for the hotkey logic
and import the working script and surly it would work right?
WRONG!
why do keyboard and tinkter hate each other so much!?!
are they in a blood feud or something?
'''
import threading
import time
import tkinter as tk
import keyboard

# Hardcoded data for non-Windows systems
data = "This is some example text for demonstration purposes."

class HotkeyManager:
    def __init__(self, hotkey="shift+q"):
        self.hotkey = hotkey
        self.hotkey_pressed = False

    def start(self):
        # Use a separate thread to avoid blocking the tkinter loop
        thread = threading.Thread(target=self.check_hotkey)
        thread.daemon = True  # Ensure thread terminates with main program
        thread.start()

    def check_hotkey(self):
        while True:
            if keyboard.is_pressed(self.hotkey):
                self.hotkey_pressed = True
                # Trigger an event or set a flag to notify the tkinter loop
                # (implementation details omitted here)
                time.sleep(0.1)  # Avoid excessive CPU usage

class App:
    def __init__(self):
        self.hotkey_manager = HotkeyManager()
        self.hotkey_manager.start()
        self.root = tk.Tk()
        self.root.title("Clipboard Reader")
        self.root.overrideredirect(True)  # Remove title bar and borders
        self.data_label = tk.Label(self.root, text="")
        self.data_label.pack(padx=10, pady=10)
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Add a button to trigger data processing and window display
        # (assuming you don't want hotkey detection anymore)
        self.process_button = tk.Button(self.root, text="Process Clipboard", command=self.process_clipboard)
        self.process_button.pack()

    def process_clipboard(self):
        # Function to retrieve and process clipboard data
        # (replace with your actual clipboard processing logic)
        print(data)  # Simulate clipboard data retrieval (replace with actual code)
        self.data_label.config(text=data)

if __name__ == "__main__":
    app = App()