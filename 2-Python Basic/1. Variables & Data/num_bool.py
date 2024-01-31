Numbers and Bool
"""
Numeric and Boolean Data Types in Python 🧮

Introduction:
In Python, numeric data types include integers (`int`) and floating-point numbers (`float`).
Additionally, there's a boolean data type (`bool`) representing True or False values.
"""

# Integers (`int`)

# Definition:
# Integers are whole numbers without a fractional component. They can be positive or negative.

# Example:
my_integer = 42
negative_integer = -7

# Floating-Point Numbers (`float`)

# Definition:
# Floating-point numbers represent real numbers with decimal points or in exponential form.

# Example:
my_float = 3.14
negative_float = -0.5

# Booleans (`bool`)

# Definition:
# Booleans represent the truth values True or False.

# Example:
is_python_fun = True
is_learning_python = False

# Common Errors and Pitfalls

# Mixing Data Types:

# Error: Performing operations between different data types without proper conversion.
result_mixing_types = 5 + 2.0  # Incorrect
# Solution: Ensure consistent data types or convert explicitly.

# Division Pitfalls:

# Error: Unexpected results in division due to integer division behavior.
result_division_pitfall = 5 / 2  # Incorrect (yields 2.5 in Python 3.x)
# Solution: Use explicit casting or use `//` for floor division.

# Misuse of Booleans:

# Error: Treating booleans as integers in arithmetic operations.
result_boolean_misuse = True + True  # Incorrect
# Solution: Use booleans in logical operations, not arithmetic.

# Floating-Point Precision:

# Error: Expecting exact precision in floating-point operations.
result_floating_point_precision = 0.1 + 0.2  # May yield unexpected result
# Solution: Be aware of floating-point precision limitations.

# Practice Exercises

# 1. Create an integer variable and a floating-point variable. Perform arithmetic operations on them.
integer_variable = 10
float_variable = 3.5
result_arithmetic_operations = integer_variable + float_variable

# 2. Compare two numbers and store the result in a boolean variable.
number1 = 15
number2 = 20
comparison_result = number1 > number2

# 3. Calculate the average of three numbers and ensure the result is a float.
num1 = 5
num2 = 10
num3 = 15
average_result = (num1 + num2 + num3) / 3.0

# Pyquest
