
## 8. Modules and Packages 

Modules and packages in Python help organize and reuse code. They allow you to logically organize your code and make it more maintainable. 

### Modules 
A module is a file containing Python definitions and statements. 

#### Importing Modules 

```python 
# Import the entire module 
import math 

print(math.pi)  # Output: 3.141592653589793 

# Import specific functions 
from math import sqrt, sin 

print(sqrt(16))  # Output: 4.0 

# Import with an alias 
import math as m 

print(m.cos(0))  # Output: 1.0 

# Import all functions (not recommended) 
from math import *
```

## Creating a Module

Create a file named `mymodule.py`:

```python
# mymodule.py 
def greet(name):     
	return f"Hello, {name}!" 

PI = 3.14159
```

Using the module:

```python
import mymodule 

print(mymodule.greet("Alice"))  # Output: Hello, Alice! 
print(mymodule.PI)  # Output: 3.14159
```

## Packages

A package is a way of organizing related modules into a directory hierarchy.

## Creating a Package

Create a directory with an `__init__.py` file:

```text
mypackage/     __init__.py    module1.py    module2.py
```

The `__init__.py` file can be empty or can initialize the package.

## Importing from Packages

```python
# Import a module from a package 
from mypackage import module1 

# Import a specific function from a module in a package 
from mypackage.module2 import some_function
```

## Standard Libraries

Python comes with a rich set of standard libraries:

```python
# Working with dates 
import datetime 

print(datetime.date.today()) 

# Working with JSON 
import json 

data = json.dumps({"name": "John", "age": 30}) 
print(data) 

# Regular expressions 
import re 

pattern = r'\d+' 
print(re.findall(pattern, "There are 123 apples and 456 oranges"))  # Output: ['123', '456']
```

## The `if __name__ == "__main__":` Idiom

This idiom allows you to execute code only when the file is run directly, not when it's imported as a module:

```python
# In mymodule.py 
def some_function():     
	print("This function is always available") 

if __name__ == "__main__":     
	print("This runs only if the file is executed directly")
```

## Exercise

1. Create a package named `geometry` with two modules: `shapes` and `calculations`.
2. In `shapes`, define classes for `Circle` and `Rectangle`.
3. In `calculations`, define functions to calculate area and perimeter for these shapes.
4. Create a main script that imports and uses these modules to calculate the area and perimeter of a circle and a rectangle.

## Key Points

- Modules are single files, while packages are directories of modules.
- Use `import` to access code from other modules or packages.
- The standard library provides a wide range of useful modules.
- Create `__init__.py` in a directory to make it a package.
- Use `if __name__ == "__main__":` to include code that runs only when the file is executed directly.
