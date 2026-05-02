import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city="Abu"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            city_name = data["name"]

            return f"Sir, the weather in {city_name} is {condition}. Temperature is {temp} degrees celsius, feels like {feels_like} degrees, and humidity is {humidity} percent."
        else:
            return "Sorry Sir, I could not find the weather for that city."

    except Exception as e:
        print("Weather Error:", e)
        return "Sorry Sir, I could not fetch the weather right now."