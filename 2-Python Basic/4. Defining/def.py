"""
Defining Functions in Python 📝

Introduction:
Functions in Python allow you to encapsulate blocks of code for reuse, promoting modularity and maintainability in your programs. They enable you to break down complex tasks into smaller, manageable parts, making your code more readable and easier to maintain. With functions, you can improve the efficiency of your code by avoiding repetition and promoting the "Don't Repeat Yourself" (DRY) principle.

"""

# Function Definition:

# Functions allow you to encapsulate blocks of code for reuse.

# Syntax:
def greet(name):
    """
    This function greets the user with the given name.
    
    Parameters:
    - name (str): The name of the user to greet.
    
    Returns:
    - str: A greeting message containing the user's name.
    """
    return f"Hello, {name}!"

# Explanation:
# - The def keyword marks the start of a function definition.
# - The function name (greet) follows def.
# - Parameters (name) are specified within parentheses.
# - The colon (:) indicates the start of the function body.
# - The return statement specifies the value the function should return.

# Example:
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Function with Default Parameter:

# You can specify default values for function parameters.

# Example:
def greet_with_default(name="World"):
    """
    This function greets the user with the given name or "World" if no name is provided.
    
    Parameters:
    - name (str, optional): The name of the user to greet. Defaults to "World".
    
    Returns:
    - str: A greeting message containing the user's name.
    """
    return f"Hello, {name}!"

# Example:
message = greet_with_default()
print(message)  # Output: Hello, World!

message = greet_with_default("Bob")
print(message)  # Output: Hello, Bob!

# Function with Multiple Parameters:

# Functions can accept multiple parameters separated by commas.

# Example:
def add_numbers(x, y):
    """
    This function adds two numbers.
    
    Parameters:
    - x (int): The first number.
    - y (int): The second number.
    
    Returns:
    - int: The sum of the two numbers.
    """
    return x + y

# Example:
result = add_numbers(3, 5)
print(result)  # Output: 8

# PyQuest! 🚀 
