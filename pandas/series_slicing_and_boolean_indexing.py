# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Slicing and Boolean Indexing for a Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series for monthly sales data
sales_data = [5000, 7500, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Slicing: Selecting sales data for Q1 (January to March)
sales_q1 = sales_series['January':'March']
print("Sales for Q1 (January to March):")
print(sales_q1)

# Boolean Indexing: Selecting months with high sales (above 7000)
high_sales_months = sales_series[sales_series > 7000]
print("\nMonths with High Sales (Above 7000):")
print(high_sales_months)
