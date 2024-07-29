# File IO

# Opening Files
file = open('example.txt', 'r')  # 'r' for read mode 

# Remember to close the file when done 
file.close()

# Using with Statement
with open('example.txt', 'r') as file:     
	# File operations here

# Read entire file
with open('example.txt', 'r') as file:     
	content = file.read()    
	print(content)
	
# Read line by line
with open('example.txt', 'r') as file:     
	for line in file:        
		print(line.strip())  # strip() removes leading/trailing whitespace
		
# Read into a list
with open('example.txt', 'r') as file:     
	lines = file.readlines()    
	print(lines)

# Writing Files
# Write mode ('w')
with open('output.txt', 'w') as file:     
	file.write('Hello, World!\n')    
	file.write('This is a new line.')
	
# Append mode ('a')
with open('output.txt', 'a') as file:     
	file.write('This line is appended.\n')
	
# Working with CSV Files
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
	
# Error Handling
try:     
	with open('nonexistent.txt', 'r') as file:        
		content = file.read() 
except FileNotFoundError:     
	print("The file does not exist.") 
except IOError:     
	print("An error occurred while reading the file.")
	

# Exercises
# 1. Create a text file named 'sample.txt' with a few lines of text.
content = """This is the first line.
This is the second line.
This is the third line."""

with open('sample.txt', 'w') as file:
    file.write(content)

# 2. Write a Python script to read this file and print its contents.
with open('sample.txt', 'r') as file:
    contents = file.read()
    print("Contents of sample.txt:")
    print(contents)

# 3. Append a new line to the file.
with open('sample.txt', 'a') as file:
	file.write("\nThis is the fourth line.")

# 4. Read the file again to verify the new line was added.
with open('sample.txt', 'r') as file:
	contents = file.read()
	print("Contents of sample.txt:")
	print(contents)