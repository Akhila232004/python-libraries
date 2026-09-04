# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Function returns another function as output
#  Author       : Team Tinitiate
# ==============================================================================



def AddNumWith5(Num1):
    
    # Nested function
    def Add5():
        return Num1+5

    # Return the "Add5" function
    return Add5

# Capture the returned function into add_5,
# and add_5 is an object not a variable
add_5 = AddNumWith5(5)

# Printing add_5() (printing as a function)
print(add_5())  # OUTPUT: 10

# Printing add_5 (printing as a variable)
print(add_5)    # OUTPUT: Some Object Address
