import requests
import os
from dotenv import load_dotenv

# Lade die .env Datei
load_dotenv()

# Hole den API-Key aus der .env Datei
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY nicht gefunden. Bitte überprüfe die .env Datei.")

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
    elif response.status_code == 401:
        print("Ungültiger API-Schlüssel. Bitte überprüfe deine .env Datei.")
    elif response.status_code == 404:
        print("Standort nicht gefunden. Bitte überprüfe die Eingabe.")
    else:
        print(f"Fehler beim Abrufen der Wetterdaten: {response.status_code}")
    return None, None

# Standort vom Benutzer abfragen
location = input("Gib deinen Standort ein: ").strip()

if location:
    # Wetterdaten abrufen und anzeigen
    temperature, weather_condition = get_weather(location)
    if temperature is not None and weather_condition is not None:
        print(f"Wetter für {location}:")
        print(f"Temperatur: {temperature}°C")
        print(f"Wetterbedingungen: {weather_condition}")
    else:
        print("Fehler beim Abrufen des Wetters. Bitte überprüfe den Standort.")
else:
    print("Bitte einen gültigen Standort eingeben.")
