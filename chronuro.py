import speech_recognition as sr
from gtts import gTTS
from google import genai
import os
from config import GEMINI_API_KEY
from features.datetime_feature import get_time, get_date, get_day, get_datetime

# Setup Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

import re

def clean_text(text):
    text = re.sub(r'\*+', '', text)   # remove *
    text = re.sub(r'#+', '', text)    # remove #
    text = re.sub(r'`+', '', text)    # remove `
    text = re.sub(r'\n+', ' ', text)  # remove newlines
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    return text.strip()

def speak(text):
    clean = clean_text(text)
    print(f"Chronuro: {clean}")
    tts = gTTS(text=clean, lang='en', slow=False)
    tts.save("response.mp3")
    os.system("afplay response.mp3 -r 1.2")
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}")
        return query.lower()
    except:
        return ""

def ask_gemini(query):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry sir, Gemini is currently unavailable."
    
def run_chronuro():
    speak("Hello Sir, I am Chronuro, How Can I Help You")
    while True:
        query = listen()

        if query == "":
            continue

        elif "time" in query:
            speak(get_time())

        elif "date" in query:
            speak(get_date())

        elif "day" in query:
            speak(get_day())

        elif "what's today" in query or "whats today" in query:
            speak(get_datetime())

        elif "exit" in query or "bye" in query:
            speak("Goodbye Sir, Chronuro going offline!")
            break

        else:
            reply = ask_gemini(query)
            speak(reply)

if __name__ == "__main__":
    run_chronuro()