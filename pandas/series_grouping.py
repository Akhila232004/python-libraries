# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Grouping in Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series with sales data
sales_data = [100, 50, 70, 120, 90]
categories = ['Footwear', 'Apparel', 'Apparel', 'Footwear', 'Apparel']

sales_series = pd.Series(sales_data, index=categories)

# Displaying the original Series
print("Original Series:")
print(sales_series)



# Grouping the Series by index values (categories)
grouped = sales_series.groupby(sales_series.index)

# Displaying the grouped object
print("\nGrouped Object:")
print(grouped)



# Applying the 'sum()' aggregation function to the grouped data
sum_by_category = grouped.sum()

print("\nTotal Sales by Category:")
print(sum_by_category)



# Accessing a specific group using 'get_group()'
footwear_group = grouped.get_group('Footwear')

print("\nFootwear Group:")
print(footwear_group)



# Using the 'apply()' method to apply a custom aggregation function
def custom_agg(sales_series):
    return sales_series.max() - sales_series.min()

custom_aggregation = grouped.apply(custom_agg)

print("\nCustom Aggregation using apply():")
print(custom_aggregation)



# Using the 'transform()' method to broadcast aggregated values to original Series
total_sales_per_category = grouped.transform('sum')

sales_series['Total Sales per Category'] = total_sales_per_category

print("\nSeries with Transformed Values:")
print(sales_series)



# Using the 'filter()' method to filter groups based on a condition
filtered_groups = grouped.filter(lambda group: group.sum() > 150)

print("\nFiltered Groups using filter():")
print(filtered_groups)
