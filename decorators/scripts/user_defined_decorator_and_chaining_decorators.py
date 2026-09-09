# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : User-defined decorator and Chaining decorators
#  Author       : Team Tinitiate
# ==============================================================================



# Implementing the same using decorators 
def EmpDiscount(func):
   def inner(bill_amount): # inner or use any name
      print("Applying Employee Discount")
      return func(bill_amount - 15)
   return inner

def StuDiscount(func):
   def inner(bill_amount):
      print("Applying Student Discount")
      return func(bill_amount - 10)
   return inner

# Create functions with decorators
# Create one function for each of the decorator
@EmpDiscount   
def CouponApply1(bill_amount):
    print(bill_amount)

@StuDiscount   
def CouponApply2(bill_amount):
    print(bill_amount)

# Test the Decorators
CouponApply1(100)
CouponApply2(100)



# Chaining decorators
# Multiple decorators can be chained in Python
@EmpDiscount
@StuDiscount
def CouponApply3(bill_amount):
    print(bill_amount)

# Test the Decorators
CouponApply3(100)
