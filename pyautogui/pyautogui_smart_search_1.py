import pyautogui
import time
import json
import os

IMAGE_PATH = 'your_image.png'  # Replace with the path to your image
COORDINATES_FILE = 'coordinates.json'


def load_coordinates():
    if os.path.exists(COORDINATES_FILE):
        with open(COORDINATES_FILE, 'r') as file:
            return json.load(file)
    return None


def save_coordinates(x, y):
    with open(COORDINATES_FILE, 'w') as file:
        json.dump({'x': x, 'y': y}, file)


def smart_search(image_path):
    search_area = None
    coordinates = load_coordinates()
    if coordinates:
        search_area = (coordinates['x'] - 50, coordinates['y'] - 50, 100, 100)

    while True:
        if search_area:
            location = pyautogui.locateCenterOnScreen(image_path, region=search_area)
        else:
            location = pyautogui.locateCenterOnScreen(image_path)

        if location:
            print(f"Found the image at: {location}")
            pyautogui.click(location)
            save_coordinates(location.x, location.y)
            break
        else:
            if search_area:
                x, y, width, height = search_area
                search_area = (x - width // 2, y - height // 2, width * 2, height * 2)
            else:
                search_area = None

        time.sleep(0.5)


if __name__ == '__main__':
    smart_search(IMAGE_PATH)
