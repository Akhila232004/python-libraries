![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# `input()` Function
* Reading keyboard input in Python can be done using various approaches, but one common method is by utilizing the `input()` function. The `input()` function allows you to prompt the user for text input through the keyboard and store the entered text as a string.
* Using the `input()` function, you can easily interact with users through the keyboard, gather input, and create interactive command-line programs.

## Using the `input()` Function
* The `input()` function displays a prompt to the user and waits for keyboard input. Once the user enters something and presses the ***Enter*** key, the input is captured and returned as a string.
```python
user_input = input("Please enter your name: ")
print(f"Hello, {user_input}!")
```
* In the above, the user is prompted to enter their name, and whatever they type is stored in the `user_input` variable. The entered name is then displayed in a greeting.

## Handling Numerical Input
* When expecting numerical input, you can use the `input()` function and then convert the input string to the desired numeric data type (like `int` or `float`) using the appropriate casting functions.
```python
age_str = input("Please enter your age: ")
age = int(age_str)
print(f"You are {age} years old.")
```

## Reading Single Line Input
* Input text is captured until an **Enter** or **NewLine** character is encountered.
```python
# Reading single line user input using "input"
l_UserInput = input("Enter text and press enter: ")
print ("text entered " + l_UserInput)
```

## Reading Multi Line Input
* Multi line input is captured until a ***termination*** string is encountered, **termination** can be defined to be any text string.
* The ***termination*** String is case sensitive.
```python
l_UserInput = ""
terminate_str = ":END"  # Termination String ':END'

print("Enter multiline user input, Please enter the string ':END'")
print("to terminate reading input")
while True:
    data = input()
    if data.strip() == terminate_str:
        break
    l_UserInput += "%s\n" % data

print(l_UserInput)
```

## Reading Python Script Command Line Arguments
* When executing a Python script at the Commandline arguments, we use `python file_name.py`
* Values can be passed to the python script, and these values are called as arguments, They are passed as below example:
```bash
python file-name.py argument1 argument2 ...
```
* Python script arguments can be read using the `sys.argv`
```python
import sys

# The 'sys.argv' returns all the arguments to this list.
commandline_args_list = sys.argv

print(commandline_args_list)

# Call the program using
# python command_line_arguments.py argument1 argument2
```

## Handling Special Keys
* The `input()` function reads text input until the ***Enter*** key is pressed. It doesn't capture special keys like arrow keys, function keys, or modifier keys (Ctrl, Shift, etc.). For capturing more complex keyboard interactions, you might need to use external libraries like 'curses', 'keyboard' or 'readline'.

## Safe input validation
* Input is always read as strings, so you might need to convert it to other data types if necessary.
* Be cautious of user input. Always validate and sanitize user input before using it, especially if it will be used in critical operations.
```python
while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
```
* In the above, the code keeps prompting the user until a valid number is entered.




##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|