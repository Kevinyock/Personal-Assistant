# Import Libraries
import pyfiglet
from gtts import gTTS
from playsound import playsound 

figletFont = pyfiglet.Figlet()

def assistantInitlization():
    
    print(figletFont.renderText("Initializing"))
    print(figletFont.renderText("Primary"))
    print(figletFont.renderText("System"))

    assistantVoice = gTTS("Initializing Primary System")
    assistantVoice.save("Audio/initialization.mp3")
    playsound("Audio/initialization.mp3")

def main():
    assistantInitlization()

    return 0


if __name__ == "__main__":
    main()