# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Remove directory using method `os.rmdir`
#  Author       : Team Tinitiate
# ==============================================================================



import os

# Directory path
new_dir = "C:/tinitiate/delete_dir_name"
# Remove directory with rmdir
os.rmdir(new_dir)
# Check if folder exists
print(os.path.exists(new_dir))
