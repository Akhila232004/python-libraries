# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `dropna()` to Remove Rows Missing Values in a Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series with missing data
sales_data = [5000, None, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Dropping missing values from the Series using dropna()
cleaned_series = sales_series.dropna()
print("Series after Dropping Missing Values (dropna()):")
print(cleaned_series)
