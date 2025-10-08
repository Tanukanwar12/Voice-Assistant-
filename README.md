 Peter — Voice Assistant

A lightweight voice-activated assistant written in Python. Uses SpeechRecognition for speech-to-text and pyttsx3 for text-to-speech. The project includes a tiny musiclibrary.py to map song names to YouTube links and a simple command processor to open websites and play songs.


---

Features

Wake-word activation ( "Peter")

Open websites (Google, YouTube, Facebook, LinkedIn)

Play songs defined in musiclibrary.py

Simple, easy-to-modify command processor

Minimal, single-file setup (plus musiclibrary.py)



---

Prerequisites

Python 3.8 or newer

A working microphone

Internet connection (for Google speech API; optional offline models available)


Required Python packages

pip install SpeechRecognition pyttsx3 pyaudio
# On Windows, if pip install pyaudio fails, try:
# pip install pipwin
# pipwin install pyaudio

# Optional (offline speech recognition):
# pip install vosk

> On Windows also run:

pip install pywin32




---

File structure (example)

Jarvis-Voice-Assistant/
├─ main.py (or peter_ai.py)
├─ musiclibrary.py
├─ README.md
└─ .gitignore

Example musiclibrary.py

music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shapeofyou": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
}


---

Installation

1. Clone or upload the repository to your machine (or create files manually).


2. (Recommended) Create a virtual environment and activate it:



python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

3. Install dependencies:



pip install -r requirements.txt
# or
pip install SpeechRecognition pyttsx3 pyaudio

4. Make sure main.py and musiclibrary.py are in the same folder.




---

Usage

1. Open terminal in the project folder.


2. Run:



python main.py
# or
python peter_ai.py

3. The assistant will say "Initializing Peter..." (or similar). When it prints Listening..., speak clearly.


4. Say the wake word (e.g., "Peter", "Jarvis"). After that you can say commands like:



"open youtube"

"play believer"

"open google"

"stop" (to exit)



---

Example commands handled by default

open google — opens https://google.com

open youtube — opens https://youtube.com

open facebook — opens https://facebook.com

open linkedin — opens https://linkedin.com

play <song> — plays a song if entry exists in musiclibrary.music


When a song is not found, the assistant should speak (or print) Sorry, song not found.


---

Troubleshooting

No module named musiclibrary

Ensure musiclibrary.py is in the same directory as your main script.

Confirm file name is exactly musiclibrary.py (not musiclibrary.py.txt).


pyttsx3 works in terminal but not inside the program

Initialize pyttsx3 only once at top-level:


engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

Then use a simple speak() wrapper:


def speak(text):
    engine.say(text)
    engine.runAndWait()

If TTS is sometimes skipped when microphone just released, add a small delay before speaking:


time.sleep(0.5)
speak("ya")

Listening timeout: Listening timed out while waiting for phrase to start

Increase timeouts when calling r.listen():


audio = r.listen(source, timeout=5, phrase_time_limit=4)

Or catch sr.WaitTimeoutError and continue to avoid error spam.


Installing PyAudio on Windows

If pip install pyaudio fails, use pipwin:


pip install pipwin
pipwin install pyaudio

If voice is muted or not playing

Check Windows Sound settings → App volume & device preferences → ensure Python / VS Code is allowed to output to speakers.

Try running the simple test:


python -c "import pyttsx3; e=pyttsx3.init(); e.say('test'); e.runAndWait()"


---

Customization

Change the wake word list or add more flexible matching in the main loop.

Add more commands to processCommand().

Expand musiclibrary.py with more songs or connect to an external API for dynamic search.



---

Contributing

Contributions welcome. Make sure to:

Fork the repo

Create a feature branch

Open a pull request with clear description of changes



---


