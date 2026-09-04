# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Demonstration of `lambda` with IF..ELSE condition
#  Author       : Team Tinitiate
# ==============================================================================



# Normal function
def EvenOrOdd(Num1):
    if(Num1%2 == 0):
        return "EVEN";
    else:
        return "ODD";
print(EvenOrOdd(12))

# Lambda function
EvenOrOddLda = lambda x: 'EVEN' if(x%2==0) else 'ODD'
print(EvenOrOddLda(12))
