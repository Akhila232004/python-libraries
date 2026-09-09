# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Merging DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Original DataFrame
product_data = {'Product': ['Shoes', 'T-shirt', 'Jeans'],
                'Price': [50, 20, 40]}
df_original = pd.DataFrame(product_data)



# New DataFrame for concatenation
new_products = {'Product': ['Socks', 'Hat'],
                'Price': [10, 15]}
df_new = pd.DataFrame(new_products)



# Concatenating vertically using pd.concat()
concatenated_df = pd.concat([df_original, df_new], ignore_index=True)

print("Concatenated DataFrame:")
print(concatenated_df)



# New DataFrame for merging
product_info = {'Product': ['Shoes', 'T-shirt', 'Jeans', 'Socks'],
                'Brand': ['Nike', 'Adidas', 'Levi\'s', 'Puma']}
df_info = pd.DataFrame(product_info)

# Merging based on the 'Product' column
merged_df = pd.merge(df_original, df_info, on='Product')

print("\nMerged DataFrame:")
print(merged_df)



# New DataFrame for joining
product_discount = {'Discount': [10, 5, 15]}
df_discount = pd.DataFrame(product_discount)

# Setting index for both DataFrames
df_original.set_index('Product', inplace=True)
df_discount.set_index(df_original.index, inplace=True)

# Joining based on indices
joined_df = df_original.join(df_discount)

print("\nJoined DataFrame:")
print(joined_df)



# New DataFrame to append
new_product = {'Product': ['Socks'],
               'Price': [10]}
df_new = pd.DataFrame(new_product)

# Appending the new product to the original DataFrame
appended_df = pd.concat([df_original, df_new], ignore_index=True)

print("\nAppended DataFrame:")
print(appended_df)



# Reset index so 'Product' becomes a column again
df_original_reset = df_original.reset_index()

# New DataFrame for combining
product_prices = {'Product': ['T-shirt', 'Jeans', 'Socks'],
                  'Price': [25, 35, 15]}
df_prices = pd.DataFrame(product_prices)

# Combining values using combine_first()
combined_df = df_original_reset.set_index('Product').combine_first(df_prices.set_index('Product')).reset_index()

print("\nCombined DataFrame:")
print(combined_df)



# New DataFrame for ordered merging
product_inventory = {'Product': ['Jeans', 'Shoes', 'T-shirt'],
                     'Inventory': [100, 80, 150]}
df_inventory = pd.DataFrame(product_inventory)

# Ordered merging based on the 'Product' column
ordered_merged_df = pd.merge_ordered(df_original, df_inventory, on='Product')

print("\nOrdered Merged DataFrame:")
print(ordered_merged_df)
