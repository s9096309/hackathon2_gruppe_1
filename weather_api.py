import requests

API_KEY = "d99eeffdfe41fc93fc4279e8e5c1ce6d"  # Setze hier deinen API-Schlüssel ein
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

stadt = input("What is your location? ").strip()

params = {"q": stadt, "appid": API_KEY, "units": "metric"}
response = requests.get(BASE_URL, params=params)

# API-Antwort ausgeben
print("API-Antwort:", response.status_code, response.text)

if response.status_code == 200:
    data = response.json()
    wetter = data["weather"][0]["description"]
    temperatur = data["main"]["temp"]
    print(f"The weather in {stadt}: {wetter}, {temperatur}°C")
else:
    print("Fehler: Ort nicht gefunden oder API-Anfrage fehlgeschlagen.")
