import RPi.GPIO as GPIO
import time
import requests
import json
import datetime


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(17, GPIO.OUT)        #light output pin
GPIO.setup(4, GPIO.OUT)         #fan output pin
while True:
    i=GPIO.input(27)
    if i==0:                 #When output from motion sensor is LOW
        print("No Motion:"+str(i))
        GPIO.output(17, 1)  #Turn OFF LED
        GPIO.output(4, 1)
        time.sleep(1)
    elif i==1:               #When output from motion sensor is HIGH
        print("Motion detected: "+str(i))
        GPIO.output(17, 0)  #Turn ON LED
        GPIO.output(4, 0)
        time.sleep(300)


def get_sunrise_sunset_data():
    response = requests.get("https://api.sunrise-sunset.org/json?lat=9.970003&lng=76.306827")
    data = json.loads(response.content)
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_object = datetime.datetime.strptime(sunrise,'%I:%M:%S %p') + datetime.timedelta(hours=5,minutes=30)
    sunset_object = datetime.datetime.strptime(sunset,'%I:%M:%S %p') + datetime.timedelta(hours=5,minutes=30)
    db = open("pir.db","r")
    db.write(json.dumps({
        "timestamp": datetime.datetime.now(),
        "sunrise":{
            "hr":sunrise_object.hour,
            "min":sunrise_object.minute,
            "sec":sunrise_object.second
        },
        "sunset":{
            "hr":sunrise_object.hour,
            "min":sunrise_object.minute,
            "sec":sunrise_object.second
        }
    }))
    db.close()
    return sunrise_object, sunset_object

def isSunset():
    data = json.loads(open("pir.db","r").read())

    sunrise_hr = data['sunrise']['hr']
    sunrise_min = data['sunrise']['min']
    sunrise_sec = data['sunrise']['sec']

    sunset_hr = data['sunset']['hr']
    sunset_min = data['sunset']['min']
    sunset_sec = data['sunset']['sec']

    now = datetime.datetime.now()

if now.hour >= sunset_hr and now.hour <= sunset_hr:
    if now.min >= sunset_min and now.min <= sunset_min:
        if now.sec >= sunset_sec and now.sec <= sunset_sec:
            print(True)
    return False