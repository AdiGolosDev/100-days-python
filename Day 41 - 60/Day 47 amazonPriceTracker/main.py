from bs4 import BeautifulSoup
import requests
import smtplib
import os

url = "https://www.amazon.de/-/en/dp/B0BPB13792"
email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PASS")
to_email = os.getenv("TO_EMAIL")

def send_email_notification(msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=to_email, msg=msg)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd"
}

response = requests.get(url, headers=headers)
# print(response.status_code)
# print(response.text[:2000])
amazon_text = response.text
soup = BeautifulSoup(amazon_text, "html.parser")
price = soup.select(selector=".a-price-whole")
print(price)
print("a-price-whole" in amazon_text)
print("a-offscreen" in amazon_text)
# 	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
