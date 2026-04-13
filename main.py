import speech_recognition as sr
import webbrowser
import musiclibrary
import pyttsx3
import time
import threading

r = sr.Recognizer()

command_mode = threading.Event()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    c = c.lower().strip()
    print(f"Processing: '{c}'")

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
        song = " ".join(c.split()[1:]).strip()
        print(f"Song requested: '{song}'")

        if song in musiclibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musiclibrary.music[song])
        else:
            found = False
            for key in musiclibrary.music:
                if key in song or song in key:
                    speak(f"Playing {key}")
                    webbrowser.open(musiclibrary.music[key])
                    found = True
                    break
            if not found:
                speak("Sorry, song not found")
    else:
        speak("Sorry, I don't know that command")

def wake_word_listener():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.3)
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                word = r.recognize_google(audio)
                print("Heard:", word)

                if "peter" in word.lower():
                    speak("Yes?")
                    command_mode.set() 

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            pass
        except Exception as e:
            print("Wake word error:", e)

def command_listener():
    while True:
        command_mode.wait()  
        command_mode.clear()

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Command mode ON — listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=6)
                command = r.recognize_google(audio)
                print("Command:", command)
                processCommand(command)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except Exception as e:
            print("Command error:", e)

if __name__ == "__main__":
    speak("Initializing Peter")

    t1 = threading.Thread(target=wake_word_listener, daemon=True)
    t2 = threading.Thread(target=command_listener, daemon=True)

    t1.start()
    t2.start()

    while True:
        time.sleep(1)
        
