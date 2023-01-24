
from playsound import playsound
import datetime


extracted_time = open("C:\\Users\\user\\Desktop\\complete-jarvis\\Data.txt",'rt')
time = extracted_time.read()
Time = str(time)


deleted_time = open("C:\\Users\\user\\Desktop\\complete-jarvis\\Data.txt",'r+')
deleted_time.truncate(0) # it means that in file thwe remaining word will be equal to the parameter(0 here)
deleted_time.close()

print(Time)

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

RingerNow(Time)
