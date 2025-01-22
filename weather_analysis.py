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
        "bitterkalt": "https://www.youtube.com/watch?v=cpUuU07_iMc",   # Winter Chill Lo-Fi Hip Hop
        "kühl": "https://www.youtube.com/watch?v=oouFE51HcqM",      # Autumn Vibes Playlist
        "mild": "https://www.youtube.com/watch?v=EzXtBIE5lW0",         # Spring Vibes
        "warm": "https://www.youtube.com/watch?v=gQWnGRtLFeE",      # Summer Vibes
        "heiß": "https://www.youtube.com/watch?v=QQQpkll5aoA",      # Tropical
        "regnet": "https://www.youtube.com/watch?v=_VyA2f6hGW4",    # Regen
        "neutral": "https://www.youtube.com/watch?v=1DjDs3LiQrE",   # Everyday Favorites
        "schneit": "https://www.youtube.com/watch?v=sE3uRRFVsmc",      # Storm / Dark Orchestra
        "stürmt": "https://www.youtube.com/watch?v=GVFgEBq0EKM",       # Storm / Dark Orchestra
        "hagelt": "https://www.youtube.com/watch?v=jYFVUILYbgE"        # Storm / Dark Orchestra
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
