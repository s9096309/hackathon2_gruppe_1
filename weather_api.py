import requests
import os
from dotenv import load_dotenv

# Lade die .env Datei
load_dotenv()

# Hole den API-Key aus der .env Datei
API_KEY = os.getenv("API_KEY")

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

# Standort vom Benutzer abfragen
#location = input("Gib deinen Standort ein: ")

# Wetterdaten abrufen und anzeigen
def get_and_print_weather_data(location):
    temperature, weather_condition = get_weather(location)
    if temperature is not None and weather_condition is not None:
        print(f"Wetter für {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wetterbedingungen: {weather_condition}")
    else:
        print("Fehler beim Abrufen des Wetters. Bitte überprüfe den Standort.")
