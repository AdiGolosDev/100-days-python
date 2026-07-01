from requests_cache import CachedSession
from datetime import timedelta
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API = os.getenv("ALPHA_V_API")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
phone_num = os.getenv("PHONE")

av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
session = CachedSession('demo_cache', expire_after=timedelta(hours=12))
r = session.get("https://www.alphavantage.co/query", params=av_params)
print(r.from_cache)
data = r.json()

time_series = data['Time Series (Daily)']
date_list = list(time_series.keys())
yesterday_close = float(time_series[date_list[0]]['4. close'])
before_yesterday_close = float(time_series[date_list[1]]['4. close'])

# initial attempt - i thought it looks ugly so i asked mr claude for help for the other version
# day_stocks_list = list(data['Time Series (Daily)'].keys())
# yesterday_closing = float(data['Time Series (Daily)'][day_stocks_list[0]]['4. close'])
# before_yesterday_closing = float(data['Time Series (Daily)'][day_stocks_list[1]]['4. close'])


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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

