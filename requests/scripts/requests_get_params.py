# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Passing Parameters
#  Author       : Team Tinitiate
# ==============================================================================



import requests

params = {
    'limit': 3,
    'sort': 'desc'
}
response = requests.get('https://fakestoreapi.com/products', params=params)
json_data = response.json()
print(json_data)
