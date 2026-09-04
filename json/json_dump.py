# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : json.dump() demonstration
#  Author       : Team Tinitiate
# ==============================================================================



import json

# Sample JSON
bill_json =  """{ "BillNumber":1250
                 ,"BillTotal":3500
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":15
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":10
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"Cookies"
                                   ,"Quantity":8
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""
data = json.loads(bill_json)
    
with open('C:/tinitiate/bill_new.json', 'w') as f:
    json.dump(data, f, indent=2)
