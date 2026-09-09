# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : `date_range()` in DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Generating a date range for a week of sales data
start_date = '2023-08-15'
end_date = '2023-08-21'
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

print("Generated Date Range:")
print(date_range)
