import pytest
from weather_api import get_weather
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung

def test_kategorisiere_temperatur():
    assert(kategorisiere_temperatur(-5), "bitterkalt")
    assert(kategorisiere_temperatur(5), "kühl")
    assert(kategorisiere_temperatur(15), "mild")
    assert(kategorisiere_temperatur(25), "warm")
    assert(kategorisiere_temperatur(35), "heiß")

def test_analysiere_wetter():
    assert(analysiere_wetter("light rain"), "regnet")
    assert(analysiere_wetter("clear sky"), "sonnig")
    assert(analysiere_wetter("snow"), "schneit")
    assert(analysiere_wetter("thunderstorm"), "stürmt")
    assert(analysiere_wetter("hail"), "hagelt")
    assert(analysiere_wetter("overcast clouds"), "neutral")

def test_gib_musikempfehlung():
    assert(gib_musikempfehlung("bitterkalt", "neutral"),
                     "https://open.spotify.com/album/6A9POxb0v1H4gNTAfD5Pn7")
    assert(gib_musikempfehlung("warm", "regnet"),
                     "https://open.spotify.com/playlist/4NV3zE3iyVp7JdaKoQrITG")
    assert(gib_musikempfehlung("heiß", "sonnig"),
                     "https://open.spotify.com/playlist/37i9dQZF1DX3fXJqxGjuEP")
    assert(gib_musikempfehlung("neutral", "neutral"),
                     "https://open.spotify.com/playlist/37i9dQZF1DWWvoJqVv7uOD")

def test_get_weather():
    location = "Berlin"
    temperature, weather_condition = get_weather(location)
    assert(temperature)
    assert(weather_condition)

    # Hier solltest du einen echten API-Key verwenden oder einen Mock für die API-Antwort erstellen.
    # Für den Test verwenden wir einen Beispielstandort.


if __name__ == '__main__':
    pytest.main()