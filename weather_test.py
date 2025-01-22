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
                     "https://www.youtube.com/watch?v=cpUuU07_iMc")
    assert(gib_musikempfehlung("warm", "regnet"),
                     "https://www.youtube.com/watch?v=gQWnGRtLFeE")
    assert(gib_musikempfehlung("heiß", "sonnig"),
                     "https://www.youtube.com/watch?v=QQQpkll5aoA")
    assert(gib_musikempfehlung("neutral", "neutral"),
                     "https://www.youtube.com/watch?v=1DjDs3LiQrE")

def test_get_weather():
     # Für den Test verwenden wir einen Beispielstandort.
    location = "Berlin"
    temperature, weather_condition = get_weather(location)
    assert(temperature)   # nicht None oder leer ist
    assert(weather_condition) #nicht None oder leer ist


if __name__ == '__main__':
    pytest.main()