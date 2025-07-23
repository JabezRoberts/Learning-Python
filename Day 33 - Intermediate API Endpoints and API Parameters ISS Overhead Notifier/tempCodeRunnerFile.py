
# response = requests.get(url="http://api.open-notify.org/iss-now.json") # Get data we want from an endpoint
# print(response.status_code) # Gives the status code 200
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# elif response.status_code == 404:
#     raise Exception("That source code does not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.") 