# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Reshaping Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series
sales_data = [100, 120, 50, 60]
dates = ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02']
products = ['Shoes', 'Shoes', 'T-shirt', 'T-shirt']

sales_series = pd.Series(sales_data, index=pd.MultiIndex.from_tuples(zip(dates, products)))

# Using stack() to convert to long format
series_long_stack = sales_series.unstack(level=-1).stack()

# Using unstack() to convert back to wide format
series_wide_unstack = series_long_stack.unstack()

# Using melt() to transform to long format
series_melted = sales_series.reset_index(name='Sales').rename(columns={'level_0': 'Date', 'level_1': 'Product'})

print("Original Series:")
print(sales_series)
print("\nLong Series using stack():")
print(series_long_stack)
print("\nWide Series using unstack():")
print(series_wide_unstack)
print("\nMelted Series using melt():")
print(series_melted)
