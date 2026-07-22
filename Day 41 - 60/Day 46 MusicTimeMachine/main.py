from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import requests

URL = "https://appbrewery.github.io/bakeboard-hot-100/" # 2016-03-12/

user_input = input("What year of music would you like to visit?\n YYYY-MM-DD format please: ")

response = requests.get(URL + user_input + "/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
songs = soup.select(selector=".chart-entry__info")

song_dict = {}
for song in songs:
    song_dict[song.select_one(selector=".chart-entry__title").text] = song.select_one(selector=".chart-entry__artist").text

print(song_dict)
