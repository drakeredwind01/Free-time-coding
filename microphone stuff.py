
import speech_recognition as s_r


if __name__ == '__main__':


    s_r.Microphone.list_microphone_names()
    print(s_r.__version__)
    print(s_r.Microphone.list_microphone_names())  # print all the microphones connected to your machine
    r = s_r.Recognizer()
    mic = s_r.Microphone(device_index=1)

    with mic as source:
        print("Say now!!!!")
        audio = r.listen(source) #take voice input from the microphone
    print(r.recognize_google(audio)) #to print voice into text


'''
#shell.ShellExecuteEx(lpVerb='runas', lpFile=r"D:/documents/ahk/0 WARFRAME.ahk")
#shell.ShellExecuteEx(lpVerb='runas', lpFile=r'D:/Program Files (x86)/Steam/steamapps/common/Warframe/Warframe.x64.exe')
#shell.ShellExecuteEx("D:/documents/ahk/0 WARFRAME .ahk")
#shell.ShellExecuteEx('D:/Program Files (x86)/Steam/steamapps/common/Warframe/Warframe.x64.exe')
keyboard.type("Black")
keyboard.press(enter)
keyboard.release(enter)
'''
