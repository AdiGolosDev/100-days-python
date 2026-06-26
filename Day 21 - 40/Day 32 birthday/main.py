import smtplib
import random
import json
import os
import datetime as dt

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

def send_quote(quote):
    from_email, from_email_pass = get_email_by_index(0)
    to_email, _ = get_email_by_index(1)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_email_pass)
        connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=f"Quote of the Day\n\n{quote}")

def get_quote():
    with open("quotes.txt") as f:
        quotes_list = f.readlines()
        quote = random.choice(quotes_list)
    
    return quote

now = dt.datetime.now()
weekday = now.weekday()
quote = get_quote()

if weekday == 4:
    send_quote(quote)
