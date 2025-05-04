import webbrowser
import speech_recognition as sr
import datetime
import subprocess
import sys
import time
import re
import psutil
from feature.customvoice import speak
from feature.llama_for_Maggie import handle_convo

# Mode flag: True for type mode, False for voice mode
type_mode = False

def respond(text):
    """Speak or print based on mode."""
    if type_mode:
        print(f"🤖 Maggi: {text}")
    else:
        speak(text)

def choose_mode():
    global type_mode
    print("Choose your mode:")
    print("1. Voice mode")
    print("2. Type mode")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "2":
        type_mode = True
        respond("Switched to type mode. You can now type your commands.")
    else:
        type_mode = False
        respond("Switched to voice mode. You can now speak your commands.")

def take_command():
    global type_mode
    if type_mode:
        return input("⌨️ You: ").lower()
    else:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 0.6
            print("🎙️ Listening...")
            audio = r.listen(source)

            try:
                query = r.recognize_google(audio, language='en-in')
                print(f"🗣️ You said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                respond("Sorry, I didn't catch that.")
            except sr.RequestError as e:
                respond(f"Google service error: {e}")
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
            respond(f"Opening {name}")
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
            respond(f"Opening {name}")
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            try:
                subprocess.call([opener, f"/System/Applications/{path}"])
            except Exception:
                respond(f"Couldn't open {name}.")
            return True
    return False

def handle_ai_mode():
    respond("AI mode activated. How may I help you?")
    while True:
        print("🧠 LLaMA is listening...")
        query = take_command()
        if "exit llama" in query or "exit ai" in query or  "bye" in query :
            respond(handle_convo("bye"))
            break
        if query:
            result = handle_convo(query)
            respond(result)

def google_search(query):
    if "search" in query and "google" in query:
        search_term = query.split("search")[-1]
        search_term = re.sub(r"\bon google\b|\bin google\b", "", search_term).strip()
        if search_term:
            respond(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            respond("What should I search for?")

def check_battery():
    battery = psutil.sensors_battery()
    if battery:
        respond(f"Battery is at {battery.percent}%")
        respond("Your charger is plugged in." if battery.power_plugged else "Your charger is not plugged in.")
    else:
        respond("Battery status is not available.")

def set_timer(query):
    try:
        minutes = int(re.findall(r"\d+", query)[0])
        respond(f"Setting a timer for {minutes} minutes.")
        time.sleep(minutes * 60)
        respond("Time's up!")
    except Exception:
        respond("I couldn't set the timer.")

def report_time():
    now = datetime.datetime.now()
    respond(f"The time is {now.hour} hours and {now.minute} minutes.")

def show_help():
    help_text = """
    Maggi's Commands:
    1. 'Open <website name>' - Open a website (e.g., 'Open YouTube').
    2. 'Open <application name>' - Open a system application (e.g., 'Open Music').
    3. 'Search <query> on Google' - Search a term on Google.
    4. 'Set a timer for <minutes>' - Set a timer.
    5. 'Check battery' - Check battery status.
    6. 'The time' - Get the current time.
    7. 'Switch to type mode' - Switch to typing commands instead of speaking.
    8. 'Switch to voice mode' - Switch to voice commands.
    9. 'Invoke AI' - Activate the AI mode to interact with LLaMA.
    10. 'Help' - Show this help message.
    11. 'Exit' or 'Bye' - Exit the program.
    """
    respond(help_text)

if __name__ == "__main__":
    respond("Hello!")
    choose_mode()

    while True:
        query = take_command()
        if not query:
            continue

        if "bye maggi" in query or "exit" in query:
            respond("Goodbye!")
            break

        if "invoke ai" in query or "ai mode" in query:
            handle_ai_mode()
            continue

        if "switch to type mode" in query:
            type_mode = True
            respond("Switched to type mode.")
            continue

        if "switch to voice mode" in query:
            type_mode = False
            respond("Switched to voice mode.")
            continue

        if "help" in query:
            show_help()
            continue

        if open_website(query):
            continue

        if open_application(query):
            continue

        if "search" in query and "google" in query:
            google_search(query)
            continue

        if "the time" in query:
            report_time()
            continue

        if "set a timer for" in query:
            set_timer(query)
            continue

        if "battery" in query:
            check_battery()
            continue
