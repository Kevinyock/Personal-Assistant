# Import Libraries
import pyfiglet
from gtts import gTTS
import playsound
import speech_recognition as sr
import pyaudio
import os

# Personal Modules
import internetVerify
import FacialRecognition
import voiceRecogition

class PersonalAssistant():
    def __init__(self):
        self.speechRecogition = sr.Recognizer()
        self.figletFont = pyfiglet.Figlet()
        self.playsound = playsound
        self.assistantInitlization()
        self.internetVerification = internetVerify.InternetConnection()
        self.voiceRecogition = voiceRecogition.VoiceRecogition()
        self.facialRecognition = facialRecognition.FacialRecognition()
    
    def assistantInitlization(self):
    
        print(self.figletFont.renderText("Initializing"))
        print(self.figletFont.renderText("Primary"))
        print(self.figletFont.renderText("System"))

        assistantVoice = gTTS("Initializing Primary System")

        if not os.path.isfile("Audio/initialization.mp3"):
            assistantVoice.save("Audio/initialization.mp3")

        self.playsound.playsound("Audio/initialization.mp3")


