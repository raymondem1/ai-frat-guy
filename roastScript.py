import requests
import pyttsx3
from better_profanity import profanity

engine = pyttsx3.init()

eb =""

def roast():
    global eb
    context = "Your mom is a hoe.\nYou are the proof that God makes mistakes\nYou make me want to go blind\nDo us a favor and stay inside\nYou look like an anti cigaretts commercial\n"
    payload = {
    "context": context,
    "token_max_length": 64,
    "temperature": 0.6,
    "stop_sequence": "\n"
        }
    response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()
    eb =response["text"]
    if __name__=='__main__':
        eb=profanity.censor(eb)
        if("****" in eb):
            eb= "saying this instead of what he wanted to say so nobody gets cancelled"
    print(eb)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.say(eb)
    engine.runAndWait()
