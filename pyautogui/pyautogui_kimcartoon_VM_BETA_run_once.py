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





import webbrowser
import pyautogui

#speak('staring in 3')
#speak('2')
#speak('1')



import pyautogui

def find_and_click(image_path, message):
  """
  This function searches for an image, clicks it if found, and prints a message.
  """
  while True:
    try:
      hit = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
      if hit:
        print(message)
        pyautogui.click(hit)
        break
      else:
        print(f"Image '{message}' not found, retrying...")
    except pyautogui.ImageNotFoundException:
      pass  # Do nothing on purpose, loop will continue searching

def main():
  """
  This function calls the find_and_click function for vm and beta images, then presses ctrl+tab.
  """
  find_and_click('D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\vm.png', 'hit vm')
  find_and_click('D:\\Documents\\github\\Free-time-coding\\pyautogui\\IMAGE_PATH\\beta.png', 'hit beta')
  pyautogui.hotkey('ctrl', 'tab')  # Press ctrl+tab

if __name__ == "__main__":
  main()
































