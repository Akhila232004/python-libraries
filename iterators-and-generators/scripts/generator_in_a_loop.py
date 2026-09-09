# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Yield in a loop in function to use in more scenarios
#  Author       : Team Tinitiate
# ==============================================================================



def GeneratorDemo1():
    for c1 in [1,2,3,4,5]:
        yield c1

# Call the function as an iterator
myIter = GeneratorDemo1()

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
