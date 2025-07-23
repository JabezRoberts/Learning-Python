from dotenv import load_dotenv
import os
import requests
# from twilio.rest import Client

load_dotenv()
api_key = os.getenv("API_KEY")
# print(api_key)

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = -76.7936
MY_LONG = 17.997

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(OWM_ENDPOINT, params=parameters)
# print(response.status_code)
response.raise_for_status()
weather_data=response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    print("in loop for")
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring brella ela ella aye aye ayeee")
        will_rain = True

if will_rain:
    print("Bring brella ela ella aye aye ayeee")