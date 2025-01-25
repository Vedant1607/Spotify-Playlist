import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Function to get date from user
def dateInput():
    inputDate = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
    
    try:
        date = datetime.strptime(inputDate,"%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")    
date = dateInput()

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
website = f"https://www.billboard.com/charts/hot-100/{date.strftime("%Y-%m-%d")}"
response = requests.get(url=website,headers=header)
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]