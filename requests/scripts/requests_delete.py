# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : DELETE Request
#  Author       : Team Tinitiate
# ==============================================================================



import requests

url = 'https://fakestoreapi.com/products/8'
response = requests.delete(url)

if response.status_code == 200:
    print('DELETE request successful!')
else:
    print('DELETE request failed with status code:', response.status_code)
