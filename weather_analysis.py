def kategorisiere_temperatur(temperature):
    if temperature < 10:
        return "kalt"
    elif 10 <= temperature <= 25:
        return "mittel"
    else:
        return "warm"

def analysiere_wetter(wetter):
    if "rain" in wetter.lower() or "drizzle" in wetter.lower():
        return "regnerisch"
    elif "clear" in wetter.lower():
        return "klar"
    elif "snow" in wetter.lower():
        return "schnee"
    else:
        return "bewölkt"

def gib_musikempfehlung(temp_kategorie, wetter_kategorie):
    if temp_kategorie == "kalt" and wetter_kategorie == "regnerisch":
        return "https://open.spotify.com/playlist/kalt_regnerisch"
    elif temp_kategorie == "warm" and wetter_kategorie == "klar":
        return "https://open.spotify.com/playlist/warm_klar"
    else:
        return "https://open.spotify.com/playlist/mischung"
