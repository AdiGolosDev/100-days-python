import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # raises http error if one occurs

data = response.json()
longitude = data["iss_position"]["longitude"]

print(longitude)