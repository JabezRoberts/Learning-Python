import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "jabez"
TOKEN = "hw4u3t2tujh423kj5r2k34t2"

GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Step 1 from Pixela website - Creates a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Step 2 - Create our graph definition
# Graph endpoint --> /v1/users/<username>/graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


# Step 3 - Make our post request
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit" : "Minutes",
    "type"  : "int",
    "color" : "ajisai"
}

# Use the request header to authenticate our user
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# To view graph visit: https://pixe.la/v1/users/a-know/graphs/test-graph and change to https://pixe.la/v1/users/jabez/graphs/graph1.html


# How to create date using datetime module
today = datetime.now()
print(today.strftime("%Y%m%d"))


# Step 4 - Post a value to our graph
# Graph post endpoint /v1/users/<username>/graphs/<graphID>
graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_post_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "280"
}

# response = requests.post(url=graph_post_endpoint, json=graph_post_config, headers=headers)
# print(response.text)


# Put and Delete Requests
# Put or update endpoint = /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
yesterday = datetime(year=2025, month=7, day=24)
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

graph_put_config = {
    "quantity": "225"
}

response = requests.put(url=put_endpoint, headers=headers, json=graph_put_config)
print(response.text)


# Now to delete a request
# Delete endpoint --> /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)