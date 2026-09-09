# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `fillna()` to Fill Missing Values in a Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series with missing data
sales_data = [5000, None, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Filling missing values in the Series with a specified value using fillna()
filled_series = sales_series.fillna(0)
print("Series after Filling Missing Values (fillna()):")
print(filled_series)
