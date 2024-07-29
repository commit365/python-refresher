# Control-Flow

# if-elif-else
x = 10

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Ternary Operator
x = 5
result = "Even" if x % 2 == 0 else "Odd"

# for Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):
    print(i)  # Prints 0 to 4

# while Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Control Flow Mechanisms
# break
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0 to 4

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4

# pass
for i in range(5):
    if i == 2:
        pass  # Do nothing
    print(i)  # Prints all numbers 0 to 4

# Nested Control Structures
for i in range(3):
    for j in range(3):
        if i == j:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()  # New line after each row


### Exercise

# 1. Write a program that prints numbers from 1 to 100.
for i in range(1, 101):
    print(i)

# 2. For multiples of 3, print "Fizz" instead of the number.
for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# 3. For multiples of 5, print "Buzz".
for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 4. For numbers which are multiples of both 3 and 5, print "FizzBuzz".
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
