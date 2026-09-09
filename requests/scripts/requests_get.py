# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : GET Request
#  Author       : Team Tinitiate
# ==============================================================================



import requests

response = requests.get('https://fakestoreapi.com/products')
print(response.text)
