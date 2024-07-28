## 3. Control Flow

Control flow in Python determines the order of execution for program statements. The main control flow mechanisms are conditional statements and loops.

### Conditional Statements

#### if-elif-else

Used for decision making in code:

```python
x = 10

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

### Ternary Operator

A concise way to write simple if-else statements:

```python
x = 5
result = "Even" if x % 2 == 0 else "Odd"
```

### Loops

#### for Loop

Used for iterating over a sequence:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):
    print(i)  # Prints 0 to 4
```

#### while Loop

Executes as long as a condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Control Flow Mechanisms

#### break

Exits the current loop:

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0 to 4
```

#### continue

Skips the rest of the current iteration:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4
```

#### pass

A null operation; used as a placeholder:

```python
for i in range(5):
    if i == 2:
        pass  # Do nothing
    print(i)  # Prints all numbers 0 to 4
```

### Combining Control Structures

Control structures can be nested:

```python
for i in range(3):
    for j in range(3):
        if i == j:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()  # New line after each row
```

Output:

```text
* 0 0 
0 * 0 
0 0 * 
```

### Exercise

1. Write a program that prints numbers from 1 to 100.
2. For multiples of 3, print "Fizz" instead of the number.
3. For multiples of 5, print "Buzz".
4. For numbers which are multiples of both 3 and 5, print "FizzBuzz".
python


### Key Points

- Indentation is crucial in Python for defining code blocks.
- elif can be used multiple times, but else is optional and used only once.
- for loops are typically used when the number of iterations is known.
- while loops are used when the iteration depends on a condition.
- break, continue, and pass provide additional control within loops.