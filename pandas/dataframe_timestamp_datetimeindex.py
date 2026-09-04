# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : `Timestamp` and `DatetimeIndex ` in DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating individual Timestamps
timestamp1 = pd.Timestamp('2023-08-15 10:30:00')
timestamp2 = pd.Timestamp('2023-08-15 15:45:00')

# Creating a DatetimeIndex for a list of Timestamps
timestamps = pd.to_datetime(['2023-08-15 10:30:00', '2023-08-15 15:45:00'])

print("Individual Timestamps:")
print(timestamp1)
print(timestamp2)
print("\nDatetimeIndex:")
print(timestamps)
