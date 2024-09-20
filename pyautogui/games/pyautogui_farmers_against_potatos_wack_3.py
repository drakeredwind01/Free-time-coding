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
    # (0, 0, 900, 90)  # Region 3
]

# Define the color range for green (in HSV)
lower_green = np.array([40, 40, 40])  # Adjust as needed based on the green in the image
upper_green = np.array([80, 255, 255])


def detect_and_click_green():
    while True:
        # Get the current mouse position (using PyAutoGUI)
        mousePos = pyautogui.position()

        for region in regions:
            print(f"Searching region: {region}")

            # Capture the screen in the defined region
            screen = np.array(ImageGrab.grab(bbox=(region[0], region[1], region[0] + region[2], region[1] + region[3])))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)  # Convert to HSV for better color detection

            # Create a mask for the green color
            mask = cv2.inRange(screen, lower_green, upper_green)
            result = cv2.bitwise_and(screen, screen, mask=mask)

            # Find non-zero points (where green is detected)
            green_points = np.where(mask > 0)

            # If green is detected, click at the first detected point
            if len(green_points[0]) > 0:
                y = green_points[0][0]
                x = green_points[1][0]
                pyautogui.click(region[0] + x, region[1] + y)  # Click the point relative to the region's top-left
                print(f"Clicked at: {(region[0] + x, region[1] + y)}")
                # return  # Exit after clicking, or remove this to keep searching indefinitely

        # Exit condition
        if keyboard.is_pressed('esc'):
            break

        time.sleep(0.1)  # Add a small delay to reduce CPU usage


if __name__ == "__main__":
    detect_and_click_green()
