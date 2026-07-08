from requests_cache import CachedSession
from datetime import timedelta
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_key = os.getenv("SHEETY_KEY")
        self.sheety_url = "https://api.sheety.co/b9282af21c6f87a9902d95863282b08a/flightDeals/prices"
        self.sheety_header = {"Authorization": f"Bearer {self.sheety_key}"}
        self.session = CachedSession("data_cache", expire_after=timedelta(hours=2))

    def get(self):
        self.response = self.session.get(url=self.sheety_url, headers=self.sheety_header)
        print(self.response)
        return(self.response)

    def post(self, city, iata_code, lowest_price):
        self.price = {
            "price": {
                "city": city,
                "iata code": iata_code,
                "lowest price": lowest_price
            }
        }

        self.response = self.session.post(url=self.sheety_url, json=self.price, headers=self.sheety_header)
        print(self.response)
        return(self.response)
