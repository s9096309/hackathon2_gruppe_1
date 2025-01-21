import requests
import json
from weather_api import get_weather
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung

# API-Konfiguration
TEAM_NAME = "Die Wilden Wetterfrösche"
API_BASE_URL = "http://hackathons.masterschool.com:3030"
TEST_MODE = True  # Wenn True, werden keine SMS gesendet, sondern nur in der Konsole ausgegeben

# Set zur Speicherung von verarbeiteten Nachrichten
verarbeitete_nachrichten = set()


def greeting(phone_number):
    """
    Sendet eine Begrüßungsnachricht.
    """
    nachricht = "Hallo, wie lautet dein Standort?"
    if TEST_MODE:
        print(f"[TEST_MODE] SMS an {phone_number}: {nachricht}")
    else:
        response = requests.post(
            f"{API_BASE_URL}/sms/send",
            json={"phoneNumber": phone_number, "teamName": TEAM_NAME, "message": nachricht},
        )
        if response.status_code == 200:
            print(f"Nachricht erfolgreich gesendet an {phone_number}.")
        else:
            print(f"Fehler beim Senden der Nachricht: {response.status_code}, {response.text}")


def abrufe_nachrichten():
    """
    Holt eingehende Nachrichten von der Masterschool API.
    """
    response = requests.get(f"{API_BASE_URL}/team/getMessages/{TEAM_NAME}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler beim Abrufen der Nachrichten: {response.status_code}, {response.text}")
        return {}


def finde_stadt_in_nachricht(nachricht, staedte_liste):
    """
    Prüft, ob eine Stadt aus der Liste in der Nachricht vorkommt.
    """
    for stadt in staedte_liste:
        if stadt.lower() in nachricht.lower():
            return stadt
    return None


def sende_sms(empfaenger, nachricht):
    """
    Sendet eine SMS über die Masterschool API.
    """
    if TEST_MODE:
        print(f"[TEST_MODE] SMS an {empfaenger}: {nachricht}")
    else:
        response = requests.post(
            f"{API_BASE_URL}/sms/send",
            json={"phoneNumber": empfaenger, "teamName": TEAM_NAME, "message": nachricht},
        )
        if response.status_code == 200:
            print(f"Nachricht erfolgreich gesendet an {empfaenger}.")
        else:
            print(f"Fehler beim Senden der Nachricht: {response.status_code}, {response.text}")


def verarbeite_nachrichten():
    """
    Verarbeitet alle eingehenden Nachrichten und sendet Antworten mit Wetterdaten und Musikempfehlung.
    """
    # Lade die Städte aus der JSON-Datei
    with open("city.list.json", "r", encoding="utf-8") as file:
        staedte_liste = [city["name"].lower() for city in json.load(file)]

    # Nachrichten einmalig abrufen (kein Loop!)
    nachrichten = abrufe_nachrichten()

    for phone_number, msgs in nachrichten.items():
        for msg in msgs:
            nachricht = msg["text"]
            received_at = msg["receivedAt"]

            # Eindeutigen Identifier für die Nachricht erstellen
            nachrichten_identifier = f"{phone_number}_{nachricht}_{received_at}"

            # Überspringe verarbeitete Nachrichten
            if nachrichten_identifier in verarbeitete_nachrichten:
                continue

            print(f"Neue Nachricht erhalten von {phone_number}: {nachricht}")
            verarbeitete_nachrichten.add(nachrichten_identifier)

            # Stadt in der Nachricht finden
            stadt = finde_stadt_in_nachricht(nachricht, staedte_liste)
            if stadt:
                # Wetterdaten abrufen
                temperature, weather_condition = get_weather(stadt)
                if temperature is not None and weather_condition is not None:
                    # Temperatur und Wetterbedingungen analysieren
                    temp_kategorie = kategorisiere_temperatur(temperature)
                    wetter_kategorie = analysiere_wetter(weather_condition)

                    # Musikempfehlung erstellen
                    musik_link = gib_musikempfehlung(temp_kategorie, wetter_kategorie)

                    # Antwortnachricht erstellen
                    antwort = (
                        f"Wetterbericht für {stadt}: {temperature}°C, {weather_condition}. "
                        f"Musikempfehlung: {musik_link}"
                    )
                else:
                    antwort = f"Fehler beim Abrufen des Wetters für {stadt}. Bitte überprüfe den Standort."
            else:
                antwort = "Deine Stadt konnte nicht gefunden werden. Bitte überprüfe die Eingabe."

            # Antwort-SMS senden
            sende_sms(phone_number, antwort)


if __name__ == "__main__":
    ask_phone_number = input("Geben Sie Ihre Handynummer ein: ")
    greeting(ask_phone_number)

    # Verarbeite Nachrichten (einmalige Verarbeitung)
    verarbeite_nachrichten()
