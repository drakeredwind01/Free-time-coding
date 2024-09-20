import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate', 200)

# Experiment with different pitch values
pitches = [0.5, 1.0, 1.5]
for pitch in pitches:
    engine.setProperty('pitch', pitch)
    engine.say("This is a test with pitch: " + str(pitch))
    engine.runAndWait()
'''
activate tf
python "D:\Documents\github\Free-time-coding\tools\_read to me args testing other voicees.py" "
'''