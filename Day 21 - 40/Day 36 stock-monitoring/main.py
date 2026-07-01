from requests_cache import CachedSession
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API = os.getenv("ALPHA_V_API")
NEWS_API = os.getenv("NEWS_API")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
PHONE_NUM = os.getenv("PHONE")

now = datetime.now()
last_week = now - timedelta(weeks=1)
last_week_str = str(last_week).split(" ")[0]

av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API
}

news_params = {
    "q":COMPANY_NAME,
    "from":last_week_str,
    "sortBy":"popularity",
    "apiKey":NEWS_API
}

session = CachedSession('stock_monitoring_cache', expire_after=timedelta(hours=24))
stock_r = session.get("https://www.alphavantage.co/query", params=av_params)
stock_data = stock_r.json()

time_series = stock_data['Time Series (Daily)']
date_list = list(time_series.keys())
yesterday_close = float(time_series[date_list[0]]['4. close'])
before_yesterday_close = float(time_series[date_list[1]]['4. close'])

num_change = yesterday_close - before_yesterday_close
percent = (num_change / before_yesterday_close) * 100
if num_change <= 0:
    change = f"🔻 {num_change}"
    percent_change = f"🔻 {percent:.2f}%"
else:
    change = f"🔺 {num_change}"
    percent_change = f"🔺 {percent:.2f}%"

if abs(percent) >= 5:
    news_r = session.get("https://newsapi.org/v2/everything", params=news_params)
    news_data = news_r.json()
    articles = news_data['articles'][0:3]

    messages = [f"TSLA:\nDollar Change:{change}  Percent Change:{percent_change}\n{article['title']}\n{article['description']}" for article in articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

