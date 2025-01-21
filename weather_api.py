import requests
from dotenv import load_dotenv
import os

# .env-Datei laden
load_dotenv()

# API-Key abrufen
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API-Key konnte nicht geladen werden. Überprüfe die .env-Datei!")

def get_weather(location):
    """
    Holt das Wetter für den angegebenen Standort.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        weather_condition = weather_data["weather"][0]["description"]
        return temperature, weather_condition
    else:
        return None, None
