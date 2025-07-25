import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')


load_dotenv()
API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")
SHEETY_ENDPOINT = os.getenv("SHEETY_GET_ENDPOINT")

nutritionix_host_domain = "https://trackapi.nutritionix.com"
nutritionix_endpoint = "/v2/natural/exercise"
URL = f"{nutritionix_host_domain}{nutritionix_endpoint}"
# request and authentication from app

my_exercice = input("Tell me which exercises you did: ")


# Authentication Headers
AUTH_HEADERS = {
    "Content-Type": "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}



## SHEETY

request_body = {
    "query": my_exercice,
    "weight_kg": 55,
    "height_cm": 185.5,
    "age": 25
}
response = requests.post(url=URL, json=request_body, headers=AUTH_HEADERS)
print(response.status_code)
print(response.json())


sheety_api=os.getenv("SHEETY_API")

SHEETY_HEADERS = {
    "Authorization": f"Bearer {sheety_api}",  # assuming it's a bearer token
    "Content-Type": "application/json"
}


today = datetime.now()
date = today.strftime("%Y/%m/%d")
print(date)

current_time = today.strftime("%H:%M:%S")
print(current_time)


# SHEETY_BODY = {
#     "workout": {
#         "date": date,
#         "time" : current_time,
#         "exercise" : "Swimming",
#         "duration" : 12,
#         "calories": 109
#     } 
# }
# sheety_post = requests.post(url=SHEETY_ENDPOINT,json=SHEETY_BODY, headers=SHEETY_HEADERS)
# print(sheety_post.text)

for exercise in response.json()["exercises"]:
    SHEETY_BODY = {
        "workout": {
            "date": date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_post = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_BODY, headers=SHEETY_HEADERS)
    print(sheety_post.text.encode('utf-8', errors='replace').decode())
