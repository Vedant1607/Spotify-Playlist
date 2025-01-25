import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.billboard.com/charts/hot-100/"

# Function to get date from user
def dateInput():
    inputDate = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
    
    try:
        date = datetime.strptime(inputDate,"%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")    
date = dateInput()
