# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : DataFrame
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a DataFrame for product inventory
data = {'ProductID': [101, 102, 103],
        'Product Name': ['Shoes', 'T-shirt', 'Jeans'],
        'Price': [50, 20, 40],
        'Quantity': [50, 100, 30]}

inventory_df = pd.DataFrame(data)
print(inventory_df)
