def kategorisiere_temperatur(temp):
    if temp <= 0:
        return "bitterkalt"
    elif 1 <= temp <= 10:
        return "kühl"
    elif 11 <= temp <= 20:
        return "mild"
    elif 21 <= temp <= 30:
        return "warm"
    else:
        return "heiß"

def analysiere_wetter(condition):
    if "rain" in condition.lower():
        return "regnerisch"
    elif "cloud" in condition.lower():
        return "bewölkt"
    elif "clear" in condition.lower():
        return "klar"
    elif "snow" in condition.lower():
        return "schnee"
    elif "storm" in condition.lower():
        return "stürmisch"
    else:
        return "neutral"

def gib_musikempfehlung(temp_kategorie, wetter_kategorie):
    playlists = {
        "bitterkalt": "https://open.spotify.com/album/6A9POxb0v1H4gNTAfD5Pn7",
        "kühl": "https://open.spotify.com/playlist/2wW2k1Hu2WeEDKvdOMyxzT",
        "mild": "https://open.spotify.com/album/75JpmNePVsBfD3pU1Of0t6",
        "warm": "https://open.spotify.com/playlist/2hmLDliFT9mW84XHxRUzwx",
        "heiß": "https://open.spotify.com/playlist/37i9dQZF1DX3fXJqxGjuEP",
        "regnerisch": "https://open.spotify.com/playlist/4NV3zE3iyVp7JdaKoQrITG",
        "bewölkt": "https://open.spotify.com/playlist/37i9dQZF1DWWvoJqVv7uOD",
        "klar": "https://open.spotify.com/playlist/2hmLDliFT9mW84XHxRUzwx",
        "schnee": "https://open.spotify.com/album/6A9POxb0v1H4gNTAfD5Pn7",
        "stürmisch": "https://open.spotify.com/album/3FdJxeAEFdLsmuSGgHi7Oa"
    }
    return playlists.get(temp_kategorie) or playlists.get(wetter_kategorie) or "https://open.spotify.com/playlist/37i9dQZF1DWWvoJqVv7uOD"
