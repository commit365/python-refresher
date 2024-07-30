
## 15. Context Managers: Using `with` Statements and Creating Custom Context Managers 

Context managers in Python provide a convenient way to manage resources, ensuring proper acquisition and release, typically used with the `with` statement. 

### Using `with` Statements 

The `with` statement simplifies exception handling by encapsulating common resource management patterns. 

```python 
# File handling with 'with' 
with open('example.txt', 'w') as file:     
	file.write('Hello, World!') # File is automatically closed after the block
```

## Built-in Context Managers

Python provides several built-in context managers:

```python
# Managing locks 
import threading 

lock = threading.Lock() 

with lock:     
	# Critical section 
	pass # replace pass with thread-safe code
```
## Managing database connections

```python
import sqlite3 
 
with sqlite3.connect('example.db') as conn:     
	 cursor = conn.cursor()    
	 # Database operations 
	 # Connection is automatically closed
```

## Creating Custom Context Managers

## Using Classes

Implement `__enter__` and `__exit__` methods:

```python
class CustomContextManager:     
	def __init__(self, filename, mode):        
		self.filename = filename        
		self.mode = mode        
		self.file = None     
		
	def __enter__(self):        
		self.file = open(self.filename, self.mode)        
		return self.file     
	
	def __exit__(self, exc_type, exc_val, exc_tb):        
		if self.file:            
			self.file.close()        
		# Return True to suppress exceptions, False otherwise        
		return False 

# Usage 
with CustomContextManager('example.txt', 'w') as file:     
	file.write('Hello from custom context manager!')
```

## Using `contextlib`

The `contextlib` module provides utilities for working with context managers:

```python
from contextlib import contextmanager 

@contextmanager 
def file_manager(filename, mode):     
	try:        
		file = open(filename, mode)        
		yield file    
	finally:        
		file.close() 
		
# Usage 
with file_manager('example.txt', 'w') as file:     
	file.write('Hello from contextlib!')
```

## Nested Context Managers

Context managers can be nested:

```python
with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:    
	content = file1.read()    
	file2.write(content)
```

## Practical Examples

## Database Transaction Manager

```python
import sqlite3 

from contextlib import contextmanager 

@contextmanager 
def transaction(connection):     
	cursor = connection.cursor()    
	try:        
		yield cursor        
		connection.commit()    
	except:        
		connection.rollback()        
		raise    
	finally:        
		cursor.close() 
		
# Usage 
conn = sqlite3.connect('example.db') 
with transaction(conn) as cursor:     
	cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
```

## Timer Context Manager

```python
import time 
from contextlib import contextmanager 

@contextmanager 
def timer():     
	start_time = time.time()    
	yield    
	end_time = time.time()    
	print(f"Execution time: {end_time - start_time:.2f} seconds") 
	
# Usage 
with timer():     
	# Code to be timed    
	time.sleep(2)
```

## Exercise

1. Create a context manager that temporarily changes the working directory.
2. Implement a context manager for managing a network connection.
3. Write a context manager that suppresses specific exceptions and logs them.

## Key Points

- Context managers ensure proper resource management.
- The `with` statement simplifies usage of context managers.
- Custom context managers can be created using classes or the `contextlib` module.
- Context managers are useful for file I/O, database connections, locks, and more.
- They help in writing cleaner, more readable, and error-resistant code.
