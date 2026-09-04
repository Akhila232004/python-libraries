# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Nested Function
#  Author       : Team Tinitiate
# ==============================================================================



def add2numsAndFive(num1,num2):
    
    # Inner Function or Nested Function `Add5`
    def Add5(num):
        return num+5;

    return Add5(num1+num2)
# Function end

# Call the function `add2numsAndFive`
print(add2numsAndFive(1,2))
