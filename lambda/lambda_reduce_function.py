# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Reduce Function with Lambda Expressions
#  Author       : Team Tinitiate
# ==============================================================================



from functools import reduce

addData = reduce((lambda x,y:x+y),range(10))
print(addData)

mulData = reduce((lambda x,y:x*y),range(1,10))
print(mulData)
