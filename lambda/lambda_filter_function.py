# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Filter Function Lambda Expressions
#  Author       : Team Tinitiate
# ==============================================================================



# Create a List of Even Numbers Only
evenList = list( filter((lambda x: x%2 == 0), range(10)))
print(evenList)



# Create a List of Salary only > 1000
salary_list = [100, 2000, 300, 4000]
list_1000_PLUS = list( filter((lambda x: x>1000), salary_list))
print(list_1000_PLUS)
