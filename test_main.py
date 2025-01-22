import requests
from weather_api import get_weather
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung

TEAM_NAME = "Die Wilden Wetterfrösche"
API_BASE_URL = "http://hackathons.masterschool.com:3030"

def get_location():
    return input("Gib deinen Standort ein: ")

def send_sms(location, temperature, weather_condition, musik_link):
    phone_number = "491771786208"
    message = f"Wetterbericht für {location}: {temperature}°C, {weather_condition}. Musikempfehlung: {musik_link}"
    response = requests.post(
        f"{API_BASE_URL}/sms/send",
        json={"phoneNumber": phone_number, "teamName": TEAM_NAME, "message": message}
    )
    if response.status_code == 200:
        print("Nachricht erfolgreich gesendet!")
    else:
        print(f"Fehler beim Senden der Nachricht: {response.status_code}")

def fetch_team_messages():
    response = requests.get(f"{API_BASE_URL}/team/getMessages/{TEAM_NAME}")
    if response.status_code == 200:
        messages = response.json()
        for phone_number, msgs in messages.items():
            print(f"Nachrichten von {phone_number}:")
            for message in msgs:
                print(f"  - {message['text']} (Empfangen um {message['receivedAt']})")
    else:
        print(f"Fehler beim Abrufen der Team-Nachrichten: {response.status_code}")

def main():
    location = get_location()
    temperature, weather_condition = get_weather(location)

    if temperature is not None and weather_condition is not None:
        temp_kategorie = kategorisiere_temperatur(temperature)
        wetter_kategorie = analysiere_wetter(weather_condition)
        musik_link = gib_musikempfehlung(temp_kategorie, wetter_kategorie)

        print(f"Wetter für {location}: {temperature}°C, {weather_condition}")
        print(f"Musikempfehlung: {musik_link}")

        send_sms(location, temperature, weather_condition, musik_link)
        fetch_team_messages()
    else:
        print(f"Fehler beim Abrufen des Wetters für {location}.")

if __name__ == "__main__":
    main()
