
from bs4 import BeautifulSoup
import googlesearch
from matplotlib.font_manager import get_fontconfig_fonts
from matplotlib.pyplot import text
import pywhatkit
from torch import classes
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import pyttsx3
from time import sleep
import requests

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
def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")
    writeab = str(query)
    oooooo = open('C:\\Users\\hp\\OneDrive\\Desktop\\AI\\DATABASE\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()
    Query = str(term)
    pywhatkit.search(Query)
    search = wikipedia.summary(Query,2)
    Speak(f": According To Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=558,y=55)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('C:\\Users\\hp\\OneDrive\\Desktop\\AI\\DATABASE\\downloads')
    Speak("downloading has started")
    try:
        Download(Link)
        Speak("Download complete , I Have Downloaded The Video .")
        Speak("folder where file is downloaded will open now") 
        os.startfile('C:\\Users\\hp\\OneDrive\\Desktop\\AI\\DATABASE\\downloads')
    except:
        Speak("video cann not be downloaded sir ")

def temprature(query):

    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+query
    html = requests.get(url).content
    
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    
    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    
    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]
    
    # printing all data
    Speak("Temperature is " +temp)
    Speak("Time is : " + time)
    Speak("Sky Description is : " + sky)
    Speak(other_data)

