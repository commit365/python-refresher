
## 11. Functional Programming: Lambda Functions, Map, Filter, and Reduce 

Functional programming in Python leverages higher-order functions like `lambda`, `map`, `filter`, and `reduce` to write concise and efficient code. 

### Lambda Functions 

Lambda functions are anonymous, inline functions defined using the `lambda` keyword. They can have any number of arguments but only one expression. 

```python 
# Basic lambda function 
square = lambda x: x ** 2 
print(square(5))  # Output: 25
```

## Map

The `map()` function applies a given function to all items in an input list (or any iterable) and returns a map object (which can be converted to a list).

```python
numbers = [1, 2, 3, 4, 5] 
squared = list(map(lambda x: x ** 2, numbers)) 
print(squared)  # Output: [1, 4, 9, 16, 25]
```

## Filter

The `filter()` function constructs an iterator from elements of the iterable for which the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5] 
even = list(filter(lambda x: x % 2 == 0, numbers)) 
print(even)  # Output: [2, 4]
```

## Reduce

The `reduce()` function applies a rolling computation to sequential pairs of values in a list. It belongs to the `functools` module.

```python
from functools import reduce 

numbers = [1, 2, 3, 4, 5] 
product = reduce(lambda x, y: x * y, numbers) 
print(product)  # Output: 120
```

## Practical Examples

## Using `map()` with a Lambda Function

```python
# Multiply all elements by 2 
numbers = [1, 2, 3, 4, 5] 
doubled = list(map(lambda x: x * 2, numbers)) 
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

## Using `filter()` with a Lambda Function

```python
# Filter out odd numbers 
numbers = [1, 2, 3, 4, 5] 
odds = list(filter(lambda x: x % 2 != 0, numbers)) 
print(odds)  # Output: [1, 3, 5]
```

## Using `reduce()` with a Lambda Function

```python
# Sum of all elements from functools 
import reduce 

numbers = [1, 2, 3, 4, 5] 
total = reduce(lambda x, y: x + y, numbers) 
print(total)  # Output: 15
```

## Exercise

1. Create a list of numbers from 1 to 10.
2. Use `map()` to create a new list with each number squared.
3. Use `filter()` to create a list of only the even numbers from the squared list.
4. Use `reduce()` to find the sum of the even squared numbers.

## Key Points

- **Lambda functions** are useful for small, one-time-use functions.
- **map()** applies a function to all items in an iterable.
- **filter()** extracts elements from an iterable based on a condition.
- **reduce()** performs a cumulative operation on an iterable.
- These functions can often be replaced with list comprehensions for better readability.
