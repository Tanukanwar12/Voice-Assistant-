import speech_recognition as sr
import webbrowser
import musiclibrary
import pyttsx3
import time

recognizer=sr.Recognizer()
engine=pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait() 
        time.sleep(0.3)
    except Exception as e:
        print("speaking error:",e)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ")
        if len(parts) > 1:
           song = parts[1]
           if song in musiclibrary.music:
               link = musiclibrary.music[song]
               speak(f"playing{song}")
               webbrowser.open(link)
           else:
               print("Sorry, song not found.")
        else:
               print("Please say the song name.")
       

if __name__ == "__main__":
    speak("intializing peter....")
    while True:
        # Listen for the wake word "peter"
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source ,timeout=5,phrase_time_limit=4)
            word=r.recognize_google(audio)
            print("you said:",word)
            if "peter" in word.lower():
                print("wake word detected")
                
                #listen for command
                with sr.Microphone() as source:
                    print("peter active....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
                    engine.runAndWait()
        
        except Exception as e:
            print("Error; {0}".format(e))


     
