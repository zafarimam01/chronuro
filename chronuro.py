from features.youtube_feature import search_youtube
import speech_recognition as sr
from gtts import gTTS
from google import genai
import os
import re
from dotenv import load_dotenv
from features.datetime_feature import get_time, get_date, get_day, get_datetime
from features.weather_feature import get_weather

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def clean_text(text):
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'#+', '', text)
    text = re.sub(r'`+', '', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
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
            model="models/gemini-2.0-flash",
            contents=query
        )
        if response.text:
            return response.text
        return "Sorry sir, I could not understand the response."
    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry sir, Gemini is not responding right now."

def run_chronuro():
    speak("Hello Sir,How are You")
    while True:
        query = listen()

        if query == "":
            continue

        # exit
        elif "exit" in query or "bye" in query or "goodbye" in query:
            speak("Goodbye Sir, Chronuro going offline!")
            break

        # youtube
        elif "youtube" in query:
            search_term = query.replace("search youtube for", "").replace("play", "").replace("youtube", "").strip()
            speak(search_youtube(search_term))

        # everything else goes to Gemini — including time, date, weather questions
        else:
            # give Gemini context about current time and weather
            now_context = f"Current time is {get_time()}. Today is {get_date()}."
            full_query = f"{now_context}\n\nUser asked: {query}\n\nAnswer naturally and concisely like a voice assistant. No bullet points, no markdown."
            reply = ask_gemini(full_query)
            speak(reply)

if __name__ == "__main__":
    run_chronuro()

    