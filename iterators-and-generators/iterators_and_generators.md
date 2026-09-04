![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Iterators and Generators
* Iterators and generators are two fundamental concepts in Python that allow you to work with sequences of data in a more efficient and flexible way.
* Iterators are objects that can be used to iterate over a sequence of data.
* Generators are functions that can be used to generate a sequence of data.

## Iterators
* Iterators are looping constructs that can be applied to data containers such as; strings, lists, and dictionaries and even a CLASS by creating a class iterator.
* The biggest advantage of iterators is there is no boundary, the loop can be closed in any part of the program (or function)
* The iteration is done using `__next__()` function being called one for each iteration, Once the values are exhausted then calling this function will throw an error.
### Iterator with `__next__()` function
```python
# Create a list of data
data_set1 = [1,2,3,4,5]

# Loop or Iterate over this data list using a loop
for value1 in data_set1:
    print(value1)

# Loop or Iterate over this data list using an iterator
# Create an iterator using the `iter()` function
itr = iter(data_set1)

# Call the print to display the next value
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

# Uncommenting below line gives an error as there are no more elements
# print(itr.__next__())

# The biggest advantage is there is no "end loop", see for loop indentation
# We can add more code in between the ".__next__()" providing some flexibility
```
### Iterator with a CLASS
* The CLASS provides `__iter__()` and `__next__()` functions which provides the iterator and gets the next value of the iterator.
* Here we demonstrate a Class with `__iter__()` and `__next__()` functions where in a MAX is specified to limit the iterations and until the MAX is reached it will increment numbers and determine EVEN or ODD starting with "1".
```python
class EvenOddNumbers:
    def __init__(self, max):
        self.max = max
        self.number = 0

    # Override the Iterator to return the class instance
    def __iter__(self):
        return self

    # Return the custom __next__ value specified within this function
    def __next__(self):
    
        # Increment the self.number once every time the __next__() is called
        self.number += 1

        # Exit when the iterations reach the MAX defined in the constructor
        if self.number > self.max:
            print("Max Number of Iterations reached: ", self.max)

        # Check if the CURRENT number is EVEN or ODD and report it
        if self.number%2 != 0:
            print(str(self.number),"is Odd Number")
        else:
            print(str(self.number),"is Even Number")

# Create an object and call the Class with the MAX value, to end the ITERATOR
obj = EvenOddNumbers(5)

# Call the __next__() of the class more than the Max iterations mentioned 5
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
```

## Generators
* Generators are used to create iterators, produces a sequence of values into a iterator.
* Python Generators return an iterator, this is done using the keyword `yield`.
* `yield` is similar to a `return` except that `yield` appends to a LIST of values for an iterator and this iterator generated can be used with `__next__()`.
```python
# Function converted to a generator using yield
def GeneratorDemo():
    yield 22
    yield 33
    yield 44

# Call the function as an iterator
myIter = GeneratorDemo()

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())



# Yield in a loop in the function to use in more scenarios
def GeneratorDemo1():
    for c1 in [1,2,3,4,5]:
        yield c1

# Call the function as an iterator
myIter = GeneratorDemo1()

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())



# Dynamic Generator
def EvenOddNum(MAX):
    num = 0
    while num < MAX:
        num += 1
        if num%2 != 0:
            yield str(num) + " is Odd Number"
        else:
            yield str(num) + " is Even Number"

# Call the function as an iterator
myIter = EvenOddNum(5)

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
# Uncommenting below line Will Error out as MAX is 5 and this is 6TH __next__()
# print(myIter.__next__())
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|