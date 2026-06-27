import requests
import json
import os
import smtplib
from datetime import datetime

# for sarajevo
LAT = 43.8486
LNG = 18.3564

#SMTP setup
CREDENTIALS_FILE = "email.json"

def load_credentials(email):
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(f"'{CREDENTIALS_FILE}' not found.")
    
    with open(CREDENTIALS_FILE, "r") as f:
        credentials = json.load(f)

    return credentials.get(email)

def get_email(index=0):
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(f"'{CREDENTIALS_FILE}' not found.")
    
    with open(CREDENTIALS_FILE, "r") as f:
        credentials = json.load(f)

    emails = list(credentials.keys())
    
    email = emails[index]
    password = credentials[email]
    return email, password

def send_email():
    msg = "Subject: ISS Satelite is Close\n\nThe international space station satelite is above Sarajevo. Take a look outside, maybe you'll see it!"

    email, password = get_email()
    to_email, _ = get_email(1)
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to_email, msg=msg)

def check_satelite_is_near(lat, lng):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() # raises http error if one occurs
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    print(f"Latitude of satelite: {latitude}")
    print(f"Longitude of satelite: {longitude}")

    if (lat - 5) < latitude < (lat + 5) and (lng - 5) < longitude < (lng + 5):
        print("The satelite is near.")
        return True
    else:
        return False
    
parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()["results"]

sunrise = data["sunrise"].split("T")
sunrise_hour = sunrise[1].split(":")[0]

sunset = data["sunset"].split("T")
sunset_hour = sunset[1].split(":")[0]

time_now = datetime.now()
hour = time_now.hour

if check_satelite_is_near(LAT, LNG):
    if hour > sunset_hour or hour < sunrise_hour:
        print("It is nighttime, and the satelite is near: sending email reminder now...")
        send_email()
