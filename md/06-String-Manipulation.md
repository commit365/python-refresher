
## 6. String Manipulation 

Strings are sequences of characters and are one of the most commonly used data types in Python. Understanding string manipulation is crucial for effective programming. 

### Creating Strings 

Strings can be created using single, double, or triple quotes: 

```python 
s1 = 'Hello' 
s2 = "World" 
s3 = '''This is a multi-line 
string'''
```

## String Concatenation

Strings can be combined using the `+` operator:


```python
greeting = s1 + ", " + s2 
print(greeting)  # Output: Hello, World
```

## String Indexing and Slicing

Access individual characters or substrings:

```python
s = "Python" 
print(s)  # Output: Python 
print(s[1:4])  # Output: yth 
print(s[::-1])  # Output: nohtyP (reverse)
```

## String Methods

Python provides many built-in methods for string manipulation:


```python
s = "hello, world" 
print(s.upper())  # Output: HELLO, WORLD 
print(s.capitalize())  # Output: Hello, world 
print(s.title())  # Output: Hello, World 
print(s.strip())  # Removes leading/trailing whitespace 
print(s.split(','))  # Output: ['hello', ' world'] 
print(','.join(['a', 'b', 'c']))  # Output: a,b,c 
print(s.replace('o', '0'))  # Output: hell0, w0rld
```

## String Formatting

## f-strings (Python 3.6+)


```python
name = "Alice" 
age = 30 
print(f"My name is {name} and I am {age} years old.")
```

## format() method

```python
print("My name is {} and I am {} years old.".format(name, age))
```

## %-formatting (older style)

```python
print("My name is %s and I am %d years old." % (name, age))
```

## String Operations

```python
# Repetition 
print("Ha" * 3)  # Output: HaHaHa 

# Membership test 
print('a' in 'abc')  # Output: True 

# Length 
print(len("Python"))  # Output: 6
```

## Raw Strings

Prefixing a string with `r` treats backslashes as literal characters:


```python
print(r"C:\Users\name")  # Output: C:\Users\name
```

## Exercise

1. Create a string containing a sentence.
2. Convert the string to uppercase and then to title case.
3. Split the string into a list of words.
4. Join the words back into a string, separating them with hyphens.
5. Replace all occurrences of a specific character in the string.

## Key Points

- Strings are immutable in Python.
- String methods return new strings; they don't modify the original string.
- f-strings provide a concise and readable way to embed expressions inside string literals.
- Always consider using string methods for manipulation tasks before writing custom logic.