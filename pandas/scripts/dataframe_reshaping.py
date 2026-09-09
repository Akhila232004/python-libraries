# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Reshaping DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a DataFrame 
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'Product': ['Shoes', 'Shoes', 'T-shirt', 'T-shirt'],
        'Sales': [100, 120, 50, 60]}

df = pd.DataFrame(data)

# Using stack() to convert to long format
df_long_stack = df.set_index(['Date', 'Product'])['Sales'].unstack().reset_index()

# Using unstack() to convert back to wide format
df_wide_unstack = df_long_stack.set_index('Date').stack().unstack()

# Using melt() to transform to long format
df_melted = df.melt(id_vars=['Date', 'Product'], value_vars='Sales', var_name='Metric', value_name='Value')

print("Original DataFrame:")
print(df)
print("\nLong DataFrame using stack():")
print(df_long_stack)
print("\nWide DataFrame using unstack():")
print(df_wide_unstack)
print("\nMelted DataFrame using melt():")
print(df_melted)
