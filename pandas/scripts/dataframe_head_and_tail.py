# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `head()` and `tail()` with DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 32, 47, 19, 28]}

df = pd.DataFrame(data)

# Using head() to display the top 3 rows
print("Top 3 rows of the DataFrame:")
print(df.head(3))

# Using tail() to display the bottom 2 rows
print("\nBottom 2 rows of the DataFrame:")
print(df.tail(2))
