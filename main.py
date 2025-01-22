import requests
from weather_api import get_weather
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung

TEAM_NAME = "Die Wilden Wetterfrösche"
API_BASE_URL = "http://hackathons.masterschool.com:3030"

# Gib den Standort ein
location = input("Gib deinen Standort ein: ")

# Wetter abfragen
temperature, weather_condition = get_weather(location)

if temperature is not None and weather_condition is not None:
    # Temperatur- und Wetterbedingungen kategorisieren
    temp_kategorie = kategorisiere_temperatur(temperature)
    wetter_kategorie = analysiere_wetter(weather_condition)

    # Musikempfehlungen basierend auf Wetter und Temperatur
    musik_link = gib_musikempfehlung(temp_kategorie, wetter_kategorie)

    print(f"Wetter für {location}:")
    print(f"Temperature: {temperature}°C")
    print(f"Wetterbedingungen: {weather_condition}")

    print(f"Für {location} hast du folgende Musikempfehlung:")
    print(musik_link)

    # SMS senden (Beispiel-Nummer)
    phone_number = input("Bitte geben sie ihre Telefonnummer an")
    message = f"Wetterbericht für {location}: {temperature}°C, {weather_condition}. Musikempfehlung: {musik_link}"

    """response = requests.post(
        f"{API_BASE_URL}/sms/send",
        json={"phoneNumber": phone_number, "teamName": TEAM_NAME, "message": message}
    )

    if response.status_code == 200:
        print("Nachricht erfolgreich gesendet!")
    else:
        print(f"Fehler beim Senden der Nachricht: {response.status_code}")

    # Team-Nachrichten abrufen
    response = requests.get(f"{API_BASE_URL}/team/getMessages/{TEAM_NAME}")
    if response.status_code == 200:
        messages = response.json()
        for phone_number, msgs in messages.items():
            print(f"Nachrichten von {phone_number}:")
            for message in msgs:
                print(f"  - {message['text']} (Empfangen um {message['receivedAt']})")
    else:
        print(f"Fehler beim Abrufen der Team-Nachrichten: {response.status_code}")

else:
    print(f"Fehler beim Abrufen des Wetters für {location}.")
"""