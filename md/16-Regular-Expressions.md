
## 16. Regular Expressions: Pattern Matching with Regular Expressions 

Regular expressions (regex) are powerful tools for pattern matching and text manipulation. Python's `re` module provides support for working with regular expressions. 

### Basics of Regular Expressions 

#### Importing the `re` Module 

```python 
import re
```

## Simple Pattern Matching

```python
pattern = r'\d+'  # Matches one or more digits 
text = "There are 123 apples and 456 oranges." 
matches = re.findall(pattern, text) 
print(matches)  # Output: ['123', '456']
```

## Common Regex Patterns

- `.`: Any character except newline
- `\d`: Digit (0-9)
- `\D`: Non-digit
- `\w`: Word character (alphanumeric + underscore)
- `\W`: Non-word character
- `\s`: Whitespace (space, tab, newline)
- `\S`: Non-whitespace
- `^`: Start of string
- `$`: End of string
- `*`: Zero or more repetitions
- `+`: One or more repetitions
- `?`: Zero or one repetition
- `{n}`: Exactly n repetitions
- `{n,}`: n or more repetitions
- `{n,m}`: Between n and m repetitions
- `[]`: Set of characters
- `|`: OR operator

## Functions in the `re` Module

## `re.match()`

Matches a pattern at the beginning of the string.

```python
pattern = r'Hello' 
text = "Hello, World!" 
match = re.match(pattern, text) 
if match:     
	print("Match found!")  # Output: Match found!
```

## `re.search()`

Searches for the first occurrence of the pattern in the string.

```python
pattern = r'World' 
text = "Hello, World!" 
match = re.search(pattern, text) 
if match:     
	print("Match found!")  # Output: Match found!
```

## `re.findall()`

Finds all occurrences of the pattern in the string.

```python
pattern = r'\d+' 
text = "There are 123 apples and 456 oranges." 
matches = re.findall(pattern, text) 
print(matches)  # Output: ['123', '456']
```

## `re.sub()`

Replaces occurrences of the pattern with a replacement string.

```python
pattern = r'apples' 
replacement = 'bananas' 
text = "I like apples." 
new_text = re.sub(pattern, replacement, text) 
print(new_text)  # Output: I like bananas.
```

## `re.split()`

Splits the string by occurrences of the pattern.

```python
pattern = r'\s+' 
text = "Split this text by whitespace." 
parts = re.split(pattern, text) 
print(parts)  # Output: ['Split', 'this', 'text', 'by', 'whitespace.']
```

## Grouping and Capturing

Using parentheses to create groups and capture parts of the match.

```python
pattern = r'(\d+)\s(\w+)' 
text = "123 apples" 
match = re.search(pattern, text) 
if match:     
	print(match.group(1))  # Output: 123    
	print(match.group(2))  # Output: apples
```

## Practical Examples

## Email Validation

```python
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' 
email = "example@example.com" 
if re.match(pattern, email):     
	print("Valid email") 
else:     
	print("Invalid email")
```

## Phone Number Extraction

```python
pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b' 
text = "Call me at 123-456-7890 or 987.654.3210" 
matches = re.findall(pattern, text) 
print(matches)  # Output: ['123-456-7890', '987.654.3210']
```

## Exercise

1. Write a regex pattern to match valid IP addresses.
2. Create a regex pattern to extract dates in the format `DD/MM/YYYY` from a given text.
3. Implement a function that uses regex to validate strong passwords (at least 8 characters, including uppercase, lowercase, digit, and special character).

## Key Points

- Regular expressions are powerful for pattern matching and text manipulation.
- The `re` module provides functions like `match()`, `search()`, `findall()`, `sub()`, and `split()`.
- Use raw strings (`r''`) for regex patterns to avoid escaping backslashes.
- Grouping and capturing allow extracting specific parts of the match.
- Regular expressions are useful for validation, extraction, and substitution tasks.
