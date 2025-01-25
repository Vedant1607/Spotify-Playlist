# Billboard Hot 100 Spotify Playlist Generator

This project allows users to create a Spotify playlist based on the Billboard Hot 100 chart for a specific date. It uses web scraping to fetch song data from Billboard's website and the Spotify API to create a playlist in the user's account.

## Features

- Input a date in the format `YYYY-MM-DD` to fetch Billboard's Hot 100 chart for that day.
- Create a Spotify playlist with the songs found on the chart.

## Prerequisites

1. Python 3.10 or later
2. Spotify Developer Account
3. Billboard website access

## Setup Instructions

### 1. Clone the Repository
```bash
$ git clone https://github.com/Vedant1607/billboard-spotify-playlist.git
$ cd billboard-spotify-playlist
```

### 2. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 3. Set Up Spotify Developer Account
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create a new application and note down the `Client ID` and `Client Secret`.
3. Set the Redirect URI to `http://localhost:8888/callback`.

### 4. Create a `.env` File
Create a `.env` file in the root directory with the following content:
```
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
REDIRECT_URI=http://localhost:8888/callback
```

### 5. Run the Script
```bash
$ python main.py
```

## Usage

1. Enter a date in the format `YYYY-MM-DD` when prompted (e.g., `2020-01-01`).
2. The script will scrape Billboard's website for the Hot 100 chart on that date.
3. It will search Spotify for each song and create a playlist in your account.

## Files

- `main.py`: The main script.
- `.env`: Contains sensitive information like Spotify credentials.

## Libraries Used

- `requests`: To fetch data from Billboard's website.
- `beautifulsoup4`: To parse and extract song data from HTML.
- `spotipy`: To interact with the Spotify Web API.
- `python-dotenv`: To securely manage environment variables.

## Error Handling

- Ensures that invalid dates are handled gracefully with a user prompt.

## Limitations

- Song names on Billboard and Spotify may not always match, leading to some songs being unfound.
- Relies on the current structure of the Billboard website.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/): A lightweight Python library for Spotify API.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): A Python library for parsing HTML and XML.
