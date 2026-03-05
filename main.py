# Import necessary libraries
# pip install SpeechRecognition
# pip install pyttsx3
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take a voice command from the user
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Network error.")
        return None

    return command.lower()

# Function to respond to different commands
def respond(command):
    if 'hello' in command or 'hi' in command:
        speak("Hello! How can I assist you today?")

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif 'search' in command:
        speak("What would you like to search for?")
        search_query = take_command()
        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif 'open' in command:
        if 'safari' in command:
            speak("Opening Safari")
            os.system("open -a Safari")
        elif 'calculator' in command:
            speak("Opening Calculator")
            os.system("open -a Calculator")

    elif 'bye' in command or 'exit' in command or 'quit' in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("I'm sorry, I don't know that command.")

# Main function to run the assistant
def run_assistant():
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        command = take_command()
        if command:
            respond(command)

# Start the assistant
run_assistant()