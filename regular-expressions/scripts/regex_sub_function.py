# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : sub() Function
#  Author       : Team Tinitiate
# ==============================================================================



import re

# This is used to replace parts of strings, with a pattern
string = "Tinitiate good python examples"

# Replace "good" with "great"
new_string = re.sub("good", "great", string)
print(string)
print(new_string)
