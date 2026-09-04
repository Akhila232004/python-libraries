# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Function converted to a generator using yield
#  Author       : Team Tinitiate
# ==============================================================================



def GeneratorDemo():
    yield 22
    yield 33
    yield 44

# Call the function as an iterator
myIter = GeneratorDemo()

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
