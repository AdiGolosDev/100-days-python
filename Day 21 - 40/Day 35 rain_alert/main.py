import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

#okinawa
# LAT = 34.623232
# LON = 133.878453

#dublin
LAT = 53.349804
LON = -6.260310

params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

data = response.json()

rain = False
for forecast in data["list"][0:5]:
    weather_id = forecast["weather"][0]["id"]
    description = forecast["weather"][0]["description"]
    if "rain" in description.lower() or "drizzle" in description.lower():
        rain = True

if rain:
    print("There will be rain within the next 15 hours")
else:
    print("There won't be rain in the next 15 hours")
