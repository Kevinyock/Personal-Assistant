# Import Libraries
import pyfiglet
from gtts import gTTS
import playsound
import speech_recognition as sr
import pyaudio

# Personal Modules
import InternetVerify
import FacialRecognition

class PersonalAssistant():
    def __init__(self):
        self.speechRecogition = sr.Recognizer()
        self.figletFont = pyfiglet.Figlet()
        self.playsound = playsound
        self.assistantInitlization()
        self.internetVerification = InternetVerify.InternetConnection()
        self.internetVerification.IsGoogleDown()
        self.facialRecognition = FacialRecognition.FacialRecognition()
    
    def assistantInitlization(self):
    
        print(self.figletFont.renderText("Initializing"))
        print(self.figletFont.renderText("Primary"))
        print(self.figletFont.renderText("System"))

        assistantVoice = gTTS("Initializing Primary System")
        assistantVoice.save("Audio/initialization.mp3")
        self.playsound.playsound("Audio/initialization.mp3")


