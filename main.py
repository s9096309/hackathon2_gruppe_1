from weather_api import get_weather
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung

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
    print(musik_link)  # Der Link sollte jetzt als vollständiger URL angezeigt werden

else:
    print(f"Fehler beim Abrufen des Wetters für {location}.")
