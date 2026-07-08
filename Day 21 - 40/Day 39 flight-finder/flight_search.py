import os
from requests_cache import CachedSession
from datetime import timedelta

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        self.endpoint = "https://serpapi.com/search"
        self.session = CachedSession("flight_cache", expire_after=timedelta(hours=1))

    def search_flights(self, departure_id, arrival_id, outbound_date, return_date):
        params = {
            "engine": "google_flights",
            "api_key": self.api_key,
            "departure_id": departure_id,
            "arrival_id": arrival_id,
            "outbound_date": outbound_date,
            "return_date": return_date,
            "currency": "EUR",
            "hl": "en",
            "gl": "at",
            "type": "1",
        }
        response = self.session.get(self.endpoint, params=params)
        data = response.json()

        flights = data.get("best_flights", []) + data.get("other_flights", [])
        if not flights:
            return None

        cheapest = min(flights, key=lambda f: f["price"])
        return cheapest
    