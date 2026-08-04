from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_text = response.text
soup = BeautifulSoup(zillow_text, "html.parser")
properties = soup.select(selector=".StyledPropertyCardDataWrapper")

properties_dict = {}
i = 0
for property in properties:
    p = {}
    p["address"] = property.find("address").text.replace("\n","").strip(" ")
    p["price"] = property.find("span").text
    p["link"] = property.find("a").get("href")
    properties_dict[i] = p
    i += 1

with open("san_francisco_p-under-3000.json", "w", encoding="utf-8") as file:
    json.dump(properties_dict, file, indent=4, sort_keys=True)
