import requests
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": "graph2",
    "name": "Reading Graph",
    "unit": "pg",
    "type": "int",
    "color": "momiji" # red
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url=pixela_endpoint, json=user_params)
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response)
data = response.json()
print(data["message"])




