# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `head()` and `tail()` with Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating a Series
fruits = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])

# Using head() to display the top 4 elements
print("Top 4 elements of the Series:")
print(fruits.head(4))

# Using tail() to display the bottom 3 elements
print("\nBottom 3 elements of the Series:")
print(fruits.tail(3))
