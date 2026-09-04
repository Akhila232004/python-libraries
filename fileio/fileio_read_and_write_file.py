# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Read and Write to file
#  Author       : Team Tinitiate
# ==============================================================================



with open('C:/tinitiate/newfile.txt', 'r+') as f:
    # Read the file
    data = f.read()
    
    # Write to the file
    f.write('Hello, World!')
