![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Lambda
* Lambdas Expressions or Lambdas are one liner syntax to create anonymous functions called Lambdas, They allow functionality and data to be passed around in a single line.
* Python's `lambda`, `map()`, `filter()`, and `reduce()` functions are built-in functions that are widely used in functional programming. 
* These functions are used for working with iterables such as lists, tuples, and dictionaries. 
* They provide an efficient and concise way of manipulating the data.
* A `lambda` function is a small anonymous built-in function that can have any number of arguments, but can only have one expression.
* They allow functionality and  data to be passed around in a single line.
* They provide a shortcut to expressions, LOOP and IF..ELSE conditions.
```python
# Demonstration of normal function and its `lambda` equivalent
# Function to Add 2 Numbers
def Add2Nums(Num1, Num2):
    return Num1+Num2;
print(Add2Nums(1,3))

# Lambda function
# Function to Add 2 Numbers
AddLda = lambda x,y: x+y
print(AddLda(1,3))



# Demonstration of `lambda` with IF..ELSE condition
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
```

## Map Function with Lambda Expressions
* The `map()` function applies a given function to each item of an iterable (e.g., list, tuple) and returns a new iterable with the results.
    * **Syntax:** map(function, iterable)
* It executes the function_object for each element in the source iteration and returns a list of the elements modified by the source function(s)
```python
# Map single function with an iteration with lambda
sequence = [2, 3, 4, 5, 6]
y = list(map(lambda v : v * 5, sequence))
print(y)



# Map multiple functions with an iteration with lambda
def Add2(x):
        return (x+2)

def Add3(x):
        return (x+3)

MyFunctions = [Add2, Add3]

for num in range(5):
    print(num)
    data = list(map(lambda x: x(num), MyFunctions))
    print(data)
```

## Filter Function with Lambda Expressions
* The `filter()` function applies a given function to each item of an iterable and returns a new iterable with the items for which the function returns `True`.
* Filter function works with two arguments a Function and Source iterable.
    * **Syntax:** filter(function, iterable)
* The function is called for each element of the iterable with filter returning only elements which qualify for a given condition.
* Unlike map function filter function can only have one iterable as input.
```python
# Create a List of Even Numbers Only
evenList = list( filter((lambda x: x%2 == 0), range(10)))
print(evenList)



# Create a List of Salary only > 1000
salary_list = [100, 2000, 300, 4000]
list_1000_PLUS = list( filter((lambda x: x>1000), salary_list))
print(list_1000_PLUS)
```

## Reduce Function with Lambda Expressions
* The `reduce()` function applies a given function to the first two items of an iterable, then applies the function to the result and the next item, and so on, until all items have been processed.
    * **Syntax:** reduce(function, iterable)
* Import `reduce` from `functools`.
```python
from functools import reduce

addData = reduce((lambda x,y:x+y),range(10))
print(addData)

mulData = reduce((lambda x,y:x*y),range(1,10))
print(mulData)
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|