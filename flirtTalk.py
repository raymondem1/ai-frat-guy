
import requests
import pyttsx3
from better_profanity import profanity

engine = pyttsx3.init()

ea =""


def flirt(): 
    global ea
    context = "You can stay as long as you want, but your pants need to leave.\nI am a treasure hunter, how about I explore your chest?\nI am on top of things. Would you like to be one of them?\nI love my bed, but I rather be in yours\nDo you have room for 8 inches?\n"
    payload = {
    "context": context,
    "token_max_length": 64,
    "temperature": 0.6,
    "stop_sequence": "\n"
        }
    response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()
    ea =response["text"]
    if __name__=='__main__':
        ea=profanity.censor(response["text"])
        if("****" in ea):
            ea= "saying this instead of what he wanted to say so nobody gets cancelled"
    print(ea)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.say(ea)
    engine.runAndWait()
