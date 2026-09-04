# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Rolling Windows with DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
import numpy as np

# Generating a DataFrame with hourly temperature data
date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='H')
temperature_data = np.random.uniform(18, 30, size=len(date_rng))
temperature_df = pd.DataFrame({'Timestamp': date_rng, 'Temperature': temperature_data})

# Calculating rolling average over a window of 6 hours
rolling_avg_df = temperature_df.copy()  # Creating a copy to avoid modifying the original data
rolling_avg_df['Rolling_Avg'] = temperature_df['Temperature'].rolling(window=6).mean()

print("Original Temperature DataFrame:")
print(temperature_df)
print("\nRolling Average Temperature DataFrame (Window = 6 hours):")
print(rolling_avg_df)
