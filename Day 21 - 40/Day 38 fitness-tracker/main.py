from datetime import datetime
from dotenv import load_dotenv
import os
import requests

load_dotenv()

xapp_id = os.getenv("XAPP_ID")
xapp_key = os.getenv("XAPP_KEY")
sheety_key = os.getenv("SHEETY_KEY")

base_url = "https://app.100daysofpython.dev"
post_url = f"{base_url}/v1/nutrition/natural/exercise"
sheety_url = "https://api.sheety.co/b9282af21c6f87a9902d95863282b08a/fitnessTrackerPython/workouts"

# query = input("Please describe the exercise you completed:\n")
query = "played basketball for 3 hours"
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

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
exercise = response.json()["exercises"][0]

workout = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise["name"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
}

sheety_header = {
    "Authorization": f"Bearer {sheety_key}"
}

#post to sheety
response = requests.post(url=sheety_url, json=workout, headers=sheety_header)
print(response)

#get from sheety
response = requests.get(url=sheety_url, headers=sheety_header)
print(response.json())

