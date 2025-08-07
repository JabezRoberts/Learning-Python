import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime


load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "https://example.com"

spotify_credentials = spotipy.Spotify(
    auth_manager=SpotifyOAuth
    (
        client_id=SPOTIFY_CLIENT_ID, 
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri = REDIRECT_URI,
        scope = "playlist-modify-private",
        cache_path=".cache",
        username="Zeilhan"
    ))




# Create an input() prompt that asks what year you would like to travel to in YYY-MM-DD format. e.g.
year = input("What year would you like to visit? Enter in the format YYYY-MM-DD: \n")
# year="2000-08-12"


# 3. Include a header when you make your request to billboard.com. See HTTP headers
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

# 4. Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List
website_url = "https://www.billboard.com/charts/hot-100/"+year

response = requests.get(url = website_url, headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
# print(soup)

all_titles = soup.find_all("h3", class_="c-title", id="title-of-a-story")
all_titles = soup.select("li ul li h3")
# print(all_titles)
song_titles = [title.getText().strip() for title in all_titles]
# print(song_titles)


# all_artists = soup.find_all(class_="c-label")
# print(all_artists)
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)


results = spotify_credentials.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
user_id = spotify_credentials.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = spotify_credentials.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


user_id = spotify_credentials.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = spotify_credentials.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

spotify_credentials.playlist_add_items(playlist_id=playlist["id"], items=song_uris)