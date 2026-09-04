# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Resampling with  DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
import numpy as np

# Generating a DataFrame with daily sales data
date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
sales_data = np.random.randint(50, 200, size=len(date_rng))
sales_df = pd.DataFrame({'Date': date_rng, 'Sales': sales_data})

# Resampling to a weekly frequency and calculating the mean sales
weekly_resampled = sales_df.resample('W-Mon', on='Date').mean()

print("Original Sales DataFrame:")
print(sales_df)
print("\nWeekly Resampled Sales DataFrame:")
print(weekly_resampled)
