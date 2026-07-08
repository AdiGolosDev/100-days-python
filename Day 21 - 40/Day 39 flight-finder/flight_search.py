import os
from requests_cache import CachedSession
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        self.endpoint = "https://serpapi.com/search"
        self.session = CachedSession("flight_cache", expire_after=timedelta(hours=1))

    def search_flights(self, arrival_id):
        today = datetime.today()
        outbound_date = (today)

        params = {
            "engine": "google_travel_explore",
            "api_key": self.api_key,
            "departure_id": "VIE", # flights from vienna
            "arrival_id": arrival_id,
            "currency": "EUR",
            "hl": "en",
            "gl": "at",
            "month": 0,
            "duration": 2
        }
        response = self.session.get(self.endpoint, params=params)
        data = response.json()

        flights = data.get("flights", [])
        if not flights:
            return None
        
        cheapest = min(flights, key=lambda f: f["price"])
        return cheapest
    