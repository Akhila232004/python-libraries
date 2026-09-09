# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Dynamic Generator
#  Author       : Team Tinitiate
# ==============================================================================



def EvenOddNum(MAX):
    num = 0
    while num < MAX:
        num += 1
        if num%2 != 0:
            yield str(num) + " is Odd Number"
        else:
            yield str(num) + " is Even Number"

# Call the function as an iterator
myIter = EvenOddNum(5)

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
# Uncommenting below line Will Error out as MAX is 5 and this is 6TH __next__()
# print(myIter.__next__())
