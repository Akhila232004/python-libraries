# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Indexing for Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series for monthly sales data
sales_data = [5000, 7500, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Display the entire Series
print("Full Sales Series:")
print(sales_series)

# Using loc for indexing (label-based)
sales_january_loc = sales_series.loc['January']  # Selects the value for January
print("Using loc for indexing:")
print(sales_january_loc)

# Using iloc for indexing (integer position-based)
sales_january_iloc = sales_series.iloc[0]  # Selects the value at position 0 (January)
print("\nUsing iloc for indexing:")
print(sales_january_iloc)
