# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : `to_datetime()` in Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
    
# Creating a Series with date strings as data
date_strings = ['2023-08-15', '2023-08-16']
values = [100, 150]
    
sales_series = pd.Series(values, index=date_strings)
    
# Converting the index to Timestamps using to_datetime()
sales_series.index = pd.to_datetime(sales_series.index)
    
print("Original Sales Series:")
print(sales_series)
