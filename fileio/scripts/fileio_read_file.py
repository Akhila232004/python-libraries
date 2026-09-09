# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Reading a file
#  Author       : Team Tinitiate
# ==============================================================================



import os

input_file = open("C:/tinitiate/data.txt","r")
# Assign the object "input_file" read function to a variable
var_text = input_file.read()
# Print the data in one go
print(var_text)
# Close the file stream handler
input_file.close()
