import requests
from datetime import datetime

# response = requests.get(url="https://api.sunrise-sunset.org/json")
# response.raise_for_status() # Just running this returns a 404 error because we didn't provide the latitude and longitude info

# the keys for the parameters must match what was given in the api documentation

MY_LATITUDE = 17.986370
MY_LONGITUDE = -76.947830

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]

# print(sunrise)
# print(sunrise.split("T")[1].split(":"))

# Now becomes
sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")

print(sunrise)
print(sunset)


time_now = datetime.now() # the time here is in a 24hr clock meanwhile from sunrise/sunset it's a 12hr clock so add the formatted param to the paramters dict
print(time_now.hour)