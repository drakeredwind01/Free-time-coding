import keyboard
from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui
import time

# Define the regions where to search
regions = [
    (343, 382, 682, 57),  # Region 1
    (343, 607, 665, 36),  # Region 2
    (343, 814, 665, 60)   # Region 3
]

# Define the color range for green (in HSV)
lower_green = np.array([40, 40, 40])  # Adjust as needed based on the green in the image
upper_green = np.array([80, 255, 255])

# Define the color range for yellow (in HSV), refined to avoid green
lower_yellow = np.array([22, 150, 200])  # Adjust Hue range to [22, 30]
upper_yellow = np.array([35, 255, 255])  # Adjust Hue range to [35, 40]

def wait():
    while True:
        time.sleep(2)
        if keyboard.is_pressed('q'):
            return

def search_color(screen, lower_bound, upper_bound):
    """Search for a color in the screen capture within the given HSV bounds."""
    mask = cv2.inRange(screen, lower_bound, upper_bound)
    points = np.where(mask > 0)
    return points

def detect_and_click_color():
    while True:
        # Get the current mouse position (using PyAutoGUI)
        mousePos = pyautogui.position()

        for region in regions:
            # Capture the screen in the defined region
            screen = np.array(ImageGrab.grab(bbox=(region[0], region[1], region[0] + region[2], region[1] + region[3])))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)  # Convert to HSV for color detection

            # First, attempt to detect green
            green_points = search_color(screen, lower_green, upper_green)
            print('looking for green')
            if len(green_points[0]) > 0:
                # If green is detected, click the first detected point
                y = green_points[0][0]
                x = green_points[1][0]
                pyautogui.click(region[0] + x, region[1] + y)
                print(f"Clicked green at: {(region[0] + x, region[1] + y)}")
                time.sleep(0.1)  # Pause briefly after clicking
                continue  # Start the next iteration immediately after detecting green

            # If no green is found, attempt to detect yellow
            yellow_points = search_color(screen, lower_yellow, upper_yellow)
            print('looking for yellow')

            if len(yellow_points[0]) > 0:
                # If yellow is detected, click the first detected point
                y = yellow_points[0][0]
                x = yellow_points[1][0]
                pyautogui.click(region[0] + x, region[1] + y)
                print(f"Clicked yellow at: {(region[0] + x, region[1] + y)}")
                time.sleep(0.1)  # Pause briefly after clicking

        # Exit condition
        if keyboard.is_pressed('esc'):
            wait()
            break

        time.sleep(0.1)  # Add a small delay to reduce CPU usage

if __name__ == "__main__":
    detect_and_click_color()
