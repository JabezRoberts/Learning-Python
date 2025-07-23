# import datetime

# # Now tap into the datetime class to get to the datetime module
# datetime.datetime

import datetime as dt

now = dt.datetime.now() # Get the current date and time
print(now) # Type date.time object
year = now.year # Type int
month = now.month

if year == 2020:
    print("It's 2020!")


day_of_week = now.weekday() 
print(day_of_week) # if it returns 1 means it's the second day of the week TUESDAY

# Let's say we wanted to create a datetime object of our own and set it to a particular date of our choice:
date_of_birth = dt.datetime(year=1990, month=2, day=28, hour=19, minute=32)
print(date_of_birth)