import pyttsx3 as pyt # type: ignore
import speech_recognition as sr # type: ignore
import datetime as dt
import wikipedia as wiki # type: ignore
import webbrowser as wb
import os

# Taking voice from my system
engine = pyt.init('sapi5') 
voices = engine.getProperty('voices') # to get properties from system
#print(voices[1].id)  To check type of voice i.e. male or female
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
# Speak function
def speak(text):
    """This function will takes text and returns voice

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()   # to close speak property

# Speech recognition function
def takeCommand():
    """ This function will recognize voice and returns text
    """
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshpld = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            querry = r.recognize_google(audio,language=('en-in'))
            print(f"User said: {querry}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return querry
    

text =takeCommand()
speak(text)
print("Ok")






