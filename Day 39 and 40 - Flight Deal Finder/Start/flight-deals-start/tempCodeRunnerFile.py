
# Get data from Google Sheet using SHEETY then used pretty print pprint
response = requests.get(url=SHEETY_ENDPOINT, json=SHEETY_BODY, headers=SHEETY_HEADERS)
pprint(response.json())


# Pass everything stored in the "prices" key back to the main.py file and store it in a variable called sheet_data, so that you can print the sheet_data from main.py
sheet_data = response.json()["prices"]
print(sheet_data)


# 5. In main.py check if sheet_data contains any values for the "iataCode" key. If not, then the IATA Codes column is empty in the Google Sheet. In this case, pass each city name in sheet_data one-by-one to the FlightSearch class. For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code. You should use the response from the FlightSearch class to update the sheet_data dictionary.
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_iata_code(city["city"])
        
        update_sheet = f"{SHEETY_ENDPOINT}/{city["id"]}"
        new_data = {
            "price": {
                "iata_code" : city["iataCode"]
            }
        }
        
        response = requests.put(url=update_sheet, json=new_data, headers=SHEETY_HEADERS)
        print(f"RESPNSE TEXT  = {response.text}")
print(sheet_data)


for destination in sheet_data:
    if destination["iataCode"] == "":
        destination["iataCode"] = flight_search.get_iata_code(destination["city"])

data_manager.destination_data = sheet_data

data_manager.update_iata_codes()





# let url = 'https://api.sheety.co/0324626fcd2afb33f8675dea8fb4e696/flightDeals/prices';
# fetch(url)
# .then((response) => response.json())
# .then(json => {
#   // Do something with the data
#   console.log(json.prices);
# });
