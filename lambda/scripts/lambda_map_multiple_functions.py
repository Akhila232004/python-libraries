# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Map multiple functions with an iteration with lambda
#  Author       : Team Tinitiate
# ==============================================================================



def Add2(x):
        return (x+2)

def Add3(x):
        return (x+3)

MyFunctions = [Add2, Add3]

for num in range(5):
    print(num)
    data = list(map(lambda x: x(num), MyFunctions))
    print(data)
