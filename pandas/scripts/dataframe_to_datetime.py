# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : `to_datetime()` in DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a list of date strings
dates_strings = ['2023-08-15', '2023-08-16', '2023-08-17']

# Converting strings to Timestamps
timestamp_list = pd.to_datetime(dates_strings)

print("Original Date Strings:")
print(dates_strings)
print("\nConverted Timestamps:")
print(timestamp_list)
