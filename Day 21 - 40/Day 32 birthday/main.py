import smtplib
import json
import os

CREDENTIALS_FILE = "email_credentials.json"

def load_credentials(email: str) -> str | None:
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(f"'{CREDENTIALS_FILE}' not found.")
    
    with open(CREDENTIALS_FILE, "r") as f:
        credentials = json.load(f)

    return credentials.get(email)

def get_email_by_index(index: int) -> tuple[str, str | None]:
    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(f"'{CREDENTIALS_FILE}' not found.")
    
    with open(CREDENTIALS_FILE, "r") as f:
        credentials = json.load(f)

    emails = list(credentials.keys())

    if index < 0 or index >= len(emails):
        raise IndexError(f"Index {index} out of range. There are {len(emails)} emails")
    
    email = emails[index]
    password = credentials[email]
    return email, password

from_email, from_email_pass = get_email_by_index(0)
to_email, _ = get_email_by_index(2)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=from_email, password=from_email_pass)
    connection.sendmail(from_addr=from_email, to_addrs=to_email, msg="Subject: Kako smo dobri programeri\n\nEvo sada i subject stavljamo")

# import datetime as dt

# now = dt.datetime.now()