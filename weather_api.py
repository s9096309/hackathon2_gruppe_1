import requests

API_KEY = "d99eeffdfe41fc93fc4279e8e5c1ce6d"

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
location = input("Gib deinen Standort ein: ")

# Wetterdaten abrufen und anzeigen
temperature, weather_condition = get_weather(location)
if temperature is not None and weather_condition is not None:
    print(f"Wetter für {location}:")
    print(f"Temperature: {temperature}°C")
    print(f"Wetterbedingungen: {weather_condition}")
else:
    print("Fehler beim Abrufen des Wetters. Bitte überprüfe den Standort.")
