# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : findall() Function
#  Author       : Team Tinitiate
# ==============================================================================



import re

# Prints all the words with a small "t" in the test-string
# The options are:
# word with a "t" in between `\w+t\w+`,
# OR indicated by the PIPE symbol `|`
# word with a "t" as the last character `\w+t`,
# OR indicated by the PIPE symbol `|`
# word with a "t" as the first character `t\w+`,

# Create a test string with repeating letters words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

all_t = re.findall(r'\w+t\w+|\w+t|t\w+',test_string)

# The re.findall returns a TUPLE and we print all the elements looping
# through the TUPLE
for lpr in all_t:
    print(lpr)
