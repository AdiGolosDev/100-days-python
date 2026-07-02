import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

t = datetime.now()
today = str(t).split(" ")[0].replace("-", "")

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = "read"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pg",
    "type": "int",
    "color": "momiji" # red
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_config = {
    "date": today,
    "quantity": "20"
}

# requests.post(url=pixela_endpoint, json=user_params)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response)
data = response.json()
print(data["message"])
