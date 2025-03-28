import keyboard
import pyautogui

num_of_clicks = 100
print(f"will click {num_of_clicks} times")

def main():
    while True:
        if keyboard.is_pressed('shift+q'):
            pyautogui.click(clicks=num_of_clicks)
            # Optional: Add a small delay to prevent excessive clicks
            # time.sleep(0.1)  # Import the time module: import time

if __name__ == "__main__":
    main()