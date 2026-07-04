import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

# my professional snake of code :)
# today = str(datetime.now()).split(" ")[0].replace("-", "")
t = datetime.now()
# t = datetime(year=2026, month=7, day=1)
today = t.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = "read"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pix_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_endpoint = f"{pix_endpoint}/{today}"

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
    "quantity": "50"
}

update_config = {
    "quantity": "120"
}

# requests.post(url=pixela_endpoint, json=user_params)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# response = requests.post(url=pix_endpoint, json=pixel_config, headers=headers)
# print(response)
# print(response.json()["message"])

response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response)
print(response.json()["message"])
