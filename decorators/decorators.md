![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Decorators
* Decorators are a powerful feature in Python that allow you to modify the behavior of functions, classes, or modules without having to modify their source code.
* Decorators are functions that take another function as input and return a new function as output.
* They act as a wrapper to an existing function, modifying its behavior.
* Also called as meta programming, the wrapping action happens at the compile time.

## Built-in Class Decorators
* Python provides a mechanism to call class functions WITHOUT creating a class Object, this is done through two decorators `@staticmethods` and `@classmethod`.
* Any function 'decorated' with `@staticmethod` is callable without instantiating the class. It’s definition is immutable via inheritance.
* `@staticmethods` is a class decorator, that enables a class function to be used without creating an object, This neither accepts a self (the object instance) nor the class is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class.
* `@classmethod` is a decorator when used provides a function in a class, as the class object to work on instead of the class instance. Enables to call a classes method with out creating an object with `@classmethods`, the class of the object instance is implicitly passed as the first argument instead of self.
```python
# Create class with two methods
class tinitiate:
    "Class to demonstrate @classmethod and @staticmethod Decorations"

    # Decorated using the `@classmethod`
    @classmethod
    def class_function(cls, x):
        print(cls, x)

    # Decorated using the `@staticmethod`
    # No need to pass the "self" (the object instance) for static method
    @staticmethod
    def static_function(x):
        print(x)

# Create an object of the class tinitiate
obj = tinitiate()

# Call the "CLASS_FUNCTION" using the object
obj.class_function("Class Object Test")

# Call the "STATIC_FUNCTION" using the object
obj.static_function("Static Object Test")

# Call the "STATIC_FUNCTION" directly without the object
tinitiate.static_function("Static Test")

# Call the "CLASS_FUNCTION" directly without the object
tinitiate.class_function("Class Test")
```

## User-defined Decorators
* Demonstration of **Callable Function**, changes behavior of an existing Function
* Demonstration of User-defined decorators to change behavior of an existing Function
* Demonstration of multiple decorators that are chained in Python
```python
# Callable function 
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



# User-defined decorator
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
```

## Custom Decorators with Parameters or Arguments
* We can pass arguments to a Decorator and also change the data that goes into the base function which uses the decorator.
```python
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
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|