import requests
import json
import time
from weather_api import get_weather  # Wetter-API
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung  # Analyse und Musikempfehlung

# API-Konfiguration
TEAM_NAME = "Die Wilden Wetterfrösche"
API_BASE_URL = "http://hackathons.masterschool.com:3030"
MASTERSCHOOL_SMS_NUMBER = "491771786208"  # Masterschool Nummer
VERARBEITETE_DATEI = "verarbeitete_nachrichten.json"  # Datei für persistente Speicherung

# Bereits verarbeitete Nachrichten laden
try:
    with open(VERARBEITETE_DATEI, "r", encoding="utf-8") as file:
        verarbeitete_nachrichten = set(json.load(file))
except FileNotFoundError:
    verarbeitete_nachrichten = set()


def speichere_verarbeitete_nachrichten():
    """
    Speichert die verarbeiteten Nachrichten in einer JSON-Datei.
    """
    with open(VERARBEITETE_DATEI, "w", encoding="utf-8") as file:
        json.dump(list(verarbeitete_nachrichten), file)


def sende_sms(empfaenger, nachricht):
    """
    Sendet eine SMS über die Masterschool API.
    """
    response = requests.post(
        f"{API_BASE_URL}/sms/send",
        json={"phoneNumber": empfaenger, "teamName": TEAM_NAME, "message": nachricht}
    )
    if response.status_code == 200:
        print(f"Nachricht erfolgreich gesendet an {empfaenger}.")
    else:
        print(f"Fehler beim Senden der Nachricht: {response.status_code}, {response.text}")


def abrufe_nachrichten():
    """
    Holt eingehende Nachrichten von der Masterschool API und speichert sie in einer Datei.
    """
    response = requests.get(f"{API_BASE_URL}/team/getMessages/{TEAM_NAME}")
    if response.status_code == 200:
        nachrichten = response.json()
        # Nachrichten in einer Datei speichern
        with open("nachrichten.json", "w", encoding="utf-8") as file:
            json.dump(nachrichten, file, indent=4, ensure_ascii=False)
        return nachrichten
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


def verarbeite_nachrichten():
    """
    Verarbeitet eingehende Nachrichten und sendet passende Antworten mit Wetterbericht und Musikempfehlung.
    """
    # Lade die Liste der Städte aus der JSON-Datei
    with open("city.list.json", "r", encoding="utf-8") as file:
        staedte_liste = [city["name"].lower() for city in json.load(file)]

    # Nachrichten abrufen
    nachrichten = abrufe_nachrichten()

    for phone_number, msgs in nachrichten.items():
        for msg in msgs:
            nachricht = msg["text"]
            received_at = msg["receivedAt"]

            # Eindeutigen Identifier für die Nachricht erstellen
            nachrichten_identifier = f"{phone_number}_{nachricht}_{received_at}"

            # Überspringe bereits verarbeitete Nachrichten
            if nachrichten_identifier in verarbeitete_nachrichten:
                continue

            verarbeitete_nachrichten.add(nachrichten_identifier)
            print(f"Neue Nachricht erhalten von {phone_number}: {nachricht}")

            # Stadt in der Nachricht finden
            stadt = finde_stadt_in_nachricht(nachricht, staedte_liste)
            if stadt:
                # Wetterdaten abrufen
                temperature, weather_condition = get_weather(stadt)
                if temperature is not None and weather_condition is not None:
                    # Analyse der Wetterdaten
                    temp_kategorie = kategorisiere_temperatur(temperature)
                    wetter_kategorie = analysiere_wetter(weather_condition)

                    # Musikempfehlung generieren
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

            # Antwort per SMS senden
            sende_sms(phone_number, antwort)

    # Verarbeitete Nachrichten speichern
    speichere_verarbeitete_nachrichten()


def begruessung(empfaenger):
    """
    Begrüßt den Nutzer per SMS und fragt nach dem Standort.
    """
    nachricht = "Hallo, wie lautet dein Standort?"
    sende_sms(empfaenger, nachricht)


if __name__ == "__main__":
    # Nutzer begrüßen (Handynummer hier als Beispiel)
    user_phone_number = input("Bitte gib die Handynummer ein, um den Nutzer zu begrüßen: ")
    begruessung(user_phone_number)

    # Nachrichten verarbeiten
    print("Warte auf Nachrichten...")
    while True:
        verarbeite_nachrichten()
        time.sleep(30)  # 30 Sekunden warten, bevor erneut Nachrichten abgerufen werden
