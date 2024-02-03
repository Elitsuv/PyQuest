# if-else.py

"""
Control Flow in Python 🔄

Introduction:
Control flow structures like if statements and loops allow you to control the execution flow of your program.

"""

# If Statements:

# An if statement allows you to conditionally execute a block of code.

# Example:
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loops:

# Loops are used to repeatedly execute a block of code.

# While Loop:

# The while loop repeats a block of code as long as a specified condition is True.

# Example:
counter = 0

while counter < 5:
    print(f"Count: {counter}")
    counter += 1

# For Loop:

# The for loop iterates over a sequence (such as a list, tuple, or string).

# Example:
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(f"Current fruit: {fruit}")

# Range Function:

# The range function generates a sequence of numbers.

# Example:
for number in range(1, 6):
    print(f"Number: {number}")

# Common Errors and Pitfalls:

# Infinite Loops:

# Error: Creating a loop without an exit condition may lead to an infinite loop.

# Example:
# while True:
#     print("This is an infinite loop!")

# Solution: Ensure there's a condition to exit the loop.

# Off-by-One Error:

# Error: Using the wrong range or conditions in loops may result in off-by-one errors.

# Example:
# for i in range(5):
#     print(i)  # This will print 0 to 4, not 1 to 5.

# Solution: Be mindful of the range and conditions.

# PyQuest! 🚀
