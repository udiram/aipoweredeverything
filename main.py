import pyttsx3
import numpy as np
engine = pyttsx3.init('nsss')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
file = open("vid1script.txt", "r")
content = file.read()
# print(content)
# engine.say(content)
engine.save_to_file(content, 'vid1.wav')
engine.runAndWait()
