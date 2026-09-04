# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : POST Request
#  Author       : Team Tinitiate
# ==============================================================================



import requests
import json

# Define the URL to send the request to
url = "https://fakestoreapi.com/products"

# Define the data to send in the request body
data = {
    "title": "test product",
    "price": 13.5,
    "description": "lorem ipsum set",
    "image": "https://i.pravatar.cc",
    "category": "electronic"
}

# Define any headers to include in the request
headers = {"Content-Type": "application/json"}
# This sets the 'Content-Type' header of the HTTP request to indicate that
# we're sending JSON data.

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))
json_response = response.json()
print(json_response)
