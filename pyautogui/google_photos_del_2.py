'''
this program deletes a file from photos when the '4' key is pressed
right fingers on left and right
left middle finger on delete and pointer on '4'
'''

import time
import keyboard  # Use keyboard library for key detection
import pyautogui

def find_click_count(image_path, message,count):
  """
  This function searches for an image, clicks it if found, and prints a message with a count.
  """
  while True:
    try:
      # print(f"searching '{image_path}'")
      hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
      if hit:
        print(f"'deleted '{count}' items so far!")
        pyautogui.click(hit)
        break
      else:
        print(f"Image '{message}' not found, retrying...")
    except pyautogui.ImageNotFoundException:
      pass  # Do nothing on purpose, loop will continue searching

def find_and_click(image_path, message):
    """
    This function searches for an image, clicks it if found, and prints a message.
    """
    while True:
        try:
            # print(f"searching '{image_path}'")
            hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if hit:
                print(message)
                pyautogui.click(hit)
                break
            else:
                print(f"Image '{message}' not found, retrying...")
        except pyautogui.ImageNotFoundException:
            pass  # Do nothing on purpose, loop will continue searching


def main_loop():
    count=0
    while True:
        # Check if 'q' is pressed
        if keyboard.is_pressed('4'):
            pyautogui.moveRel(-1,0)
            count += 1
            time.sleep(0.5)
            find_click_count("IMAGE_PATH/google/google_photos_delete.png","deleting", count)
            find_and_click("IMAGE_PATH/google/google_photos_move_to_trash.png", "moving to trash")


if __name__ == "__main__":
    print('ready!')
    main_loop()
