## 2. Data Types and Variables

### Basic Data Types

Python has several built-in data types:

1. **Numeric Types**
   - `int`: Integers (e.g., -1, 0, 100)
   - `float`: Floating-point numbers (e.g., 3.14, -0.5)
   - `complex`: Complex numbers (e.g., 1+2j)

2. **Sequence Types**
   - `str`: Strings (e.g., "Hello", 'Python')
   - `list`: Ordered, mutable sequences (e.g., [1, 2, 3])
   - `tuple`: Ordered, immutable sequences (e.g., (1, 2, 3))

3. **Mapping Type**
   - `dict`: Key-value pairs (e.g., {"name": "Alice", "age": 30})

4. **Set Types**
   - `set`: Unordered collection of unique elements (e.g., {1, 2, 3})
   - `frozenset`: Immutable version of set

5. **Boolean Type**
   - `bool`: True or False

6. **None Type**
   - `None`: Represents absence of a value

### Variables

Variables in Python:
- Are created when you assign a value
- Don't need to be declared with any particular type
- Can be reassigned to different types

```python
x = 5           # int
y = "Hello"     # str
z = 3.14        # float

# Multiple assignment
a, b, c = 1, 2, "three"
```

### Type Conversion

Python provides functions for type conversion:

```python
# String to Integer
age = int("30")

# Integer to String
age_str = str(30)

# String to Float
pi = float("3.14")

# Integer to Float
x = float(5)

# Float to Integer (truncates decimal part)
y = int(3.9)  # y will be 3
```

### Checking Types

Use type() function to check the type of a variable:

```python
x = 5
print(type(x))  # <class 'int'>

y = "Hello"
print(type(y))  # <class 'str'>
```

### Exercise

1. Create variables of each basic data type.
2. Perform type conversions between int, float, and str.
3. Use type() to verify the type of each variable before and after conversion.

### Key Points

- Python is dynamically typed, but it's still important to understand types.
- Type conversion is useful but be careful of potential data loss (e.g., float to int).
- Always consider the appropriate data type for your variables to ensure efficient and correct code.
