from flight_search import FlightSearch
from data_manager import DataManager

flight_search = FlightSearch()
data_manager = DataManager()

# 1. Get data from Google Sheet
sheet_data = data_manager.get_sheet_data()

# 2. Check if any iataCode is missing and update it
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_iata_code(city["city"])

# 3. Push updated codes back to Google Sheet
data_manager.destination_data = sheet_data
data_manager.update_iata_codes()

# 4. Done. You can print the updated sheet_data if you want
print(sheet_data)