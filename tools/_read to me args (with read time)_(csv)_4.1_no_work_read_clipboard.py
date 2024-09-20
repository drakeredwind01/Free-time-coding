import pyautogui
import time
import sys
'''doesn't work can't figure this out'''
# Voice stuff (optional)
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate', 350)
engine.setProperty('pitch', 1)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()  # Uncomment these lines if you want voice output

def main():
    try:
        # Read from clipboard
        clipboard_content = pyautogui.getClipboardText()

        # ... (rest of your code)

    except KeyboardInterrupt:
        print("Script interrupted by user.")
    except AttributeError:
        print("Error: pyautogui is not installed or clipboard access is denied.")
    """Reads clipboard content, calculates reading time, and prints results."""

    # Read from clipboard
    clipboard_content = pyautogui.getClipboardText()

    # Validate if clipboard content is empty
    if not clipboard_content:
        print("Clipboard is empty!")
        return

    starttime = time.time()

    # Calculate character count and word count (assuming basic space separation)
    char_count = len(clipboard_content)
    word_count = len(clipboard_content.split()) + 1  # Add 1 to account for last word

    # Print basic information
    print("__________________________________________________")
    print(f"Number of characters: {char_count}")
    print(f"Number of words: {word_count}")

    # Calculate estimated AI reading time (assuming average WPM)
    ai_wpm = 400  # Adjust this value based on your model's performance
    ai_time = char_count / (ai_wpm / 60)  # Convert WPM to minutes

    # Print AI reading time and estimated words per minute
    speak(clipboard_content)  # Uncomment this line to speak the content (optional)
    print(f"AI TIME: {ai_time:.2f} seconds")
    print(f"AI W/M: {int(char_count / ai_time)}")

    # Assume a human reading speed of 150 WPM for comparison
    human_wpm = 150
    human_time = word_count / human_wpm

    # Print estimated human reading time
    print(f"Human TIME: {human_time:.2f} seconds")
    print(f"Human W/M: {human_wpm}")

    # Calculate estimated time saved
    total_time_saved = int(ai_time - human_time)
    print(f"Total Time Saved: {total_time_saved} seconds")

    # Print output for Google Sheets (optional)
    print(f"{char_count},{word_count},{ai_time:.2f},{total_time_saved}")

if __name__ == "__main__":
    main()