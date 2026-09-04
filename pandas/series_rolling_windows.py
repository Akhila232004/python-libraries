# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Rolling Windows with Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
import numpy as np

# Generating a Series with daily sales data
date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
sales_data = np.random.randint(50, 200, size=len(date_rng))
sales_series = pd.Series(sales_data, index=date_rng)

# Calculating rolling average over a window of 3 days
rolling_avg = sales_series.rolling(window=3).mean()

print("Original Sales Series:")
print(sales_series)
print("\nRolling Average Sales Series (Window = 3 days):")
print(rolling_avg)
