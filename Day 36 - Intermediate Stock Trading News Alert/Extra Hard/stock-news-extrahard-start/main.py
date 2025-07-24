import requests
from dotenv import load_dotenv
import os



load_dotenv()
api_key = os.getenv("ALPHA_ADVANTAGE_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_NEWS_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : api_key
}


news_parameters = {
    "apiKey": news_api_key,
    # "searchIn": COMPANY_NAME,
    "q": "Tesla",
    # "language": "en"
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

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

response = requests.get(STOCK_NEWS_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
print(stock_data["Time Series (Daily)"]["2025-07-23"]["1. open"])
print(stock_data["Time Series (Daily)"]["2025-07-23"]["4. close"])

# The above line gives the opening and closing price for yesterday but the date is hardcoded
# What happens when the date changes?
# To resolve this issue we will convert the entire dictionary holding the returned data into a list so we can get the first entry or yesterdy at all times

new_stock_data = stock_data["Time Series (Daily)"]
stock_data_list = [value for (key,value) in new_stock_data.items()]
# print(stock_data_list)
yesterday_data = stock_data_list[0]
print(yesterday_data)
yesterday_closing_price = yesterday_data["4. close"]
print(f"yesterday's closing price: {yesterday_closing_price}")


# Now we need to get the day before yesterday's data
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Day before yesterday's closing price: {day_before_yesterday_closing_price}")


# Find the difference between yesterday and day before yesterday's price
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(f"The stock difference is: {difference}")

up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
percentage_difference = round((difference / float(yesterday_closing_price)) * 100)
print(f"The percentage difference is: {percentage_difference}%")

# Now if the percentage is greater than 5 print get news
# AND Get articles related to the company name using News API
if abs(percentage_difference) > 0: 
    print("Get news!")
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = response.json()["articles"]
    print(f"News Data: {news_data}")

# Now use slice to get the first three articles on the company
    three_articles = news_data[:3]
    print(three_articles)

    # "Headline: {article title}. \nBrief: {article_description}" --> Format we need
    formatted_articles = [f"{STOCK}: {up_down}{percentage_difference}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

# Now use Twilio to send a separate message with each article
# check solution code for this part. I can't access Twilio