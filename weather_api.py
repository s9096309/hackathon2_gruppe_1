import requests

API_KEY = "d99eeffdfe41fc93fc4279e8e5c1ce6d"

def get_weather(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            weather_condition = data["weather"][0]["description"]
            return temperature, weather_condition
        else:
            print(f"Fehler bei der Wetterabfrage: {response.status_code}")
    except Exception as e:
        print(f"Exception bei der Wetterabfrage: {e}")
    return None, None
