import pywhatkit
import wikipedia
from pywikihow import WikiHow,search_wikihow
import os
import webbrowser as web
import pyttsx3
import wolframalpha
import requests
from playsound import playsound
import datetime




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def RingerNow(time):
    print("where")
    time_to_set= str(time)
    time_now = time_to_set.replace("jarvis","")
    time_now = time_now.replace("set alarm for","")
    time_now = time_now.replace("set ","")
    time_now = time_now.replace("alarm  ","")
    time_now = time_now.replace("for ","")
    time_now = time_now.replace(" and ",":")
    time_now = time_now.replace(" ","")


    Alarm_time = str(time_now)
    print(Alarm_time)
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_time == Alarm_time :
            print("Wake Up ma'am , It's time to work.")
            playsound("D:\\music\\Ddlj Short.wav")
            
        elif current_time > Alarm_time:
            break




def YoutubeSearch(term):
    result = "https://www.youtube.com/results?search_query="+term
    web.open(result)
    Speak("This is what I found ma'am")
    pywhatkit.playonyt(term)
#YoutubeSearch('Srk movies')  
def GoogleSearch(Query):
    # query=term.replace("jarvis","")
    # query=query.replace("what is","")
    # query=query.replace("how to","")
    # query=query.replace("what is","")
    # query=query.replace(" ","")
    # query = query.replace("who is","")
    # query=query.replace("what do you mean by","")
    
    #Query=str(term)
    pywhatkit.search(Query)
    if 'how to' in Query:
        max_result=1
        how_to_func=search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)

    else:
        search=wikipedia.summary(Query,2)
        Speak(f":According to your search : {search}")

def Alarm(query):
    TimeHere = open("C:\\Users\\user\\Desktop\\complete-jarvis\\Data.txt","a")
    TimeHere.write(query) # this will save our given command to data.txt file
    TimeHere.close()
    print("here")
    extracted_time = open("C:\\Users\\user\\Desktop\\complete-jarvis\\Data.txt",'rt')
    time = extracted_time.read()
    Time = str(time)
    
    
    deleted_time = open("C:\\Users\\user\\Desktop\\complete-jarvis\\Data.txt",'r+')
    deleted_time.truncate(0) # it means that in file thwe remaining word will be equal to the parameter(0 here)
    deleted_time.close()

    # path=r"C:\\Users\\user\\Desktop\\complete-jarvis\\Database\\ExtraPro\\Alarm.py"
    # os.startfile("C:\\Users\\user\\Desktop\\complete-jarvis\\Database\\ExtraPro\\Alarm.py")
    RingerNow(Time)
    
    print("there")

def DownloadYoutube():
     from pytube import YouTube
     from pyautogui import click
     from pyautogui import hotkey
     import pyperclip 
     from time import sleep
     sleep(2)
     click(x=942,y=59)
     hotkey('ctrl','c')
     value = pyperclip.paste()
     Link=str(value)

     def Download(link):
        url=YouTube(link)
        video = url.streams.first()
        video.download("C:\\Users\\user\\Desktop\\complete-jarvis\\Database\YouTube")

    
     Download(Link)
     Speak("")
     Speak("one Ma'am ,I have downloaded the video")
     Speak("You can go and check it out")
     os.startfile("C:\\Users\\user\\Desktop\\complete-jarvis\\Database\YouTube")
# Alarm('set alarm for 10 and 43'
# Alarm('set alarm for 10 and 43
#DownloadYoutube()
def WolfRam(query):
    api_key = "G4G4R7-RGG44Y7XYA"
    requester = wolframalpha.Client(api_key) #It will prepare the database
    requested =  requester.query(query) #will give the results

    try:
      Answer = next(requested.results).text
    #   Speak(f"{Answer}")
      return Answer
    except:
        Speak("Sorry Ma'am,I did not find suitable results")

# kk=WolfRam('Temperature in delhi')
# print(kk)

def Calculator(query):
    Term=str(query)
    Term=Term.replace("jarvis","")
    Term=Term.replace("multiply","*")
    Term=Term.replace("plus","+")
    Term=Term.replace("minus","-")
    Term=Term.replace("into","*")
    Term=Term.replace("divide by","/")

    final = str(Term)
    try :
        result=WolfRam(final)
        Speak(result)
        print(result)
    except:
        Speak("Sorry Ma'am , I could not do it")
def Temp(query):
    Term=str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("in ","")
    Term = Term.replace("what is the ","")
    Term = Term.replace("temperature" ,"")
    temp_query=str(Term)

    if 'outside' in temp_query:
        var1="temperature in delhi"
        answer = WolfRam(var1)
        Speak(f"{var1} is {answer}")
    else :
        var2 = "temperature in "+ temp_query
        ans = WolfRam(var2)
        Speak(f"{var2} is {ans}")

# WolfRam('temperature in jaipur')
# Calculator('50 plus 50')
# Temp('temperature outside')
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }

    Speak(f"Ma'am your location is {location_data['city'] ,location_data['region']}")
    



