import random
import pyttsx3

engine = pyttsx3.init()

def frat():
    lines = open('fratLines.txt').read().splitlines()
    myline =random.choice(lines)
    print(myline)
    engine.say(myline)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()
