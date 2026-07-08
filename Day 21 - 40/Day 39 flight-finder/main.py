from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from email_notification import Email
from dotenv import load_dotenv

load_dotenv()

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
email_sender = Email()

sheet_rows = data_manager.get().json()["prices"]

for row in sheet_rows:
    row_id = row["id"]
    city = row["city"]
    iata_code = row["iataCode"]
    lowest_price = row["lowestPrice"]

    cheapest = flight_search.search_flights(iata_code)

    if cheapest is None:
        continue

    if cheapest["price"] < lowest_price:
        data_manager.post(row_id, city, iata_code, cheapest["price"])
        email_msg = f"Subject: Klokan Cheap Flight Alert\n\nA flight to {city} is available for cheap! Fly there for {cheapest['price']} Euros"
        email_sender.send_email(email_msg)
        # notification_manager.send_msg(f"Klokan Flight Alert! Pay {cheapest['price']} to travel to {city}!")
