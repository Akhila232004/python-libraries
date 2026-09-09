# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : defaultdict()
#  Author       : Team Tinitiate
# ==============================================================================



from collections import defaultdict

food = defaultdict(lambda: 'Bread')
food['Breakfast'] = 'cereal'
food['Lunch'] = 'Pizza'
print(food['Breakfast'])
print(food['Lunch'])

# Get Value of Key, that doesnt exist
print(food['Dinner'])
