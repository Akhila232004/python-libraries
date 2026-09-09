# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Time Zone Handling with DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a DataFrame with time zone awareness
data = {'Date': ['2023-08-15 10:00:00', '2023-08-15 15:00:00'],
        'Sales': [100, 150]}

sales_df = pd.DataFrame(data)
sales_df['Date'] = pd.to_datetime(sales_df['Date']).dt.tz_localize('UTC')

# Converting time zone to 'America/New_York'
sales_df['Date_NY'] = sales_df['Date'].dt.tz_convert('America/New_York')

print("Original Sales DataFrame:")
print(sales_df)
