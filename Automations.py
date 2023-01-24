from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from keyboard import press_and_release
import pyttsx3
import webbrowser as web
import speech_recognition as sr
from time import sleep
import  geocoder 
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
# import great_circle_calculator.great_circle_calculator as great_circle
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def Speak(audio):
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

def ChromeAuto(command):
    while True:
        query = str(command)
        if 'new tab' in query:
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
            elif 'instagram' in NameA:
                web.open("https://www.instagram.com/")
            else:
                string = "https://www."+NameA+".com"
                string2=string.replace(" ","")
                web.open(string2)
def YouTubeAuto(command):
    query=str(command)
    if 'pause' in query:
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
        press_and_release('shift + ,')
        click(x=667,y=146)
        Speak("What to search , Ma'am")
        search=TakeCommand()
        write(search)
        sleep(1)
        press('enter')

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def GoogleMaps(Place):
        Url_Place = "https://www.google.com/maps/place/"+str(Place)
        geolocator = Nominatim(user_agent = "myGeocoder")
        location = geolocator.geocode(Place,addressdetails = True)
        target_latlon =location.latitude , location.longitude
        location = location.raw['address']

        target = {'city' : location.get('city',''),
                       'state' : location.get('state',''),
                           'country' : location.get('country','') }

        current_loc = geocoder.ip('me')

        current_latlon = current_loc.latlng
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            
            "latitude": response.get("latitude"),
            "longitude": response.get("longitude")
        }
        current = (location_data['latitude'] , location_data['longitude'])
        distance = str(great_circle(current,target_latlon))
        distance = str(distance.split(' ',1)[0])
        distance = round(float(distance),2)

        Speak(target)
        Speak(f"Ma'am ,{Place} is {distance} kilometere away from Your Location")

