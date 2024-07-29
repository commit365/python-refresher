## 4. Functions

Functions are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable and maintainable.

### Defining Functions

Use the `def` keyword to define a function:

```python 
def greet():     
	print("Hello, World!")
```

## Calling Functions

Invoke a function by its name followed by parentheses:

```python
greet()  # Output: Hello, World!
```

## Function Arguments

Functions can accept parameters to make them more flexible:

```python
def greet(name):
	print(f"Hello, {name}!") 

greet("Alice")  # Output: Hello, Alice!
```

## Default Arguments

Provide default values for parameters:

```python
def greet(name="World"):
	print(f"Hello, {name}!")  
	
greet("Alice")  # Output: Hello, Alice!
	
greet()  # Output: Hello, World! 
```
   
## Keyword Arguments

Pass arguments by parameter name:

```python
def greet(first_name, last_name):     
	print(f"Hello, {first_name} {last_name}!") 
	
greet(last_name="Doe", first_name="John")  # Output: Hello, John Doe!
```

## Return Values

Functions can return values using the `return` statement:

```python
def add(a, b):     
	return a + b 

result = add(5, 3) 
print(result)  # Output: 8
```

## Variable Scope

Variables defined inside a function are local to that function:

```python
def my_function():     
	x = 10  # Local variable    

print(x)  # Error: x is not defined
my_function()
```

## Lambda Functions

Anonymous functions defined using the `lambda` keyword:

```python
add = lambda a, b: a + b 

print(add(5, 3))  # Output: 8
```

## Docstrings

Add documentation to functions using triple quotes:

```python
def greet(name):     
		"""    This function greets the person passed in as a parameter.    """
		print(f"Hello, {name}!") 
		
print(greet.__doc__)
```

## Exercise

1. Write a function `is_even` that takes an integer and returns `True` if the number is even, otherwise `False`.
2. Write a function `factorial` that takes an integer and returns its factorial.

## Key Points

- Functions help in organizing code and making it reusable.
- Parameters can have default values and can be passed by position or keyword.
- Use the `return` statement to return values from functions.
- Lambda functions provide a concise way to create small, anonymous functions.
- Docstrings are used to document what a function does.