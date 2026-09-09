# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Iterator with `__next__()` function
#  Author       : Team Tinitiate
# ==============================================================================



# Create a list of data
data_set1 = [1,2,3,4,5]

# Loop or Iterate over this data list using a loop
for value1 in data_set1:
    print(value1)

# Loop or Iterate over this data list using an iterator
# Create an iterator using the `iter()` function
itr = iter(data_set1)

# Call the print to display the next value
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

# Uncommenting below line gives an error as there are no more elements
# print(itr.__next__())

# The biggest advantage is there is no "end loop", see for loop indentation
# We can add more code in between the ".__next__()" providing some flexibility
