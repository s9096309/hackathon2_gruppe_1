import pytest
from weather_api import get_weather
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung

def test_kategorisiere_temperatur():
    assert kategorisiere_temperatur(-5) == "bitterkalt"
    assert kategorisiere_temperatur(5) == "kühl"
    assert kategorisiere_temperatur(15) == "mild"
    assert kategorisiere_temperatur(25) == "warm"
    assert kategorisiere_temperatur(35) == "heiß"

def test_analysiere_wetter():
    assert analysiere_wetter("light rain") == "regnet"
    assert analysiere_wetter("clear sky") == "sonnig"
    assert analysiere_wetter("snow") == "schneit"
    assert analysiere_wetter("thunderstorm") == "stürmt"
    assert analysiere_wetter("hail") == "hagelt"
    assert analysiere_wetter("overcast clouds") == "neutral"


def test_gib_musikempfehlung():
  # Testfälle für Temperaturkategorien
  assert gib_musikempfehlung("bitterkalt",
                             "neutral") == "https://www.youtube.com/watch?v=1DjDs3LiQrE"  # Priorität: neutral
  assert gib_musikempfehlung("kühl", "neutral") == "https://www.youtube.com/watch?v=1DjDs3LiQrE"  # neutral hat Vorrang

  # Testfälle für Wetterkategorien
  assert gib_musikempfehlung("warm", "regnet") == "https://www.youtube.com/watch?v=_VyA2f6hGW4"  # regnet hat Vorrang
  assert gib_musikempfehlung("heiß", "schneit") == "https://www.youtube.com/watch?v=sE3uRRFVsmc"  # schneit hat Vorrang

  # Testfälle ohne spezifische Wetterkategorie
  assert gib_musikempfehlung("mild", "unbekannt") == "https://www.youtube.com/watch?v=EzXtBIE5lW0"  # mild

  # Testfall: Sowohl Temperatur- als auch Wetterkategorie unbekannt
  assert gib_musikempfehlung("unbekannt", "unbekannt") == "https://www.youtube.com/watch?v=1DjDs3LiQrE"


def test_get_weather():
    # Für den Test verwenden wir einen Beispielstandort.
    location = "Berlin"
    temperature, weather_condition = get_weather(location)
    assert temperature is not None  # Stellt sicher, dass temperature nicht None ist
    assert weather_condition is not None  # Stellt sicher, dass weather_condition nicht None ist

if __name__ == '__main__':
    pytest.main()
