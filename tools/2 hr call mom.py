import time
from win32comext.shell import shell

#voice stuff
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
speak('speach online')


if __name__ == '__main__':
    speak('adding one hour to the clock')
    starttime = time.time()
    curtime = (time.time() - starttime)
    meettime = 1800
    while 1:
        curtime = (time.time() - starttime)
        waitfor = (meettime-curtime)
        print(waitfor)
        time.sleep(20)
        if (curtime >= meettime):
            print("time met", curtime)
            #shell.ShellExecuteEx(lpFile=r"D:/documents/music/System of a Down/safe.xspf")
            shell.ShellExecuteEx(lpFile=r"D:/documents/music/Halloween/sounds/Halloween_Vocals-Mike_Koenig-517765553.mp3")
            exit()



            '''3600 = hr'''

