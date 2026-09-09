# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Passing function as parameter to another function
#  Author       : Team Tinitiate
# ==============================================================================



# Function "add5" adds 5 to input number
def add5(num1):
   return num1+5

def addSpl(num1, num2):
    return num1+num2

# Function that accepts another function as an input parameter
def addTwoNums(func):
    num1 = 1
    num2 = 2
    
    # Return the parameter, by passing another parameter "num1"
    if func == add5:
        return func(num1)
        
    elif func == addSpl:
        return func(num1, num2)

# Calling "addTwoNums" function with "add5" function as input parameter
print(addTwoNums(add5))
print(addTwoNums(addSpl))
