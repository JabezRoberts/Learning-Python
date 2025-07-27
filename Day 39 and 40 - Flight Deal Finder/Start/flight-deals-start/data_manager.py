import requests
from dotenv import load_dotenv
import os


load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_API = os.getenv("SHEETY_API")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.sheety_headers = {
            "Authorization" : f"Bearer {os.getenv('SHEETY_API')}"
        }
        self.destination_data = []
    
    def get_sheet_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    
    def update_iata_codes(self):
        for city in self.destination_data:
            update_url = f"{self.sheety_endpoint}/{city['id']}"
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]  # ✅ Must match column name in Google Sheet
                }
            }
            response = requests.put(
                url=update_url,
                json=new_data,
                headers=self.sheety_headers
            )
            response.raise_for_status()
            print(f"Updated {city['city']} with IATA code {city['iataCode']}")