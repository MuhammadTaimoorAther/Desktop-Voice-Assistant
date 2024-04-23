import requests
#import cartopy.crs as ccrs 
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

Api_Key = "KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"

def NasaNews(Date):

    Speak("Extracting Data From Nasa API. ")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params = {'date':str(Date)}
    r = requests.get(Url,params = Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)
    Path_1 = "C:\\Users\\hp\\OneDrive\\Desktop\\AI\\" + str(FileName)
    img = Image.open(Path_1)
    img.show()
    Speak(f"Heading or title of the news is : {Title}")
    Speak(f"According To Nasa : {Info}")
