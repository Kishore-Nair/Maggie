import webbrowser
import speech_recognition as sr
import datetime
import subprocess
import sys
import time
import re
import psutil
import random
import os
import requests

from feature.customvoice import speak
from feature.llama_for_Maggie import handle_convo

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        print("🎙️ Listening...")
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"🗣️ User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            speak(f"Google service error: {e}")
        return ""

def open_website(query):
    websites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "facebook": "https://facebook.com",
        "twitter": "https://twitter.com",
        "instagram": "https://instagram.com",
        "linkedin": "https://linkedin.com",
        "wikipedia": "https://wikipedia.org",
        "reddit": "https://reddit.com",
        "amazon": "https://amazon.com",
        "netflix": "https://netflix.com",
        "github": "https://github.com",
        "stack overflow": "https://stackoverflow.com",
        "pinterest": "https://pinterest.com",
        "tiktok": "https://tiktok.com",
        "quora": "https://quora.com"
    }

    for name, url in websites.items():
        if f"open {name}" in query:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return True
    return False

def open_application(query):
    apps = {
        "music": "Music.app",
        "safari": "Safari.app",
        "mail": "Mail.app",
        "photos": "Photos.app",
        "messages": "Messages.app",
        "calendar": "Calendar.app",
        "notes": "Notes.app",
        "reminders": "Reminders.app",
        "facetime": "FaceTime.app",
        "contacts": "Contacts.app",
        "maps": "Maps.app",
        "preview": "Preview.app",
        "finder": "Finder.app",
        "app store": "App Store.app",
        "system settings": "System Settings.app"
    }

    for name, path in apps.items():
        if f"open {name}" in query:
            speak(f"Opening {name}")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            try:
                subprocess.call([opener, f"/System/Applications/{path}"])
            except Exception:
                speak(f"Couldn't open {name}.")
            return True
    return False

def handle_ai_mode():
    speak("Done! How may I help you?")
    while True:
        query = take_command()
        if "exit llama" in query:
            speak(handle_convo("bye"))
            break
        if query:
            response = handle_convo(query)
            speak(response)

def google_search(query):
    search_term = re.sub(r"(search|on google|in google)", "", query).strip()
    if search_term:
        speak(f"Searching Google for {search_term}")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
    else:
        speak("What should I search for?")

def check_battery(_=None):
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery is at {battery.percent}%")
        if battery.power_plugged:
            speak("Charger is plugged in.")
        else:
            speak("Charger is not plugged in.")
    else:
        speak("Battery info not available.")

def set_timer(query):
    try:
        minutes = int(re.findall(r"\d+", query)[0])
        speak(f"Setting a timer for {minutes} minutes.")
        time.sleep(minutes * 60)
        speak("Time's up!")
    except:
        speak("I couldn't set the timer.")

def report_time(_=None):
    now = datetime.datetime.now()
    speak(f"The time is {now.hour} hours and {now.minute} minutes.")

def handle_help(_=None):
    help_text = (
        "You can say things like:\n"
        "- 'Open YouTube' or 'Open Safari'\n"
        "- 'Search cats on Google'\n"
        "- 'Set a timer for 2 minutes'\n"
        "- 'Check battery'\n"
        "- 'What time is it?'\n"
        "- 'Play music' or 'Take a note'\n"
        "- 'Tell a joke' or 'What's the weather?'\n"
        "- 'Invoke AI' for conversation\n"
        "- 'Bye Maggie' to exit"
    )
    speak(help_text)

def tell_joke(_=None):
    jokes = [
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why do Java developers wear glasses? Because they don’t C sharp.",
        "Why did the robot cross the road? Because it was programmed by a chicken!"
    ]
    speak(random.choice(jokes))

def tell_weather(_=None):
    try:
        res = requests.get("https://wttr.in/?format=3")
        speak(f"Weather: {res.text}")
    except:
        speak("Sorry, couldn't fetch the weather.")

def take_note(_=None):
    speak("What should I write?")
    note = take_command()
    if note:
        with open("notes.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note taken.")

def play_music(_=None):
    music_dir = os.path.expanduser("~/Music")
    try:
        songs = [song for song in os.listdir(music_dir) if song.endswith(".mp3")]
        if songs:
            song = random.choice(songs)
            os.system(f"open '{os.path.join(music_dir, song)}'")
            speak("Playing music")
        else:
            speak("No music files found.")
    except:
        speak("Music folder not accessible.")

# Routing keywords to functions
commands = [
    ("help", handle_help),
    ("joke", tell_joke),
    ("weather", tell_weather),
    ("note", take_note),
    ("play music", play_music),
    ("search", google_search),
    ("set a timer", set_timer),
    ("battery", check_battery),
    ("the time", report_time),
    ("invoke ai", handle_ai_mode)
]

if __name__ == "__main__":
    speak("Hi! I’m Maggie. You can ask me things like 'open YouTube', 'set a timer', or 'check battery'. Say 'help' to hear more.")
    print("🧠 Maggie is running...")

    while True:
        query = take_command()
        if not query:
            continue

        if "bye maggie" in query:
            speak("Goodbye!")
            break

        # High-priority commands
        if open_website(query):
            continue
        if open_application(query):
            continue

        matched = False
        for keyword, func in commands:
            if keyword in query:
                func(query)
                matched = True
                break

        if not matched:
            speak("Sorry, I didn't understand. Say 'help' to hear what I can do.")
