from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
#from notifypy import Notify
import pyttsx3
import speech_recognition as sr
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def WhatsappMsg(name,message):
     
    startfile("C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=271, y=112)

    sleep(1)

    write(name)

    sleep(1)

    click(x=229, y=274)

    sleep(1)

    click(x=594, y=694)

    sleep(1)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=271, y=112)

    sleep(1)

    write(name)

    sleep(1)

    click(x=229, y=274)

    sleep(1)

    click(x=594, y=694)

    sleep(1)

    click(x=1216, y=65)

def WhatsappChat(name):

    startfile("C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=271, y=112)

    sleep(1)

    write(name)

    sleep(1)

    click(x=229, y=274)

    sleep(1)

    click(x=594, y=694)

    sleep(1)

def ChromeAuto(command):

    query = str(command)

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:

        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:
        tab = query.replace("switch tab ", "")
        Tab = tab.replace("to","")
        
        num = Tab

        bb = f'ctrl + {num}'

        press_and_release(bb)

    elif 'open' in query:

        name = query.replace("chrome open ","")

        NameA = str(name)

        if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:

            web.open("https://www.instagram.com/")

        else:

            string = "https://www." + NameA + ".com"

            string_2 = string.replace(" ","")

            web.open(string_2)

def YouTubeAuto(command):

    query = str(command)

    if 'pause' in query:
        Speak("ok sir pausing")
        press('space bar')

    elif 'resume' in query:
        Speak("ok sir resuming")
        press('space bar')

    elif 'full screen' in query:
        Speak("ok sir going full screen")
        press('f')

    elif 'film screen' in query:
        Speak("ok sir going film screen")
        press('t')

    elif 'skip' in query:
        Speak("ok sir skipping add")
        press('tab + shift + Enter')

    elif 'back' in query:
        Speak("ok sir going on last tab")
        press('j')

    elif 'increase' in query:
        Speak("ok sir increasing volume")
        press_and_release('SHIFT + .')

    elif 'decrease' in query:
        Speak("ok sir decreasing volume")
        press_and_release('SHIFT + ,')

    elif 'previous' in query:
        Speak("ok sir playing previous")
        press_and_release('SHIFT + p')

    elif 'next' in query:
        Speak("ok sir playing next")
        press_and_release('SHIFT + n')
    
    elif 'search' in query:
        Speak("ok sir")
        click(x=667, y=146)

        Speak("What To Search Sir ?")

        search = TakeCommand()

        write(search)

        sleep(0.8)

        press('enter')

    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')

    elif 'my channel' in query:

        web.open("https://www.youtube.com/channel/UC7A5u12yVIZaCO_uXnNhc5g")

    else:
        Speak("No Command Found!")

def WindiowsAuto(command):

    query = str(command)

    if 'home screen' in query:

        press_and_release('windows + m')

    elif 'minimize' in query:

        press_and_release('windows + m')

    elif 'show start' in query:

        press('windows')

    elif 'open setting' in query:

        press_and_release('windows + i')

    elif 'open search' in query:

        press_and_release('windows + s')

    elif 'screen shot' in query:

        press_and_release('windows + SHIFT + s')

    elif 'restore windows' in  query:

        press_and_release('Windows + Shift + M')

    else:
        Speak("Sorry , No Command Found!")
