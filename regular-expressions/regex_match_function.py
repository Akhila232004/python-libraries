# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : match() Function
#  Author       : Team Tinitiate
# ==============================================================================



import re

# Create a test string with repeating letters/words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

# Search for match: The
match = re.search(r'The',test_string)

if match:
    print("Word 'The' is found in beginning of string:", "\n", test_string)
else:
    print("Word 'The' is NOT found in beginning of  string:", "\n", test_string)
