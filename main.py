import pyttsx3 
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from Features import GoogleSearch
from Features import Alarm
from Features import Temp
from Features import Calculator
from Features import DownloadYoutube
from Features import YoutubeSearch
import os
from keyboard import press
from keyboard import write
from keyboard import press_and_release
import webbrowser as web
from pyautogui import click
from time import sleep
import datetime
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def TakeCommand():
    #It takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again Please...")
        return "None"
    query = query.lower()
    return query
#speak("Hello Zeenat,How are you?")
def TaskExe():
    
    while True:
        query = TakeCommand()
        if 'set alarm' in query :
            Alarm(query)
        elif 'youtube search' in query:
            query=query.replace("youtube search ","")
            YoutubeSearch(query)
        elif 'google search' in query:
            query=query.replace("google search","")
            GoogleSearch(query)
        elif 'whatsapp' in query:
            from WhatsApp import sendMessage
            sendMessage()
        elif 'temperature' in query:
            Temp(query)
        elif 'calculate' in query:
            Calculator(query)
        elif 'download youtube' in query:
            DownloadYoutube()
        elif 'my location' in query:
            from Features import get_location
            get_location()
        elif 'distance from' in query:
            from Automations import GoogleMaps
            query=query.replace("distance from ","")
            query=query.replace("jarvis ","")
            query=query.replace("tell me ","")
            query=query.replace("the ","")
            GoogleMaps(query)

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            length=len(songs)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0, length-1)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'new tab' in query:
            press_and_release('ctrl+t')
        elif 'close tab' in query:
            press_and_release('ctrl+w')
        elif 'new window' in query:
            press_and_release('ctrl+n')
        elif 'history' in query:
            press_and_release('ctrl+h')
        elif 'download' in query:
            press_and_release('ctrl+j')
        elif 'bookmark' in query:
            press_and_release('ctrl+d')
            press('enter')
        elif 'incognito' in query:
            press_and_release('ctrl+shift+n')
        elif 'switch tab' in query:
            tab=query.replace("switch tab ","")
            Tab=tab.replace("to ","")
            num  = Tab
            bb = f'ctrl+{num}'
            press_and_release(bb)
        elif 'open' in query:
            name=query.replace("open ","")
            NameA = str(name)
            if 'youtube' in NameA:
                web.open("https://www.youtube.com/")
            elif 'instagram' in NameA:
                web.open("https://www.instagram.com/")
            elif 'facebook' in NameA:
                web.open("https://www.facebook.com/")
            else:
                string = "https://www."+NameA+".com"
                string2=string.replace(" ","")
                web.open(string2)
        elif 'pause' in query:
            press('space bar')
        elif 'resume' in query:
            press('space bar')
        elif 'full screen' in query:
            press('f')
        elif 'film screen' in query:
            press('t')
        elif 'skip' in query:
            press('l')
        elif 'back' in query:
            press('j')
        elif 'increase' in query:
            press_and_release('shift + .')
        elif 'decrease' in query:
            press_and_release('shift + ,')
        elif 'previous' in  query:
            press_and_release('shift + p')
        elif 'next' in query:
            press_and_release('shift + n')
        elif 'mute' in query:
            press('m')
        elif 'unmute' in query:
            press('m')
        elif 'search' in query:
            print("hey            hello       bye")
            click(x=667,y=146)
            speak("What to search , Ma'am")
            search=TakeCommand()
            write(search)
            sleep(1)
            press('enter')
    
TaskExe()