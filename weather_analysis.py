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

def analysiere_wetter(bedingung):
    if "rain" in bedingung:
        return "regnet"
    elif "clear" in bedingung:
        return "sonnig"
    elif "snow" in bedingung:
        return "schneit"
    elif "storm" in bedingung or "thunderstorm" in bedingung:
        return "stürmt"
    elif "hail" in bedingung:
        return "hagelt"
    else:
        return "neutral"

def gib_musikempfehlung(temp_kategorie, wetter_kategorie):
    """
    Playlist passend zum Wetter -> SPÄTER: Einzelnen Song aus passender Playlist ausgeben?
    """

    playlists = {
        "bitterkalt": "https://open.spotify.com/album/6A9POxb0v1H4gNTAfD5Pn7",   # Winter Chill Lo-Fi Hip Hop
        "kühl": "https://open.spotify.com/playlist/2wW2k1Hu2WeEDKvdOMyxzT",      # Autumn Vibes Playlist
        "mild": "https://open.spotify.com/album/75JpmNePVsBfD3pU1Of0t6",         # Spring Vibes
        "warm": "https://open.spotify.com/playlist/2hmLDliFT9mW84XHxRUzwx",      # Summer Vibes
        "heiß": "https://open.spotify.com/playlist/37i9dQZF1DX3fXJqxGjuEP",      # Tropical
        "regnet": "https://open.spotify.com/playlist/4NV3zE3iyVp7JdaKoQrITG",    # Regen
        "neutral": "https://open.spotify.com/playlist/37i9dQZF1DWWvoJqVv7uOD",   # Everyday Favorites
        "schneit": "https://open.spotify.com/album/6A9POxb0v1H4gNTAfD5Pn7",      # Winter Chill Lo-Fi Hip Hop
        "stürmt": "https://open.spotify.com/album/3FdJxeAEFdLsmuSGgHi7Oa",       # Storm / Dark Orchestra
        "hagelt": "https://open.spotify.com/album/3FdJxeAEFdLsmuSGgHi7Oa"        # Storm / Dark Orchestra
    }

    # Priorität: Wetter > Temperatur
    if wetter_kategorie in playlists:
        return playlists[wetter_kategorie]
    elif temp_kategorie in playlists:
        return playlists[temp_kategorie]
    else:
        return playlists["neutral"]



# https://open.spotify.com/album/6A9POxb0v1H4gNTAfD5Pn7  Winter Chill Lo-Fi Hip Hop
# https://open.spotify.com/playlist/2wW2k1Hu2WeEDKvdOMyxzT Autumn Vibes Playlist
# https://open.spotify.com/album/75JpmNePVsBfD3pU1Of0t6  Spring Vibes
# https://open.spotify.com/playlist/2hmLDliFT9mW84XHxRUzwx Summer Vibes
# https://open.spotify.com/playlist/37i9dQZF1DX3fXJqxGjuEP Tropical
# https://open.spotify.com/playlist/4NV3zE3iyVp7JdaKoQrITG Regen
# https://open.spotify.com/playlist/37i9dQZF1DWWvoJqVv7uOD  Everyday Favorites
# https://open.spotify.com/album/3FdJxeAEFdLsmuSGgHi7Oa  Storm / Dark Orchestra