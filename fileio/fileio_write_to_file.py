# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Write to file
#  Author       : Team Tinitiate
# ==============================================================================



import os

# Create a file handler to create a new file in WRITE mode
# STEP 1: Create Folder if doesn't exist and ignore if exists
try:
    os.mkdir("C:/tinitiate")
except:
    pass

# STEP 2: Create a file in Write Mode 
new_file = open("C:/tinitiate/new_data.txt", "w")

# STEP 3: Write to file using write method
new_file.write("Welcome to Tinitiate.COM\n")
new_file.write("Line 2 data\n")
new_file.write("Line 3 data\n")

# The `close()` function will close the file handler and
# flushes all unwritten data to the file
new_file.close()
