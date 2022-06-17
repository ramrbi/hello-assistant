
from logging import shutdown
import pyautogui
import cv2
from click import command
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser as w
import pywhatkit
import flask
import pywintypes
import os
import qrcode
from qrcode import make
Listener=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
  engine.say(text)
  engine.runAndWait()



def take_command():
    with sr.Microphone() as source:
            print('listening...')
            voice = Listener.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()
    if "hello" in command:
       command=command.replace("hello","")

       return command
           
       
def run_red():
    command=take_command()
    print(command)
    if 'play'in command:
        song=command.replace('play',"")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif"time" in command:
        time=datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('time is'+time)
    elif 'wikipedia ' in command:
        thing=command.replace('wikipedia',' ')
        info=wikipedia.summary(thing,1)
        print(info)
        talk(info)
    elif 'youtube channel'in command:
        w.open('https://www.youtube.com/channel/UC5yaAk5MGP5kWXf4UOed3Kw')
        talk('opening your yt channel')
    elif 'twitter'in command:
        w.open("https://twitter.com/home")
        talk('opening twitter')
    elif 'youtube'in command:
        w.open('https://www.youtube.com')
        talk("opening youtube")
    elif 'insta' in command:
        w.open('https://www.instagram.com')
        talk('opening insta')
    elif 'replit'in command:
        w.open("https://replit.com/~")
        talk('opening replit')
    elif 'shutdown' in command:
        os.system("shutdown /s /t 1")
        talk('shutdowning')
    elif 'restart'in command:
         os.system("shutdown /r /t 1")
         talk("restarting")
    elif 'open' in command:
        app=command.replace('open',"")
        talk("opening"+app)
        os. system(app)

    
    elif 'who is your creator'in command:
        talk('its K ram santosh')
    elif 'what do you eat'in command:
        print('electricity and ram of your computer temporarily ')
        talk('electricity and ram of your computer temporarily ')
    elif 'whatsapp'in command:
        w.open('https://web.whatsapp.com')
    elif 'edit photos'in command:
        w.open('https://www.canva.com')
        talk('opening canva.com')
    elif 'edit videos' in command:
        os. system('wondershare flimora')
        talk('opening wonder share flimora')
    elif 'edit audio'in command:
        os. system('audacity')


    while "create qr" in command:
        talk('paste your link here')
        r=input("paste your link here:")
        img= qrcode.make(
            r
        )
        img.save("qrcode.png")
        img.show()
        break
    else:
        return None
    
        
run_red()