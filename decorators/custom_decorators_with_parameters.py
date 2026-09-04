# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Custom Decorators with Parameters or Arguments
#  Author       : Team Tinitiate
# ==============================================================================



# Create decorator with argument
def decorator_coupon(N1):
    def wrap(f):
        def wrapped_f(A):
            return f(A - N1)
        return wrapped_f
    return wrap    

# Use decorator with function declaration
@decorator_coupon(15)
def GetFinalPrice1(A):
    print(A)

@decorator_coupon(25)
def GetFinalPrice2(A):
    print(A)

# Applying multiple decorators on a single function declaration
@decorator_coupon(15)
@decorator_coupon(25)
def MultipleCoupons(A):
    print(A)
    
# Call the function with decorators
GetFinalPrice1(100)
GetFinalPrice2(100)
MultipleCoupons(100)
