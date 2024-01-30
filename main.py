import pyttsx3 as tts
import wikipedia as wiki
import math

voice = 0
engine = tts.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def mainMenu():
    c_input = input("1. Press 1 to change volume\n2. Press 2 to change voice\nEnter your search Topic: ")
    api_input = c_input.lower().strip()
    return api_input


def program():
    api_input = mainMenu()
    if api_input != "exit" and api_input != "exit!" and api_input != "quit" and api_input != "quit!":
        if api_input == "1":
            while True:
                volume_level = int(input("Enter a volume level between 1 to 100: "))
                if volume_level<0:
                    volume_level = 0
                elif volume_level>100:
                    volume_level = 100
                volume_level = math.ceil(volume_level)
                engine.setProperty('volume',volume_level/100)
                speak("I'm hoping this is not too loud or too feable")
                volume_level_approval = input("Please confirm if the above volume level is alright(Y or n): ")
                volume_level_approval = volume_level_approval.lower().strip()
                if volume_level_approval == "y" or volume_level_approval == "yes":
                    program()
        if api_input == "2":
            while True:
                voice_switch_approval = input("Do you want to swith Voice(Y or n): ")
                voice_switch_approval = voice_switch_approval.lower().strip()
                global voice
                if voice == 0: voice = 1 
                else: voice = 0  
                engine.setProperty('voice', voices[voice].id)
                speak("Voices are amusing")
                if voice_switch_approval == "y" or voice_switch_approval == "yes":
                    program()
        print("Searching wikipedia...")
        speak("Searching wikipedia...")
        result = wiki.summary(api_input, sentences = 3)
        print(result)
        speak(result)
        program()
    else:
        speak("Okay! Closing")
        exit(1)
    

if __name__ == "__main__":
    speak("Hello WikiBot")
    program()