## 5. Data Structures 

Python provides several built-in data structures that are essential for organizing and storing data: lists, tuples, sets, and dictionaries. 

### Lists 

Lists are ordered, mutable sequences of elements: 

```python
# Creating a list 
fruits = ["apple", "banana", "cherry"] 

# Accessing elements 
print(fruits[0])  # Output: apple 

# Modifying elements 
fruits[1] = "blueberry" 

# Adding elements 
fruits.append("orange") 

# Removing elements 
fruits.remove("cherry") 

# List comprehension 
squares = [x**2 for x in range(5)] 
print(fruits)  # Output: ['apple', 'blueberry', 'orange'] 

print(squares)  #Output: [0, 1, 4, 9, 16] 
```

## Tuples

Tuples are ordered, immutable sequences of elements:

```python
# Creating a tuple 
coordinates = (10, 20) 

# Accessing elements 
print(coordinates[0])  # Output: 10 

# Tuples are immutable 
coordinates = 15  # Error: 'tuple' object does not support item assignment 

# Tuple unpacking 
x, y = coordinates 

print(x, y)  # Output: 10 20
```

## Sets

Sets are unordered collections of unique elements:

```python
# Creating a set 
numbers = {1, 2, 3, 4, 4} 

# Adding elements 
numbers.add(5) 

# Removing elements 
numbers.remove(3) 

# Set operations 
odds = {1, 3, 5, 7} 
evens = {2, 4, 6, 8} 
primes = {2, 3, 5, 7} 

# Union 
union = odds | evens 

# Intersection 
intersection = odds & primes 

# Difference 
difference = odds - primes 

print(numbers)  # Output: {1, 2, 4, 5} 
print(union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8} 
print(intersection)  # Output: {3, 5, 7} 
print(difference)  # Output: {1}
```

## Dictionaries

Dictionaries are unordered collections of key-value pairs:

```python
# Creating a dictionary 
person = {"name": "Alice", "age": 30} 

# Accessing values 
print(person["name"])  # Output: Alice 

# Modifying values 
person["age"] = 31 

# Adding key-value pairs 
person["city"] = "New York" 

# Removing key-value pairs 
del person["age"] 

# Dictionary comprehension 
squares = {x: x**2 for x in range(5)} 

print(person)  # Output: {'name': 'Alice', 'city': 'New York'} 
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Exercise

1. Create a list of numbers from 1 to 10 and print the even numbers.
2. Create a tuple with the names of five cities and print the first and last city.
3. Create a set of vowels and check if 'e' is in the set.
4. Create a dictionary with three key-value pairs representing a person's attributes (e.g., name, age, city) and print each key-value pair.

## Key Points

- **Lists** are ordered and mutable.
- **Tuples** are ordered and immutable.
- **Sets** are unordered collections of unique elements.
- **Dictionaries** are unordered collections of key-value pairs.
- Use comprehensions to create lists, sets, and dictionaries concisely.
