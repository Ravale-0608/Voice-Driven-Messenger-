import os
import time
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import subprocess


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

        while said != "bye":
            try:
                said = r.recognize_google(audio)
                speak(said)
            except Exception as e:
                print("Exception: " + str(e))
    return said


get_audio()