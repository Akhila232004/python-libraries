# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Demonstration of normal function and its `lambda` equivalent
#  Author       : Team Tinitiate
# ==============================================================================



# Function to Add 2 Numbers
def Add2Nums(Num1, Num2):
    return Num1+Num2;
print(Add2Nums(1,3))

# Lambda function
# Function to Add 2 Numbers
AddLda = lambda x,y: x+y
print(AddLda(1,3))
