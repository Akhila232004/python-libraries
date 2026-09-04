# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `isna()` to Detect Missing Values for a Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series with missing data
sales_data = [5000, None, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Detecting missing values in the Series using isna()
missing_values_series_isna = sales_series.isna()
print("Missing Values in Series (using isna()):")
print(missing_values_series_isna)
