# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Slicing for a DataFrame
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

# Slicing: Selecting employees in the IT Department
it_department = employees_df[employees_df['Department'] == 'IT']
print("Employees in the IT Department:")
print(it_department)

# Slicing: Selecting specific columns for a subset of employees
selected_columns = employees_df.loc[:, ['Name', 'Salary']]  # Selects 'Name' and 'Salary' columns for all rows
print("\nSelected Columns for All Employees:")
print(selected_columns)
