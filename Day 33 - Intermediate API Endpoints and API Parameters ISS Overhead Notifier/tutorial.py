import requests # Needed to be used to connect to APIs

response = requests.get(url="http://api.open-notify.org/iss-now.json") # Get data we want from an endpoint
print(response.status_code) # Gives the status code 200
if response.status_code != 200:
    raise Exception("Bad response from ISS API")
elif response.status_code == 404:
    raise Exception("That source code does not exist")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data.") 

# You can have the requests module to generate the exception
response = requests.get(url="http://api.open-notify.org/iss-now.json") # Get data we want from an endpoint
response.raise_for_status()


# Get data from API
data = response.json()
print(data) # Prints the data as we see it on their website

data = response.json()["iss_position"]
print(data)

longitude_data = response.json()["iss_position"]["longitude"]
latitude_data = response.json()["iss_position"]["latitude"]
print(f"Longitude: {longitude_data}")
print(f"Latitude: {latitude_data}")

iss_position = (longitude_data, latitude_data)
print(iss_position)