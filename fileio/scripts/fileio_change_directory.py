# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Change to specified directory With `chdir()`
#  Author       : Team Tinitiate
# ==============================================================================



# `chdir()` Changes to specified Directory
import os

my_dir = "C:/tinitiate"
# Change directory to the specified name in `my_dir`
os.chdir(my_dir)
# Check if current directory is the one specified in variable `my_dir`
print(os.getcwd())
