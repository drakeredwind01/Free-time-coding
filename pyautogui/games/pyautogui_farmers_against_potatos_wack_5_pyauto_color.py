import pyautogui
import time

# Define the regions (replace with your region coordinates from the original script)
regions = [
    (343, 382, 682, 57),  # Region 1
    (343, 607, 665, 36),  # Region 2
    (343, 814, 665, 60)   # Region 3
]

# Define the color to search for (replace with desired RGB values)
color_to_find = (0, 255, 0)  # Example: Green (adjust for yellow)

def click_on_color(regions, color):
    for region in regions:
        left, top, width, height = region

        # Loop through pixels within the region
        for y in range(top, top + height):
            for x in range(left, left + width):
                # Check if pixel color matches the desired color
                if pyautogui.pixelMatchesColor(x, y, color):
                    pyautogui.click(x, y)
                    print(f"Clicked color at: {(x, y)}")
                    time.sleep(0.1)  # Pause briefly after clicking
                    return  # Exit the loop after finding a match

if __name__ == "__main__":
    # Continuously search for the color until Esc is pressed
    while True:
        click_on_color(regions, color_to_find)
        if pyautogui.isPressed('esc'):
            break
        time.sleep(0.1)  # Add a small delay to reduce CPU usage