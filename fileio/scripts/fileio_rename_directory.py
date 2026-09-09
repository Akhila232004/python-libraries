# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Rename a folder or file
#  Author       : Team Tinitiate
# ==============================================================================



import os

# Current folder name
old_name = "C:/tinitiate/newdir"
# New folder name
new_name = "C:/tinitiate/renamedir"
# Rename the folder
os.rename(old_name, new_name)
print(f"Folder renamed from {old_name} to {new_name}")
