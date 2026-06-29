import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

#japan
LAT = 34.623232
LON = 133.878453

params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

print(response)