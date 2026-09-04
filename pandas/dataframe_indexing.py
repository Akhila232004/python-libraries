# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Indexing for DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a DataFrame for employee information
data = {'EmployeeID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Department': ['HR', 'IT', 'Marketing', 'Finance', 'IT'],
        'Salary': [60000, 75000, 55000, 80000, 70000]}

employees_df = pd.DataFrame(data)

# Display the entire DataFrame
print("Full DataFrame:")
print(employees_df)

# Using loc for indexing (label-based)
employee_bob_loc = employees_df.loc[1]  # Selects the row with index 1 (Bob's details)
print("Using loc for indexing:")
print(employee_bob_loc)

# Using iloc for indexing (integer position-based)
employee_bob_iloc = employees_df.iloc[1]  # Selects the row at position 1 (Bob's details)
print("\nUsing iloc for indexing:")
print(employee_bob_iloc)
