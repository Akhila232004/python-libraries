# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Read file line by line as list of strings
#  Author       : Team Tinitiate
# ==============================================================================



# Read file line by line as list of strings suffixed with newline character '\n'
import os

readlines_file = open("C:/tinitiate/data.txt","r")
# Prints the file contents as a LIST
print(readlines_file.readlines())

readlines_file.close()
