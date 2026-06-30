import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
api_key = os.getenv("API_KEY")
auth_token = os.getenv("AUTH_TOKEN")
phone_num = os.getenv("PHONE")
account_sid = os.getenv("ACCOUNT_SID")

client = Client(account_sid, auth_token)

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
# angela's(100 days python instructor) code checks if weather id is < 700 which includes snow and everything
# if it snows i ain't bringing no umbrella
for forecast in data["list"][0:5]:
    # weather_id = forecast["weather"][0]["id"] i think i don't even need this for my own code to work
    description = forecast["weather"][0]["description"]
    if "rain" in description.lower() or "drizzle" in description.lower():
        rain = True

if rain:
    text = "It will rain in the next 15 hours, bring an umbrella if you are made out of sugar..."
else:
    text = "There won't be rain in the next 15 hours. No need to think of bringing an umbrella."

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=text,
  to=phone_num
)
print(message.sid)
