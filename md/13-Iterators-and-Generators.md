
## 13. Iterators and Generators: Creating and Using Iterators and Generators 

Iterators and generators are powerful tools in Python for efficient handling of sequences and data streams. 

### Iterators 

An iterator is an object that can be iterated (looped) upon. It implements the `__iter__()` and `__next__()` methods. 

#### Creating an Iterator 

```python 
class Counter:     
	def __init__(self, low, high):        
		self.current = low        
		self.high = high     
	
	def __iter__(self):        
		return self     
	
	def __next__(self):        
		if self.current > self.high:            
			raise StopIteration        
		else:            
			self.current += 1            
		return self.current - 1 

# Using the iterator 
for c in Counter(3, 8):     
	print(c)  # Output: 3 4 5 6 7 8
```

## Generators

Generators are a simple way to create iterators using functions and the `yield` keyword.

## Creating a Generator Function

```python
def countdown(n):     
	while n > 0:        
		yield n        
		n -= 1 
		
# Using the generator 
for number in countdown(5):     
	print(number)  # Output: 5 4 3 2 1
```

## Generator Expressions

Similar to list comprehensions, but use parentheses instead of square brackets:

```python
squares = (x**2 for x in range(10)) 
print(list(squares))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Itertools Module

The `itertools` module provides a set of fast, memory-efficient tools for creating iterators.

```python
import itertools 

# Infinite counter 
for i in itertools.count(10):     
	print(i)    
	if i >= 15:        
		break  # Output: 10 11 12 13 14 15 
		
# Cycle through an iterable 
colors = itertools.cycle(['red', 'green', 'blue']) 
for i in range(7):     
	print(next(colors))  # Output: red green blue red green blue red 
	
# Repeat an element 
for i in itertools.repeat("Hello", 3):     
	print(i)  # Output: Hello Hello Hello
```

## Practical Examples

## Fibonacci Sequence Generator

```python
def fibonacci():     
	a, b = 0, 1    
	while True:        
		yield a        
		a, b = b, a + b 

fib = fibonacci() 
for _ in range(10):     
	print(next(fib))  # Output: 0 1 1 2 3 5 8 13 21 34
```

## Reading Large Files

```python
def read_large_file(file_path):     
	with open(file_path, 'r') as file:        
		while True:            
			line = file.readline()            
			if not line:                
				break            
			yield line.strip() 

# Usage 
for line in read_large_file('large_file.txt'):     
	print(line)
```

## Exercise

1. Create a generator function that yields all prime numbers up to a given limit.
2. Use the `itertools` module to create an iterator that alternates between two given values indefinitely.
3. Implement a custom iterator class that generates a sequence of even numbers.

## Key Points

- **Iterators** are objects that can be iterated upon.
- **Generators** are a simple way to create iterators using functions and the `yield` keyword.
- Generator expressions provide a concise way to create generators.
- The `itertools` module offers powerful tools for working with iterators.
- Generators are memory-efficient for handling large datasets or infinite sequences.
