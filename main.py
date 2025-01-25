import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Function to get date from user
def dateInput():
    inputDate = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
    
    try:
        date = datetime.strptime(inputDate,"%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")    
date = dateInput()

# Scrape Billboard website
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
website = f"https://www.billboard.com/charts/hot-100/{date.strftime('%Y-%m-%d')}"
response = requests.get(url=website,headers=header)
website_html = response.text

# Parse HTML to get song names
soup = BeautifulSoup(website_html,"html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                                               client_secret=os.getenv("CLIENT_SECRET"),
                                               redirect_uri="http://localhost:8888/callback",
                                               scope = "playlist-modify-private playlist-modify-public",
                                               show_dialog=True
                                               ))

# Create a new Spotify playlist
user_id = sp.current_user()["id"]
print(user_id)
print("\n"*10)
playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Hot 100 - {date.strftime('%Y-%m-%d')}", public=False)
playlist_id = playlist["id"]