# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `isnull()` to Detect Missing Values for a DataFrame
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a DataFrame with missing data
data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
        'Age': [25, 30, None, 22, 28],
        'Salary': [60000, 75000, 55000, None, 70000]}

employees_df = pd.DataFrame(data)

# Detecting missing values using isnull()
missing_values_null = employees_df.isnull()
print("Missing Values (using isnull()):")
print(missing_values_null)
