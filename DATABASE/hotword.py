import os
import speech_recognition as sr

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

def wakeup():
    while True:

        wake_up=listen()
        print('listening')
        if 'wakeup' in wake_up:
            os.startfile('C:\\Users\\hp\\OneDrive\\Desktop\\AI\\AI.py')
        
        else:
            print('.......')



wakeup()