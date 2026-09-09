# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Callable function
#  Author       : Team Tinitiate
# ==============================================================================



# Changes behavior of an existing Function
def EmployeeDiscount(bill_amount):
   return bill_amount - 15

def StudentDiscount(bill_amount):
   return bill_amount - 10

def ApplyCoupon(bill_amount, func):
    final_amount = func(bill_amount)
    print(final_amount)

ApplyCoupon(100, EmployeeDiscount)
ApplyCoupon(100, StudentDiscount)
