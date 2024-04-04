# Exercise:

# 1. Write a function named 'square' that takes a number as input and returns its square.

# 2. Define a function 'average' that calculates the average of two numbers passed as arguments.

# 3. Create a function 'is_even' that checks if a given number is even. It should return True if the number is even, otherwise False.

# 4. Implement a function 'factorial' that computes the factorial of a given number. The factorial of a number n is the product of all positive integers less than or equal to n.

# 5. Write a function 'reverse_string' that takes a string as input and returns the reverse of the string.

# Answers:

# 1.
def square(num):
    return num ** 2

# 2.
def average(num1, num2):
    return (num1 + num2) / 2

# 3.
def is_even(num):
    return num % 2 == 0

# 4.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 5.
def reverse_string(string):
    return string[::-1]

# PyQuest! 🚀