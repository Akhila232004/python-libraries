# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : split() Function
#  Author       : Team Tinitiate
# ==============================================================================



import re

words2list = re.split(r's','Tinitiate good python examples')
print(words2list)

# Split a Comma Separated String
csv2list = re.split(r',','1,AAA,2000')
print(csv2list)
