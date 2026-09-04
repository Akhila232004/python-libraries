![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Advanced Function Features
* Python have advanced function features that allow you to create more complex and powerful functions.

## Simple Function
```python
def Add2Nums(Num1,Num2):
    return Num1+Num2;

print(Add2Nums(1,2))
```

## Nested Function
* A Nested Function is a function inside a function.
* This is useful when you want to create a function that does more than one task.
```python
def add2numsAndFive(num1,num2):
    
    # Inner Function or Nested Function `Add5`
    def Add5(num):
        return num+5;

    return Add5(num1+num2)
# Function end

# Call the function `add2numsAndFive`
print(add2numsAndFive(1,2))
```

## Passing function as parameter to another function
```python
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
```

## Function returns another function as output
```python
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
```

## Function Wrappers
* A Functions "Functionality" can be enhanced without changing the function.
* The easy option to enhance a function is by calling the function as an inner function in another function which is called the wrapper or outer function.
* A function wrapper is a higher-order function that returns a new function which calls the original function and augments its behavior without modifying the original’s source.
```python
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
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|