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
    argCharicters = len(arg_line)
    print(argCharicters)


    def check_space(argv):
        return argv.count(" ")
    numWords = {check_space(arg_line)+1}
    print(f"Number of words: {check_space(arg_line)+1}")


    speak(arg_line)
    curtime = (time.time() - starttime)
    print(curtime)

    # for google sheets
    print("{argCharicters},{wordcount},{curtime}".format(argCharicters=argCharicters, wordcount=numWords, curtime=curtime))


'''
python "D:\documents\ai\python\my-first-conda-project\_read to me args (with read time)2.py" "
596 = 5min = 300sec
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








'''

