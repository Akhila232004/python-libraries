# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Iterator with a CLASS
#  Author       : Team Tinitiate
# ==============================================================================



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
