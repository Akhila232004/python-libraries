# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Merging Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating the Series and list
prices_data = [50, 20, 40]
product_names = ['Shoes', 'T-shirt', 'Jeans']



# Creating the original Series
original_series = pd.Series(prices_data, index=product_names)

# Displaying the original Series
print("Original Series:")
print(original_series)



# Creating a new Series for appending
new_product = pd.Series([30], index=['Hat'])

# Appending the new product to the original Series
appended_series = pd.concat([original_series, new_product])

print("\nAppended Series:")
print(appended_series)



# Creating a Series for updating missing values
updated_prices = pd.Series([25, 18], index=['Shoes', 'T-shirt'])

# Updating missing values using combine_first()
combined_series = original_series.combine_first(updated_prices)

print("\nCombined Series:")
print(combined_series)



# Creating a Series for ordered merging
inventory_data = [100, 80, 120]
inventory_series = pd.Series(inventory_data, index=['Shoes', 'T-shirt', 'Jeans'])

df_price = original_series.rename_axis('Product').reset_index(name='Price')
df_inv   = inventory_series.rename_axis('Product').reset_index(name='Inventory')

# Ordered merging using merge_ordered()
ordered_merged_series = pd.merge_ordered(df_price, df_inv, on='Product')

print("\nOrdered Merged Series:")
print(ordered_merged_series)
