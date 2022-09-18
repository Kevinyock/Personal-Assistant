import pyfiglet
from gtts import gTTS
from playsound import playsound 

figletFont = pyfiglet.Figlet()

def main():

    print(figletFont.renderText("Initializing"))
    print(figletFont.renderText("Primary"))
    print(figletFont.renderText("System"))

    assistantVoice = gTTS("Initializing Primary System")
    #assistantVoice.save

    return 0

if __name__ == "__main__":
    main()