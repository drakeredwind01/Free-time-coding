import time
import os

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

    speak(arg_line)
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


'''
python "D:\documents\ai\python\my-first-conda-project\_read to me args (with read time)2.py" "
596 = 5min = 300sec
'''
'''
python "D:\Documents\github\Free-time-coding\tools\_read to me args (with read time)_(csv)_4.py" "
'''



'''

    print(
        "{argCharicters},{wordcount},{curtime},{total_time_saved}".format(
            argCharicters=argCharicters,
            wordcount=numWords,
            curtime=curtime,
            total_time_saved=total_time_saved,
        )
    )

'''
'''

(1)  print("First number is {} and second number is {}".format(first, second))
(1b) print("First number is {first} and number is {second}".format(first=first, second=second)) 
or

(2) print('First number is', first, 'second number is', second) 
(Note: A space will be automatically added afterwards when separated from a comma)

or

(3) print('First number %d and second number is %d' % (first, second))
or

(4) print('First number is ' + str(first) + ' second number is' + str(second))
  
Using format() (1/1b) is preferred where available.



20240731T085709Z
_read to me args (with read time)_(csv)_4.py
    adding human read time estimate
    output:
        284                                                 removed
        __________________________________________________  added
        Number of charicters: 284
        Number of words: 48
        8.958579540252686                                   removed
        AI TIME: 8.958579540252686
        AI W/M: 1902
        Human TIME: 19                                      added
        Human W/M: 150
        Total Time Saved: 8 seconds
        284,set(),8.958579540252686,8


'''

