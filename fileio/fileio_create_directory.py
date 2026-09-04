# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Create directory using method `os.mkdir`
#  Author       : Team Tinitiate
# ==============================================================================



import os

# New Directory Path
new_dir = "C:/tinitiate/newdir"
# Create Directory with msdir
os.mkdir(new_dir)
# Check if folder exists
print(os.path.exists(new_dir))
