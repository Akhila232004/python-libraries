# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : List all files and directories in a given path
#  Author       : Team Tinitiate
# ==============================================================================



# Using `os.walk()` we can list all files and folders in a given folder path 
import os

my_dir = "C:/tinitiate"
print(os.listdir(my_dir))
