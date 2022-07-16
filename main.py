import os
import time
import pyaudio
import datetime
import speech_recognition as sr
from gtts import gTTS
import subprocess
import pywhatkit
now = datetime.datetime.now()



def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    subprocess.call(['say', text])

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))
    return said


contacts = {'brother': '+15714885819', 'amna': '+15716396640', 'mom': '+15878909324', 'dad': '+923008466642'
            }
speak("Nice to meet you. My name is Alfred!")
text = get_audio()
if 'message' in text:
    speak("Who do you want to send a message to?")
    text = get_audio()
    speak("What is your message?")
    msg = get_audio()
    for contact in contacts:
        if contact in text:
            speak("Messaging "+str(contact))
            num = contacts[contact]
            hour = now.hour
            minute = now.minute
            pywhatkit.sendwhatmsg(num, msg, hour, minute+2)
            speak("Message successfully sent")