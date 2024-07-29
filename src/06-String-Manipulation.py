# String Manipulation

# Create Strings
s1 = 'Hello' 
s2 = "World" 
s3 = '''This is a multi-line 
string'''

# String Concatenation
greeting = s1 + ", " + s2 
print(greeting)  # Output: Hello, World

# String Indexing and Slicing
s = "Python" 
print(s)  # Output: Python 
print(s[1:4])  # Output: yth 
print(s[::-1])  # Output: nohtyP (reverse)

# String Methods
s = "hello, world" 
print(s.upper())  # Output: HELLO, WORLD 
print(s.capitalize())  # Output: Hello, world 
print(s.title())  # Output: Hello, World 
print(s.strip())  # Removes leading/trailing whitespace 
print(s.split(','))  # Output: ['hello', ' world'] 
print(','.join(['a', 'b', 'c']))  # Output: a,b,c 
print(s.replace('o', '0'))  # Output: hell0, w0rld

# String Formatting
# f-strings (Python 3.6+)
name = "Alice" 
age = 30 
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# %-formatting (older style)
print("My name is %s and I am %d years old." % (name, age))

# String Operations
# Repetition 
print("Ha" * 3)  # Output: HaHaHa 

# Membership test 
print('a' in 'abc')  # Output: True 

# Length 
print(len("Python"))  # Output: 6

# Raw Strings
print(r"C:\Users\name")  # Output: C:\Users\name

## Exercises

# 1. Create a string containing a sentence.
quote = "Be the change that you wish to see in the world. — Mahatma Gandhi"
print(quote)

# 2. Convert the string to uppercase and then to title case.
upper_quote = quote.upper()
print(upper_quote)
title_quote = upper_quote.title()
print(title_quote)

# 3. Split the string into a list of words.
split_quote = quote.split(" ")
print(split_quote)

# 4. Join the words back into a string, separating them with hyphens.
hyphen_quote = '-'.join(split_quote)
print(hyphen_quote)

# 5. Replace all occurrences of a specific character in the string.
replace_quote = quote.replace('o', '0')
print(replace_quote)