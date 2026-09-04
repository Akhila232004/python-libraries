![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# File IO
* The `OS` Module of Python handles the **FILE IO (File Input Output)**
* Common Folder operations include list directories, find current directory name, go to a specific directory, create directory or delete directory.
* Common File Operations include open a file to read or write, read a file line by line, check if a file exists, delete a file, create an empty file.

## File IO Directory Operations
File IO Directory Operations includes the following:
### Get current directory with `getcwd()`
```python
# `getcwd()` displays the current directory
import os

print(os.getcwd())
```
### Change to specified directory With `chdir()`
```python
# `chdir()` Changes to specified Directory
import os

my_dir = "C:/tinitiate"
# Change directory to the specified name in `my_dir`
os.chdir(my_dir)
# Check if current directory is the one specified in variable `my_dir`
print(os.getcwd())
```
### List all files and directories in a given path
```python
# Using `os.walk()` we can list all files and folders in a given folder path 
import os

my_dir = "C:/tinitiate"
print(os.listdir(my_dir))
```
### List all files and directories "recursively" in a given path
```python
# Using `os.walk()` we can list all files and folders in a given folder path recursively
from os import walk

mypath = "C:/tintiate"
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
```
### Create directory using method `os.mkdir`
```python
import os

# New Directory Path
new_dir = "C:/tinitiate/new_dir_name"
# Create Directory with msdir
os.mkdir(new_dir)
# Check if folder exists
print(os.path.exists(new_dir))
```
### Rename a folder or file
```python
import os

# Current folder name
old_name = "C:/tinitiate/newdir"
# New folder name
new_name = "C:/tinitiate/rename_dir_name"
# Rename the folder
os.rename(old_name, new_name)
print(f"Folder renamed from {old_name} to {new_name}")
```
### Remove directory using method `os.rmdir`
```python
import os

# Directory path
new_dir = "C:/tinitiate/delete_dir_name"
# Remove directory with rmdir
os.rmdir(new_dir)
# Check if folder exists
print(os.path.exists(new_dir))
```

## File IO File Operations
File IO File Operations includes the following:
### Read file
* Create a file handler to open the file in READ mode using `open()` function
* The `open()` function returns a file object
* This is a built-in function used to work with files
* Pass filename and the access mode (Read/Write/Append...)
* **Usage:** 
    * FILE_OBJECT = OPEN ("File_path\File_name",FILE_MODE)
* **FILE_MODE:**
    * "r" READ Mode
    * "w" WRITE Mode (overwrite the file)
    * "a" APPEND Mode (Appends to a file)
    * "r+" READ and WRITE Mode
    * "x" Create a new file
* The `with open()` statement is a Python expression used to work with files.
* It provides a way to ensure that a file is closed when the block inside the `with` statement is exited, regardless of how the block is exited.
```python
import os

input_file = open("C:/tinitiate/data.txt","r")
# Assign the object "input_file" read function to a variable
var_text = input_file.read()
# Print the data in one go
print(var_text)
# Close the file stream handler
input_file.close()
```
### Read file line by line using method `readline()`
```python
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
```
### Read file line by line as list of strings
```python
# Read file line by line as list of strings suffixed with newline character '\n'
import os

readlines_file = open("C:/tinitiate/data.txt","r")
# Prints the file contents as a LIST
print(readlines_file.readlines())

readlines_file.close()
```
### Write to file
```python
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
```
### Append to file
```python
import os

# Writing a LIST to file
append_file = open("C:/tinitiate/new_data.txt","a")

list_1 = ['a', 'ZZ']
append_file.writelines(list_1)

# Writing a TUPLE to file
tuple_1 = ('A', 'b')
append_file.writelines(tuple_1)

# Writing a DICTIONARY to file
dictionary_1 = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
append_file.writelines(dictionary_1)
append_file.close()
```
## Create a new file
```python
with open('C:/tinitiate/newfile.txt', 'x') as f:
    f.write('Welcome to Tinitiate!\n')
```
### Read and Write to file
```python
with open('C:/tinitiate/newfile.txt', 'r+') as f:
    # Read the file
    data = f.read()
    
    # Write to the file
    f.write('Hello, World!')
```
### Rename file or folder
```python
# The `rename()` method can be used to rename both a folder or a file
import os

os.rename("C:/tinitiate/new_data.txt", "C:/tinitiate/info.txt" )
```
### Remove file
```python
# Use the `remove()` method to remove or delete file
import os

os.remove("C:/tinitiate/info.txt")
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|