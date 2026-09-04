# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Grouping in DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating the DataFrame
data = {'Product': ['Shoes', 'T-shirt', 'Jeans', 'Shoes', 'Jeans'],
        'Category': ['Footwear', 'Apparel', 'Apparel', 'Footwear', 'Apparel'],
        'Sales': [100, 50, 70, 120, 90]}

df = pd.DataFrame(data)

# Displaying the original DataFrame
print("Original DataFrame:")
print(df)



# Grouping the data by the 'Category' column
grouped = df.groupby('Category')

# Displaying the grouped object
print("\nGrouped Object:")
print(grouped)



# Applying the 'sum()' aggregation function to the grouped data
sum_by_category = grouped['Sales'].sum()

print("\nTotal Sales by Category:")
print(sum_by_category)



# Accessing a specific group using 'get_group()'
footwear_group = grouped.get_group('Footwear')

print("\nFootwear Group:")
print(footwear_group)



# Grouping by multiple columns and applying multiple aggregation functions
grouped_multiple = df.groupby(['Category', 'Product'])
result = grouped_multiple['Sales'].agg(['sum', 'mean', 'max'])

print("\nGrouped Data with Multiple Aggregations:")
print(result)



# Resetting the index of the grouped DataFrame
result_reset_index = result.reset_index()

print("\nReset Index of Grouped Data:")
print(result_reset_index)



# Using the 'apply()' method to apply a custom aggregation function
def custom_agg(sales_series):
    return sales_series.max() - sales_series.min()

custom_aggregation = grouped['Sales'].apply(custom_agg)

print("\nCustom Aggregation using apply():")
print(custom_aggregation)



# Using the 'transform()' method to broadcast aggregated values to original DataFrame
total_sales_per_category = grouped['Sales'].transform('sum')

df['Total Sales per Category'] = total_sales_per_category

print("\nDataFrame with Transformed Values:")
print(df)



# Using the 'filter()' method to filter groups based on a condition
filtered_groups = grouped.filter(lambda group: group['Sales'].sum() > 150)

print("\nFiltered Groups using filter():")
print(filtered_groups)
