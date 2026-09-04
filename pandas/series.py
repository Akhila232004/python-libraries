# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series for daily sales of a product
sales_data = [10, 15, 8, 12, 20]
sales_series = pd.Series(sales_data, name='Daily Sales')

print(sales_series)
