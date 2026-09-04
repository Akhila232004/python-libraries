# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Function Wrappers
#  Author       : Team Tinitiate
# ==============================================================================



# Parent function
# This is the function whose function should be enhanced
def AddTWONums(Num1,Num2):
    return Num1+Num2;

# Enhance functionality by a wrapper function
# Change the parent functions functionality
# Call the function "AddTWONums" inside the wrapper
def add3Nums_1(Num1,Num2,Num3):

    # Call the parent function inside the add3Nums_1
    return AddTWONums( AddTWONums(Num1,Num2) ,
                       Num3)

# Called the add3Nums_1 function
print(add3Nums_1(1,2,3))
