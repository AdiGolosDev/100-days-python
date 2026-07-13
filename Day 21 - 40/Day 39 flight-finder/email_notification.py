import smtplib
import os
import json

class Email:
    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("EMAIL_PASS")
        enterEmail = True
        emails = []
        while enterEmail:
            email = input("Please enter your email: ")
            emails.append(email)
            again = input("Do you want to add another email to the email list? y / n")
            if again != "y":
                enterEmail = False

        if os.path.exists("emails.json"):
            with open("emails.json", "r") as f:
                existing_emails = json.load(f)
        else:
            existing_emails = []

        # Combine old + new emails
        self.all_emails = existing_emails + emails

        # Save back to the JSON file
        with open("emails.json", "w") as f:
            json.dump(self.all_emails, f, indent=4)

    def send_email(self, msg):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            for email in self.all_emails:
                connection.sendmail(from_addr=self.email, to_addrs=email, msg=msg)
