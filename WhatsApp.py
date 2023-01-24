import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser 
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query.lower()

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message")
    a = Command()
    speak("What's the message")
    message = Command()
    if a == 'priya':
       pywhatkit.sendwhatmsg("+916307033814",message,time_hour=strTime,time_min=update)
    elif a=='nisha':
       pywhatkit.sendwhatmsg("+919119321170",message,time_hour=strTime,time_min=update)
    elif a=='chitrakshi':
       pywhatkit.sendwhatmsg("+918394813877",message,time_hour=strTime,time_min=update)
    elif a=='daksh':
        pywhatkit.sendwhatmsg("+919119189909",message,time_hour=strTime,time_min=update)
    elif a=='saurabh':
        pywhatkit.sendwhatmsg("+918306343469",message,time_hour=strTime,time_min=update)
    elif a=='abhishek':
        pywhatkit.sendwhatmsg("+919557896980",message,time_hour=strTime,time_min=update)