
## 12. Comprehensions: List, Dictionary, and Set Comprehensions 

Comprehensions provide a concise way to create lists, dictionaries, and sets in Python. They are often more readable and efficient than traditional loops. 

### List Comprehensions 

List comprehensions allow you to create lists in a single line of code. 

#### Basic List Comprehension 

```python 
# Create a list of squares 
squares = [x ** 2 for x in range(10)] 
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## With Condition

```python
# Create a list of even numbers 
evens = [x for x in range(10) if x % 2 == 0] 
print(evens)  # Output: [0, 2, 4, 6, 8]
```

## Dictionary Comprehensions

Dictionary comprehensions allow you to create dictionaries in a single line of code.

## Basic Dictionary Comprehension

```python
# Create a dictionary of squares 
squares_dict = {x: x ** 2 for x in range(10)} 
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

## With Condition

```python
# Create a dictionary of even squares 
even_squares_dict = {x: x ** 2 for x in range(10) if x % 2 == 0} 
print(even_squares_dict)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## Set Comprehensions

Set comprehensions allow you to create sets in a single line of code.

## Basic Set Comprehension

```python
# Create a set of squares 
squares_set = {x ** 2 for x in range(10)} 
print(squares_set)  # Output: {0, 1, 64, 4, 36, 9, 16, 81, 49, 25}
```

## With Condition

```python
# Create a set of even numbers 
evens_set = {x for x in range(10) if x % 2 == 0} 
print(evens_set)  # Output: {0, 2, 4, 6, 8}
```

## Nested Comprehensions

Comprehensions can be nested to create complex structures.

## Nested List Comprehension

```python
# Create a 2D list (matrix) 
matrix = [[x * y for x in range(3)] for y in range(3)] 
print(matrix)  # Output: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

## Practical Examples

## Flatten a List of Lists

```python
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]] 
flattened = [item for sublist in list_of_lists for item in sublist] print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
```

## Exercise

1. Use a list comprehension to create a list of the first 10 cube numbers.
2. Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5 and the values are their cubes.
3. Use a set comprehension to create a set of the unique vowels in a given string.

## Key Points

- **List comprehensions** provide a concise way to create lists.
- **Dictionary comprehensions** provide a concise way to create dictionaries.
- **Set comprehensions** provide a concise way to create sets.
- Comprehensions can include conditions to filter elements.
- Nested comprehensions can create complex data structures.
