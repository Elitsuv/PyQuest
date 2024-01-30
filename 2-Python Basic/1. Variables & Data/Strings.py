
#Introduction:
#In Python, a string is a sequence of characters enclosed in single (' ') or double (" ") quotes.
#Strings are versatile and play a crucial role in various operations, from simple text manipulation to complex data processing.
  

# Basics of Strings:

# Creating Strings:
single_quoted = 'Hello, World!'
double_quoted = "Python is awesome!"

# String Concatenation:
greeting = "Hello"
name = "Alice"
full_greeting = greeting + " " + name

# String Length:
message = "Python is powerful"
length = len(message)

# Common Errors and Pitfalls:

# Misusing Quotes:
# Error: Mixing quotes within a string can lead to syntax errors.
incorrect_string = "This is a 'wrong' string"

# Solution: Use consistent quotes or escape the inner quotes.

# Forgetting Indexing Starts at 0:
# Error: Assuming the first character of a string is at index 1.
text = "Python"
first_char = text[1]  # Incorrect

# Solution: Remember that indexing starts at 0 in Python.

# Not Updating Immutable Strings:
# Error: Attempting to modify a string in place.
word = "Hello"
# word[0] = 'J'  # Incorrect

# Solution: Strings are immutable; create a new one or use slicing.

# Ignoring String Methods:
# Error: Overlooking built-in string methods for manipulation.
text = "   Python   "
# trimmed_text = text.trim()  # Incorrect

# Solution: Use strip(), lower(), upper(), and other string methods as needed.

# Practice Exercises:

# 1. Create a string with your name and print it.
my_name = "John Doe"
print(my_name)

# 2. Concatenate two strings and display the result.
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)

# 3. Calculate the length of a sentence and print it.
sentence = "Python is fascinating and powerful."
length_of_sentence = len(sentence)
print(length_of_sentence)
