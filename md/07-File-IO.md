
## 7. File I/O: Reading from and Writing to Files 

File Input/Output (I/O) operations are essential for working with external data in Python. This section covers how to read from and write to files. 

### Opening Files 

Use the `open()` function to open files. It returns a file object: 

```python 
file = open('example.txt', 'r')  # 'r' for read mode 

# Remember to close the file when done 
file.close()
```

## Using `with` Statement

The `with` statement automatically closes the file after you're done:

```python
with open('example.txt', 'r') as file:     
	# File operations here
```

## Reading Files

## Read entire file

```python
with open('example.txt', 'r') as file:     
	content = file.read()    
	print(content)
```

## Read line by line

```python
with open('example.txt', 'r') as file:     
	for line in file:        
		print(line.strip())  # strip() removes leading/trailing whitespace
```

## Read into a list

```python
with open('example.txt', 'r') as file:     
	lines = file.readlines()    
	print(lines)
```

## Writing to Files

## Write mode ('w')

Overwrites the entire file:

```python
with open('output.txt', 'w') as file:     
	file.write('Hello, World!\n')    
	file.write('This is a new line.')
```

## Append mode ('a')

Adds to the end of the file:

```python
with open('output.txt', 'a') as file:     
	file.write('This line is appended.\n')
```

## Working with CSV Files

Python's `csv` module makes it easy to work with CSV files:

```python
import csv # Reading CSV 
with open('data.csv', 'r') as file:     
	csv_reader = csv.reader(file)    
	for row in csv_reader:        
		print(row) 

# Writing CSV 
data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]] 
with open('output.csv', 'w', newline='') as file:     
	csv_writer = csv.writer(file)    
	csv_writer.writerows(data)
```

## File Modes

- `'r'`: Read (default)
- `'w'`: Write (overwrites file)
- `'a'`: Append
- `'r+'`: Read and write
- `'b'`: Binary mode (e.g., `'rb'` for reading binary)

## Error Handling

Use try-except blocks to handle potential file-related errors:

```python
try:     
	with open('nonexistent.txt', 'r') as file:        
		content = file.read() 
except FileNotFoundError:     
	print("The file does not exist.") 
except IOError:     
	print("An error occurred while reading the file.")
```

## Exercise

1. Create a text file named 'sample.txt' with a few lines of text.
2. Write a Python script to read this file and print its contents.
3. Append a new line to the file.
4. Read the file again to verify the new line was added.

## Key Points

- Always close files after opening them, or use the `with` statement.
- Choose the appropriate file mode for your operation.
- Use the `csv` module for working with CSV files.
- Handle potential file-related errors with try-except blocks.
- Be cautious with write mode ('w') as it overwrites existing files.
