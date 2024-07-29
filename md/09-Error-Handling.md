
## 9. Error Handling: Exception Handling and Debugging Techniques 

Error handling is crucial for writing robust Python programs. It allows you to gracefully manage unexpected situations and provide meaningful feedback. 

### Exception Handling 

#### Basic Try-Except Block 

```python 
try:     
	result = 10 / 0 
except ZeroDivisionError:     
	print("Cannot divide by zero!")
```

## Handling Multiple Exceptions

```python
try:     
	number = int(input("Enter a number: "))    
	result = 10 / number 
except ValueError:     
	print("Invalid input. Please enter a number.") 
except ZeroDivisionError:     
	print("Cannot divide by zero!")
```

## The Else Clause

Executed if no exception occurs:

```python
try:     
	number = int(input("Enter a number: ")) 
except ValueError:     
	print("Invalid input") 
else:     
	print(f"You entered: {number}")
```

## The Finally Clause

Always executed, regardless of whether an exception occurred:

```python
try:     
	file = open("example.txt", "r")    # File operations here 
except FileNotFoundError:     
	print("File not found") 
finally:     
	file.close()  # This will always execute
```

## Raising Exceptions

```python
def validate_age(age):     
	if age < 0:        
		raise ValueError("Age cannot be negative")    
	return age 
		
try:     
	validate_age(-5) 
except ValueError as e:     
	print(e)
```

## Debugging Techniques

## Print Debugging

Insert print statements to track program flow and variable values:

```python
def complex_function(x, y):     
	print(f"Inputs: x={x}, y={y}")  # Debug print    
	result = x * y    
	print(f"Result: {result}")  # Debug print    
	return result
```

## Using the `assert` Statement

```python
def calculate_average(numbers):     
	assert len(numbers) > 0, "List is empty"    
	return sum(numbers) / len(numbers)
```

## Python Debugger (pdb)

Use `pdb` for interactive debugging:

```python
import pdb 

def complex_function(x, y):     
	result = x * y    
	pdb.set_trace()  # Debugger will start here    
	return result 

complex_function(3, 4)
```

Common pdb commands:

- `n` (next line)
- `s` (step into function)
- `c` (continue execution)
- `p variable` (print variable value)
- `q` (quit debugger)

## Logging

Use the `logging` module for more sophisticated debugging:

```python
import logging 

logging.basicConfig(level=logging.DEBUG) 

def complex_function(x, y):     
	logging.debug(f"Function called with x={x}, y={y}")    
	result = x * y    
	logging.info(f"Function returning {result}")    
	return result 
	
complex_function(3, 4)
```

## Exercise

1. Write a function that takes two numbers as input and returns their division.
2. Implement proper exception handling to deal with zero division and invalid input (non-numeric input).
3. Add logging to your function to track its usage.
4. Use `assert` to ensure both inputs are positive numbers.

## Key Points

- Use try-except blocks to handle specific exceptions.
- The `else` clause in a try-except block runs if no exception occurs.
- The `finally` clause always runs, whether an exception occurred or not.
- Use `raise` to throw exceptions when necessary.
- Print debugging, assertions, `pdb`, and logging are valuable debugging tools.
- Choose the appropriate debugging technique based on the complexity of the issue and the development stage.