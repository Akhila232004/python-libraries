# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Append to file
#  Author       : Team Tinitiate
# ==============================================================================



import os

# Writing a LIST to file
append_file = open("C:/tinitiate/new_data.txt","a")

list_1 = ['a', 'ZZ']
append_file.writelines(list_1)

# Writing a TUPLE to file
tuple_1 = ('A', 'b')
append_file.writelines(tuple_1)

# Writing a DICTIONARY to file
dictionary_1 = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
append_file.writelines(dictionary_1)
append_file.close()
