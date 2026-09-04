# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Resampling with  Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
import numpy as np

# Generating a DataFrame with hourly temperature data
date_rng = pd.date_range(start='2023-08-01', end='2023-08-05', freq='H')
temperature_data = np.random.uniform(18, 30, size=len(date_rng))
temperature_df = pd.DataFrame({'Timestamp': date_rng, 'Temperature': temperature_data})

# Resampling to a daily frequency and calculating the maximum temperature
daily_resampled = temperature_df.resample('D', on='Timestamp').max()

print("Original Temperature DataFrame:")
print(temperature_df)
print("\nDaily Resampled Temperature DataFrame:")
print(daily_resampled)
