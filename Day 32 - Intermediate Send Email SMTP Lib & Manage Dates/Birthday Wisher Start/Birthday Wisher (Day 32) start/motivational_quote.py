import smtplib
import datetime as dt
import random


# TODO Use the datetime module to obtain the current day of the week.
# TODO Open the quotes.txt file and obtain a list of quotes
# TODO Use the random module to pick a quote from your list of quotes
# TODO Use the smtpliv to send the email to yourself

MY_EMAIL = "testemail@gmail.com"
MY_PASSWORD = "1234abf"


now = dt.datetime.now() # Get the current date and time
day = now.weekday()
if day == 1:
    with open("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 32 - Intermediate Send Email SMTP Lib & Manage Dates/Birthday Wisher Start/Birthday Wisher (Day 32) start/quotes.txt") as quote_data:
        quotes = quote_data.readlines()
        quote = random.choice(quotes)
    print(f"random quote: \n\n {quote}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motiv \n\n{quote}"
        )