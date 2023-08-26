import time
import os

import sys

#voice stuff
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate', 400)


def speak(audio):
    # print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


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
    print(len(arg_line))


    def check_space(argv):
        return argv.count(" ")
    print(f"Number of Spaces: {check_space(arg_line)+1}")


    speak(arg_line)
    curtime = (time.time() - starttime)
    print(curtime)

'''
python "D:\documents\ai\python\my-first-conda-project\_read to me args (with read time).py" "
596 = 5min = 300sec
'''

