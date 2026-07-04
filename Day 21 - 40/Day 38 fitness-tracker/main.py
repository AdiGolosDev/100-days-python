from datetime import datetime
from dotenv import load_dotenv
import os
import requests

load_dotenv()

xapp_id = os.getenv("XAPP_ID")
xapp_key = os.getenv("XAPP_KEY")

base_url = "https://app.100daysofpython.dev"
post_url = f"{base_url}/v1/nutrition/natural/exercise"

# query = input("Please describe the exercise you completed:\n")
query = "swam for 1 hours"

body = {
    "query": query,
    "weight_kg": 90,
    "height_cm": 188,
    "age": 22,
    "gender": "male"
}

headers = {
    "x-app-id": xapp_id,
    "x-app-key": xapp_key
}

response = requests.post(url=post_url, json=body, headers=headers)
print(response.json()["exercises"])
