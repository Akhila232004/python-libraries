# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : search() Function
#  Author       : Team Tinitiate
# ==============================================================================



import re

# Create a test string with repeating letters/words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

# Search for pattern: tinitiate (in small letters)
match = re.search(r'tinitiate',test_string)

if match:
    print("The word 'tinitiate' is found in the string:", "\n", test_string)
else:
    print("The word 'tinitiate' is NOT found in the string:", "\n", test_string)


# Search for more complicated patterns, search for 12*, where *
# is wildcard character which matches everything else after the pattern "12"
match = re.search(r'12*',test_string)

if match:
    print("The word '12*' is found in the string:", "\n", test_string)
else:
    print("The word '12*' is NOT found in the string:", "\n", test_string)
