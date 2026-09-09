# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Multiple pattern matching in words of a given string
#  Author       : Team Tinitiate
# ==============================================================================



import re

my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'

# Word pattern 'starts with'
# From 'my_string' find all words starting with 'H'
starting_h = re.findall(r'\bH+\w+.\b', my_string)

for word in starting_h:
    print(word)

# Word pattern 'ends with'
# From 'my_string' find all words ending with '2'
ending_2 = re.findall(r'\b\w+2\b', my_string)

for word in ending_2:
    print(word)

# Word pattern 'has pattern in between'
# From 'my_string' find all words those have '3' in them
has_3 = re.findall(r'\w*3\w*', my_string)

for c in has_3:
    print(c)

# Word pattern with multiple patterns (using an pattern1 OR pattern2)
# From 'my_string' find all words those have 'ou' OR 'OI' in them
has_3 = re.findall(r'\w*OI\w*|\w*ur\w*', my_string)

for c in has_3:
    print(c)
