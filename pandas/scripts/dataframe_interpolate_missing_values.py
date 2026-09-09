# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `interpolate()` to Fill Missing Values in a DataFrame
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a DataFrame with missing data
data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
        'Age': [25, 30, None, 22, 28],
        'Salary': [60000, 75000, 55000, None, 70000]}

employees_df = pd.DataFrame(data)

# Filling missing values with interpolation using interpolate()
interpolated_df = employees_df.interpolate()
print("DataFrame after Filling Missing Values with Interpolation (interpolate()):")
print(interpolated_df)
