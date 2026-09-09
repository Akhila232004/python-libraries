# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : ChainMap()
#  Author       : Team Tinitiate
# ==============================================================================



import collections

# initializing dictionaries
e1 = { 'Emp1' : 1, 'Emp2' : 2 }
e2 = { 'Emp3' : 3, 'Emp4' : 4 }

# initializing ChainMap
chain = collections.ChainMap(e1, e2)

# printing chainMap using maps
print(chain.maps)

# printing keys using keys()
print(list(chain.keys()))

# printing keys using keys()
print(list(chain.values()))

# use new_child() to add new dictionary
e3 = { 'Emp5' : 5, 'Emp6' : 6 }
chain = chain.new_child(e3)
