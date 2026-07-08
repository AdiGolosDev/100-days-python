import smtplib
import os

class Email:
    def __init__(self):
         self.email = os.getenv("EMAIL")
         self.password = os.getenv("EMAIL_PASS")
         self.to_email = os.getenv("TO_EMAIL")

    def send_email(self, msg):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email, to_addrs=self.to_email, msg=msg)
