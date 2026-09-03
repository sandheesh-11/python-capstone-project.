import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

def assistant():
    speak("Hello! I am your voice controlled virtual assistant.")
    speak("How can I help you?")

    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! How are you?")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + time)

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + date)

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                speak("Searching for " + query)
                webbrowser.open(
                    "https://www.google.com/search?q=" + query.replace(" ", "+")
                )

        elif "exit" in command or "stop" in command or "goodbye" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I don't know that command yet.")

assistant()
