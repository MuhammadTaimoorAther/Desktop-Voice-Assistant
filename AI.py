from multiprocessing.sharedctypes import Value
import wikipedia
import webbrowser
import os
import pyttsx3
import speech_recognition as  sr
import smtplib
import datetime
from types import coroutine
import pyttsx3
import speech_recognition as sr
from Automations import ChromeAuto, Speak, WindiowsAuto, YouTubeAuto
from Features import GoogleSearch, YouTubeSearch, temprature
from win10toast import ToastNotifier
import pywhatkit
from pywikihow import search_wikihow

name='Jarvis'    
def listen():


        r=sr.Recognizer()

        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold=2
            r.adjust_for_ambient_noise(source,1)
            audio=r.listen(source,0,2)

        try:

            print("Recognizing.....")
            query =r.recognize_google(audio,language="eng-in")
            print(f"you just said : {query}")

        except :
            print("please say it again sir ")
            query='none'

        query =str(query)
        return query.lower()

def say(Text):
        engine = pyttsx3.init("sapi5")
        Voices = engine.getProperty('voices')
        engine.setProperty('voice',Voices[3].id)
        engine.setProperty('rate', 170)
        print("       ")
        print (f"A.I : {Text}")
        engine.say(text=Text)
        engine.runAndWait()
        print("      ")

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            say("Good Morning!")

        elif hour>=12 and hour<18:
            say("Good Afternoon!")   

        else:
            say("Good Evening!")  

        say("I am your virtual assistant Sir. I'm here to help you")       

################################################################################################


def main_function():
        wishMe()
        while True:
            query = listen().lower()
            # Logic for executing tasks based on query
            if 'google search about' in query:
                Query = query.replace("google search about","")
                GoogleSearch(query)
            
            elif 'youtube search about' in query:
                Query = query.replace("jarvis","")
                query = Query.replace("youtube search","")
                from Features import YouTubeSearch
                YouTubeSearch(query)

            elif 'download this video' in query:
                from Features import DownloadYouTube
                DownloadYouTube()
                
            elif 'speed test' in query:
                from Features import SpeedTest
                SpeedTest()

            elif 'send message' in query:

                name = query.replace("send message ","")
                name = name.replace("send ","")
                name = name.replace("to ","")
                Name = str(name)
                say(f"Whats is The Message For {Name}")
                MSG = listen()
                say("message will be sent to : ")
                say(name)
                say("and The Message is : ")
                say(MSG)
                from Automations import WhatsappMsg
                WhatsappMsg(Name,MSG)

            elif 'call' in query:
                from Automations import WhatsappCall
                name = query.replace("call ","")
                name = name.replace("jarvis ","")
                Name = str(name)
                WhatsappCall(Name)

            elif 'show message' in query:
                say("With Whom sir ?")
                name = listen()
                say("ok sir opening whatsapp chat ")
                from Automations import WhatsappChat
                WhatsappChat(name)

            elif 'space news' in query:


                Speak("Tell Me The Date For News Extracting Process .")
                input(Value)
                #Date = list() 
                #from Features import DateConverter
                #Value = DateConverter(Date)
                from Nasa import NasaNews
                NasaNews(Value)

            if 'wikipedia ' in query:#done
                try:
                    say('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    say("According to Wikipedia : ")
                    say(results)
                except :
                    say("sorry sir, unable to find answer ")

            elif 'play music' in query:
                music_dir = 'E:\\SnapTube Audio'
                songs = os.listdir(music_dir)
                print(songs)

                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                say(f"Sir, the time is {strTime}")

            elif 'go to sleep' in query:
                say("ok sir going to sleep")
                exit()
            
            elif 'shutdown pc' in query:
                os.system("shutdown /s")

            elif 'chrome' in query:
                ChromeAuto(query)

            elif 'youtube' in query:
                YouTubeAuto(query)
            elif 'window' in query:
                WindiowsAuto(query)
            elif 'how to' in query:
                Speak('getting data from internet ')
                op=query.replace("jarvis","")
                max_result=1
                how_to_func=search_wikihow(op,max_result)
                assert len(how_to_func)==1
                #how_to_func[0].print()
                Speak(how_to_func[0].summary)

            elif 'temperature in' in query:
                query=query.replace("temperature in","")
                Speak('checking')
                temprature(query)
            elif 'reminder' in query:
                remembermsg=query.replace("reminder","")
                Speak("sir i want to remind that : "+{remembermsg})
                remember=open('data.txt','w')
                remember.write(remembermsg)
                remember.close()
            elif 'what do you remember' in query:
                remember=open('data.txt','r')
                Speak("you told me that : "+remember.read())
            

#say("hi there im your assistant")
main_function()
