# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Shifting with DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
import numpy as np

# Generating a DataFrame with daily temperature data
date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
temperature_data = np.random.uniform(18, 30, size=len(date_rng))
temperature_df = pd.DataFrame({'Date': date_rng, 'Temperature': temperature_data})

# Shifting the temperature data forward by 1 day
shifted_df = temperature_df.copy()  # Creating a copy to avoid modifying the original data
shifted_df['Shifted_Temperature'] = temperature_df['Temperature'].shift(periods=1)

print("Original Temperature DataFrame:")
print(temperature_df)
print("\nShifted Temperature DataFrame (1 day forward):")
print(shifted_df)
