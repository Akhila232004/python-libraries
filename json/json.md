![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# JSON Module
* The `json` module provides a simple and easy-to-use API for working with JSON data.
* JSON(JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate.
* The `json` module can be used to:
  * Decode JSON data from a string or file object.
  * Encode Python objects to JSON data.
  * Write JSON data to a file.
  * Read JSON data from a file.

## json.loads()
* Used to deserialize JSON formatted data into Python objects.
* This method reads JSON formatted data from a string and returns a Python object.
```python
import json

# Sample JSON
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"Cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""

# Parse JSON using "loads" Method
data = json.loads(bill_json)

# Get Subset of JSON
print(data["BillDetails"])

# JSON Nested value, Get First Product
print(data["BillDetails"][0]["Product"])

# JSON Get All Products
for restaurant in data["BillDetails"]:
    print(restaurant["Product"])
```

## json.dumps()
* Used to serialize Python objects into JSON formatted data.
* This method serializes a Python object and returns the resulting JSON formatted data as a string.
```python
import json

# Sample JSON
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"Cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""

data = json.loads(bill_json)
for restaurant in data["BillDetails"]:
      del restaurant["Product"]
      data_new = json.dumps(data, indent=2)
print(data_new)
```

## json.load()
* Used to deserialize JSON formatted data into Python objects.
* This method reads JSON formatted data from a file-like object and returns a Python object.
```python
import json

with open('C:/tinitiate/bill.json') as f:
    data = json.load(f)
    print(data)

StoreLocation = data['StoreLocation']
BillNumber = data['BillNumber']

for bill in data['BillDetails']:
    Product = bill['Product']
    print(Product)
```

## json.dump()
* Used to serialize Python objects into JSON formatted data.
* This method serializes a Python object and writes the resulting JSON formatted data to a file-like object.
```python
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
```

## Using API
* API is a way to access data from a remote server.
* API response in format of JSON.
```python
import json
import requests

# Sample API for weather forecast
request = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json")
response =request.text

data = json.loads(response)
print(json.dumps(data, indent=2))

dataseries=list()
temp=dict()

for item in data['dataseries']:
    temp['timepoint'] = item['timepoint']
    temp['cloudcover'] = item['cloudcover']
    temp['seeing'] = item['seeing']    
    temp['transparency'] = item['transparency']
    temp['rh2m'] = item['rh2m']
    temp['lifted_index'] = item['lifted_index']
    temp['lifted_index'] = item['lifted_index']
    
    dataseries.append({
        'Timepoint':temp['timepoint'],
        'Cloudcover': temp['cloudcover'],
        'Seeing': temp['seeing'],
        'Sransparency': temp['transparency'],
        'Rh2m': temp['rh2m'],
        'Lifted_index': temp['lifted_index']
    })     
    
with open('C:/tinitiate/weather_forecast.json', 'w') as f:
  json.dump(dataseries, f, indent=2)
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|