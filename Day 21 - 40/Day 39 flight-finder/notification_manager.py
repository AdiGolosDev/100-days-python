import os
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    def send_msg(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_FROM_PHONE"),
            to=os.getenv("MY_PHONE")
        )
        print(message.status)
