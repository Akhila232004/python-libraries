# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : `date_range()` in Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Generating a Series with date range as index
start_date = '2023-08-15'
end_date = '2023-08-21'
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
values = [100, 150, 120, 130, 140, 110, 180]

sales_series = pd.Series(values, index=date_range)

print("Generated Sales Series with Date Index:")
print(sales_series)
