import time
import os
import win32clipboard # for clipboard
'''SUCCESS'''
import sys

#voice stuff
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate', 350)
engine.setProperty('pitch', 1)
# my limit 2023.11.19.19.18.27.053 400  hard 500


def speak(audio):
    # print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

'''
activate tf
python "D:\Documents\github\Free-time-coding\tools\_read to me args (with read time)_(csv)_4.0.py" "
'''

if __name__ == '__main__':


    '''
    args = sys.argv
    args = sys.argv[1:]
    args = str(sys.argv[0:])
    arg_line = " ".join(sys.argv[1:])
    '''


    arg_line = " ".join(sys.argv[1:])
    '''    
    args = args.replace("[", "")
    args = args.replace("]", "")
    args = args.replace(",", "")
    args = args.replace("'", "")
    '''
    starttime = time.time()
    print(arg_line)
    argCharicters = len(arg_line)
    #print(argCharicters) redundant
    print(f"__________________________________________________") #testing
    print(f"Number of charicters: {argCharicters}") #testing


    def check_space(argv):
        return argv.count(" ")
    word_count = {check_space(arg_line) + 1}
    print(f"Number of words: {check_space(arg_line)+1}")

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    speak(data)
    curtime = (time.time() - starttime)
    # print(curtime)    # redunant
    print(f"AI TIME: {curtime}")  # testing
    # AIWPM = (number of words) / (time in minutes)
    # AIWPM = (435 words) / (64.37510085105896 seconds/ 60 seconds/minute)
    # AIWPM = 418.829 WPM
    # print(f"AI W/M: {int(argCharicters / curtime)}")  # wrong
    print(f"AI W/M: {int(argCharicters / (curtime / 60))}")  # testing
    # AI words per minute is calculated by dividing the number of characters by the time in minutes (since 1 minute is equal to 60 seconds)
    number_of_words = len(word_count)  # Get the number of words from the set
    # print(f"Human TIME: {int(number_of_words / 2.5)}") is always 0. don't know why
    print(f"Human TIME: {int(word_count.pop() / 2.5)}")  # Get and remove the only element, then divide
    print(f"Human W/M: 150")  # testing
    # TODO add human would take to read time
    # Human words per minute is assumed to be 150 words per minute

    # total time saved = (human reading time - AI reading time)
    total_time_saved = int(curtime - ((check_space(arg_line) + 1) / 150)) # wrong


    print(
        f"Total Time Saved: {total_time_saved} seconds"
    )  # testing

    # for google sheets
    print(
        f"{argCharicters},{word_count},{curtime},{total_time_saved}"
    )



