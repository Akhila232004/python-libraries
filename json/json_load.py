# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : json.load() demonstration
#  Author       : Team Tinitiate
# ==============================================================================



import json

with open('C:/tinitiate/bill.json') as f:
    data = json.load(f)
    print(data)

StoreLocation = data['StoreLocation']
BillNumber = data['BillNumber']

for bill in data['BillDetails']:
    Product = bill['Product']
    print(Product)
