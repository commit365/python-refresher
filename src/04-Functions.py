# Define Function
def greet():     
	print("Hello, World!")
	
# Call Function
greet()  # Output: Hello, World!

# Function Argument
def greet(name):
	print(f"Hello, {name}!") 

greet("Alice")  # Output: Hello, Alice!

# Default Argument
def greet(name="World"):
	print(f"Hello, {name}!")  
	
greet("Alice")  # Output: Hello, Alice!
	
greet()  # Output: Hello, World! 

# Keyword Arguments
def greet(first_name, last_name):     
	print(f"Hello, {first_name} {last_name}!") 
	
greet(last_name="Doe", first_name="John")  # Output: Hello, John Doe!

# Return Values
def add(a, b):     
	return a + b 

result = add(5, 3) 
print(result)  # Output: 8

# Variable Scope
def my_function():     
	x = 10  # Local variable    

# print(x)  # Error: x is not defined
my_function()

# Lambda Function
add = lambda a, b: a + b 

print(add(5, 3))  # Output: 8

# Docstring
def greet(name):     
		"""    This function greets the person passed in as a parameter.    """
		print(f"Hello, {name}!") 
		
print(greet.__doc__)

# Exercises
# 1. Write a function is_even that takes an integer and returns True if the number is even, otherwise False.
def is_even(x):
	return x % 2 == 0

print("2 is even: ", is_even(2))
print("3 is even:", is_even(3))

# 2. Write a function factorial that takes an integer and returns its factorial.
def factorial(n):
	if n < 0:
		return 0  # Should ideally return error as factorial is defined only for non-negative numbers
	elif n == 0 or n == 1:
		return 1
	else:
		result = 1
		for i in range(n):
			result *= i+1
		return result

print("-1! =", factorial(-1)) 
print("0! =", factorial(0)) 
print("1! =", factorial(1)) 
print("2! =", factorial(2)) 
print("3! =", factorial(3)) 
print("4! =", factorial(4)) 