# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Time Zone Handling with Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Create a standalone Series of timestamps
dates = pd.Series(['2023-08-15 10:00:00', '2023-08-15 15:00:00'])

# Convert to datetime and localize to UTC
dates = pd.to_datetime(dates).dt.tz_localize('UTC')

# Convert to Tokyo timezone
dates_tokyo = dates.dt.tz_convert('Asia/Tokyo')

print("\nOriginal Series (UTC):")
print(dates)

print("\nConverted Series (Asia/Tokyo):")
print(dates_tokyo)
