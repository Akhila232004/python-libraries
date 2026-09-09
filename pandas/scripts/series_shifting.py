# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Shifting with Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
import numpy as np

# Generating a Series with daily sales data
date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
sales_data = np.random.randint(50, 200, size=len(date_rng))
sales_series = pd.Series(sales_data, index=date_rng)

# Shifting the data forward by 1 day
shifted_series = sales_series.shift(periods=1)

print("Original Sales Series:")
print(sales_series)
print("\nShifted Sales Series (1 day forward):")
print(shifted_series)
