import time
import os

#voice stuff
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
#speak('speach online')

import keyboard  # Use keyboard library for key detection


import webbrowser
import pyautogui

#speak('staring in 3')
#speak('2')
#speak('1')



import pyautogui
import pyautogui

def find_and_click(image_path, message):
  """
  This function searches for an image, clicks it if found, and prints a message.
  """
  while True:
    try:
      print(f"searching '{image_path}'")
      hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.973, region=(319, 316, 717, 553))
      # confidence=0.975 almost works
      # confidence=0.973 almost works almost great
      # (343, 382), (1025, 439)
      # (343, 607), (1008, 643)
      # (343, 814), (1008, 874)
      if hit:
        print(message)
        pyautogui.click(hit)
        break
      if keyboard.is_pressed('shift+q'):
        exit()
      if keyboard.is_pressed('esc'):
        exit()
      else:
        print(f"Image '{message}' not found, retrying...")
    except pyautogui.ImageNotFoundException:
      pass  # Do nothing on purpose, loop will continue searching

def find_2_and_click(image_path_1, message_1, image_path_2, message_2):
  """
  This function searches for an image, clicks it if found, and prints a message.
  """
  while True:
    try:
      print(f"searching '{image_path_1}'")
      hit = pyautogui.locateCenterOnScreen(image_path_1, confidence=0.8)
      if hit:
        print(message_1)
        pyautogui.click(hit)
        pass
      print(f"searching '{image_path_2}'")
      hit_2 = pyautogui.locateCenterOnScreen(image_path_2, confidence=0.5)
      if hit_2:
        print(message_2)
        pyautogui.click(hit_2)
      # pass  # Do nothing on purpose, loop will continue searching
      if keyboard.is_pressed('shift+q'):
        exit()
      if keyboard.is_pressed('esc'):
        exit()
    except pyautogui.ImageNotFoundException:
      print(f"Image not found, retrying...")
      # Optionally, add a delay between retries
      # time.sleep(1)  # Uncomment to introduce a delay
      pass

def main():
  """
  This function calls the find_and_click function for vm and beta images, then presses ctrl+tab.
  This loop will repeat the entire process indefinitely.
  """
  while True:
    find_and_click('../IMAGE_PATH/farmer_against_potatos_green.png', 'hit farmer_against_potatos_green')

if __name__ == "__main__":
  main()

'''
    mousepose = pyautogui.position()
    find_and_click('../IMAGE_PATH/wco_tv_play_button.png', 'hit wco_tv_play_button.png')
    pyautogui.moveRel(xOffset=-50,yOffset=0)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'tab')  # Press ctrl+tab
    time.sleep(1)
    pyautogui.scroll(-700) # Press page down


'''