# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `isnull()` to Detect Missing Values for a Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series with missing data
sales_data = [5000, None, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Detecting missing values in the Series using isnull()
missing_values_series = sales_series.isnull()
print("Missing Values in Series (using isnull()):")
print(missing_values_series)
