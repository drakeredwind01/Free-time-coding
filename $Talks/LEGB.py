import time
import win32clipboard
import pyautogui
import keyboard  # Use keyboard library for key detection

# Voice stuff (optional)
import pyttsx3

__author__ = "Drake_Redwind"
print(__author__)

where_in_the_script = "I am reading from global scope"

class PascalCase():
    where_in_the_script = "I am reading from class scope"

    def __init__(self):
        print("i'm in class > __init__")
        where_in_the_script = "I am reading from local scope \n"
        print(self.where_in_the_script)  # Prints "I am reading from class scope"
        print(where_in_the_script)  # Prints "I am reading from global scope"

    def print_simple(self):
        print("i'm in class > print_simple")
        were_in_the_script = "I am reading from local scope within print_simple \n"
        print(self.where_in_the_script)  # Prints "I am reading from class scope"
        print(were_in_the_script)  # Prints "I am reading from global scope"

    def main_loop(self):
        print("i'm in class > main_loop")
        print("Ready \n")
        self.print_simple()


if __name__ == "__main__":
    PascalCase().main_loop()