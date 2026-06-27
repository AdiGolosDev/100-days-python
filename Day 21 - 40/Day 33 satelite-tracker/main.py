import requests
import json

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # raises http error if one occurs

data = response.json()["iss_position"]["longitude"]
print(data)
