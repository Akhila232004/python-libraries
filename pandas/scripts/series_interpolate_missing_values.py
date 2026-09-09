# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `interpolate()` to Fill Missing Values in a Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series with missing data
sales_data = [5000, None, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Filling missing values in the Series with interpolation using interpolate()
interpolated_series = sales_series.interpolate()
print("Series after Filling Missing Values with Interpolation (interpolate()):")
print(interpolated_series)
