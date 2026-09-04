# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Multiple pattern matching in a given string
#  Author       : Team Tinitiate
# ==============================================================================



import re

# String pattern match with 'exact word'
# Print 'my_string' if exact word 'Hour32' is found in it
my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'

Hour32 = re.search('Hour32', my_string)
if Hour32:
    print(my_string)
    
# String pattern 'starts with'
# Print 'my_string' if it starts with 'H'
starting_h = re.search('H*$', my_string)

if starting_h:
    print(my_string)

# String pattern 'ends with'
# Print 'my_string' if string ends with '2'
ending_2 = re.search('2$', my_string)

if ending_2:
    print(my_string)

# String with multiple Patterns (using an pattern1 OR pattern2)
# Print 'my_string' if there are words with 'ou' OR 'OI' in them
has_OIur = re.search('OI|ur', my_string)

if has_OIur:
    print(my_string)
