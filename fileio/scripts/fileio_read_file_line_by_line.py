# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Read file line by line using method `readline()`
#  Author       : Team Tinitiate
# ==============================================================================



import os

# Open the file
input_file1 = open("C:/tinitiate/data.txt","r")
# While true enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() # Read line by line, to variable current line
    if not curr_line:
        break                          # Break if there is no line to read
    print(curr_line)                   # Print the current line

# Close the file stream handler
input_file1.close()
