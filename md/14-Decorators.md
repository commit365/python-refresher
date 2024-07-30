
## 14. Decorators: Understanding and Using Decorators 

Decorators in Python are a powerful way to modify or enhance functions or classes without directly changing their source code. They use the `@` symbol followed by the decorator name. 
### Basic Decorator 

A decorator is a function that takes another function as an argument and returns a new function. 

```python 
def simple_decorator(func):     
	def wrapper():        
		print("Something is happening before the function is called.")        
		func()        
		print("Something is happening after the function is called.")    
	return wrapper 

@simple_decorator 
def say_hello():     
	print("Hello!") 

say_hello() 

# Output:
# Something is happening before the function is called. 
# Hello! 
# Something is happening after the function is called.
```

## Decorators with Arguments

Decorators can also accept arguments from the decorated function.

```python
def decorator_with_args(func):     
	def wrapper(*args, **kwargs):        
		print(f"Positional arguments: {args}")        
		print(f"Keyword arguments: {kwargs}")        
		return func(*args, **kwargs)    
	return wrapper 
	
@decorator_with_args 
def greet(name, greeting="Hello"):     
	print(f"{greeting}, {name}!") 

greet("Alice", greeting="Hi") 

# Output: 
# Positional arguments: ('Alice',) 
# Keyword arguments: {'greeting': 'Hi'} 
# Hi, Alice!
```

## Decorators with Parameters

Decorators can also accept their own parameters.

```python
def repeat(times):     
	def decorator(func):        
		def wrapper(*args, **kwargs):            
			for _ in range(times):                
				result = func(*args, **kwargs)            
			return result        
		return wrapper    
	return decorator 
	
@repeat(times=3) 
def say_hi(name):     
	print(f"Hi, {name}!") 

say_hi("Bob") 

# Output: 
# Hi, Bob! 
# Hi, Bob! 
# Hi, Bob!
```

## Class Decorators

Decorators can be applied to classes as well.

```python
def singleton(cls):     
	instances = {}    

	def get_instance(*args, **kwargs):        
		if cls not in instances:            
			instances[cls] = cls(*args, **kwargs)        
		return instances[cls]    
		
	return get_instance 

@singleton 
class DatabaseConnection:     
	def __init__(self):        
		print("Initializing database connection") 

# Only one instance is created 
db1 = DatabaseConnection() 
db2 = DatabaseConnection() 

print(db1 is db2)  # Output: True
```

## Practical Examples

## Timing Function Execution

```python
import time 

def timing_decorator(func):     
	def wrapper(*args, **kwargs):        
		start_time = time.time()        
		result = func(*args, **kwargs)        
		end_time = time.time()        
		print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")        
		return result    
	return wrapper 

@timing_decorator 
def slow_function():     
	time.sleep(2) 

slow_function() 

# Output: slow_function took 2.00 seconds to execute.
```

## Memoization

```python
def memoize(func):     
	cache = {}    
	def wrapper(*args):        
		if args in cache:            
			return cache[args]        
		result = func(*args)        
		cache[args] = result        
		return result    
	return wrapper 

@memoize 
def fibonacci(n):     
	if n < 2:        
		return n    
	return fibonacci(n-1) + fibonacci(n-2) 
	
print(fibonacci(100))  # Calculates quickly due to memoization
```

## Exercise

1. Create a decorator that logs the arguments and return value of a function.
2. Implement a decorator that retries a function a specified number of times if it raises an exception.
3. Write a decorator that checks if the arguments to a function are of a specific type.

## Key Points

- Decorators modify or enhance functions or classes without changing their source code.
- They are denoted by the `@` symbol followed by the decorator name.
- Decorators can accept arguments from both the decorated function and as their own parameters.
- Class decorators can modify class behavior.
- Common uses include logging, timing, memoization, and access control.
