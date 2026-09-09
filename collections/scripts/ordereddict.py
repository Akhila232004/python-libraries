# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : OrderedDict()
#  Author       : Team Tinitiate
# ==============================================================================



from collections import OrderedDict

print("Regular Dict:")
d1 = {}
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3
d1['d'] = 4
d1['e'] = 5

for key, value in d1.items():
    print(key, value)

print("Ordered Dict:")
od1 = OrderedDict()
od1['a'] = 1
od1['b'] = 2
od1['c'] = 3
od1['d'] = 4
od1['e'] = 5

for key, value in od1.items():
    print(key, value)
