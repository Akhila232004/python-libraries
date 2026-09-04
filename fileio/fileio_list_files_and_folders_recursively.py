# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : List all files and directories "recursively" in a given path
#  Author       : Team Tinitiate
# ==============================================================================



# Using `os.walk()` we can list all files and folders in a given folder path recursively
from os import walk

mypath = "C:/tinitiate"
all_files = []
all_folders = []

# Loop through all Files and Folders in a Given Path [mypath variable]
for (dirpath, dirnames, filenames) in walk(mypath):
    # Capture all files and store in list all_files
    all_files.extend(filenames)
    # Capture all files and store in list all_folders
    all_folders.extend(dirnames)
# Print all files and folders lists
print(all_files)
print(all_folders)
