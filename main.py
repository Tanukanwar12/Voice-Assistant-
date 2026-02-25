import speech_recognition as sr
import webbrowser
import musiclibrary
import pyttsx3
import time

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        song = " ".join(c.split(" ")[1:])
        if song in musiclibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musiclibrary.music[song])
        else:
            speak("Sorry, song not found")

if __name__ == "__main__":
    speak("Initializing Peter")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        while True:
            try:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
                word = r.recognize_google(audio)
                print("You said:", word)

                if "peter" in word.lower():
                    speak("Yes?")
                    print("Peter active")

                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                speak("Sorry, I didn't understand")
            except Exception as e:
                print("Error:", e)
        
