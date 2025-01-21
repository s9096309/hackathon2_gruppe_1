import pytest
from weather_api import get_weather
from weather_analysis import kategorisiere_temperatur, analysiere_wetter, gib_musikempfehlung

def test_kategorisiere_temperatur(self):
    self.assertEqual(kategorisiere_temperatur(-5), "bitterkalt")
    self.assertEqual(kategorisiere_temperatur(5), "kühl")
    self.assertEqual(kategorisiere_temperatur(15), "mild")
    self.assertEqual(kategorisiere_temperatur(25), "warm")
    self.assertEqual(kategorisiere_temperatur(35), "heiß")
def test_analysiere_wetter(self):
    self.assertEqual(analysiere_wetter("light rain"), "regnet")
    self.assertEqual(analysiere_wetter("clear sky"), "sonnig")
    self.assertEqual(analysiere_wetter("snow"), "schneit")
    self.assertEqual(analysiere_wetter("thunderstorm"), "stürmt")
    self.assertEqual(analysiere_wetter("hail"), "hagelt")
    self.assertEqual(analysiere_wetter("overcast clouds"), "neutral")
def test_gib_musikempfehlung(self):
    self.assertEqual(gib_musikempfehlung("bitterkalt", "neutral"),
                     "https://open.spotify.com/album/6A9POxb0v1H4gNTAfD5Pn7")
    self.assertEqual(gib_musikempfehlung("warm", "regnet"),
                     "https://open.spotify.com/playlist/4NV3zE3iyVp7JdaKoQrITG")
    self.assertEqual(gib_musikempfehlung("heiß", "sonnig"),
                     "https://open.spotify.com/playlist/37i9dQZF1DX3fXJqxGjuEP")
    self.assertEqual(gib_musikempfehlung("neutral", "neutral"),
                     "https://open.spotify.com/playlist/37i9dQZF1DWWvoJqVv7uOD")

def test_get_weather(self):
    # Hier solltest du einen echten API-Key verwenden oder einen Mock für die API-Antwort erstellen.
    # Für den Test verwenden wir einen Beispielstandort.
    location = "Berlin"
    temperature, weather_condition = get_weather(location)
    self.assertIsNotNone(temperature)
    self.assertIsNotNone(weather_condition)
if __name__ == '__main__':
    pytest.main()