import requests

# for vienna
LAT = 48.208176
LNG = 16.373819

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status() # raises http error if one occurs

# data = response.json()
# longitude = data["iss_position"]["longitude"]

# print(longitude)

parameters = {
    "lat": LAT,
    "lng": LNG
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()["results"]
sunrise = data["sunrise"]
sunset = data["sunset"]

print(f"Sunrise is: {sunrise}\nSunset is: {sunset}")
