# Variables in Python
x = 5           # int
y = "Hello"     # str
z = 3.14        # float

# Multiple assignment
a, b, c = 1, 2, "three"

# Type Conversion
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

# Checking Types
x = 5
print(type(x))  # <class 'int'>

y = "Hello"
print(type(y))  # <class 'str'>

### Exercise
# 1. Create variables of each basic data type.
n = 9  # int
s = "10"  # string
π = 3.14159  # float
L = [2021, 2022, 2023, 2024, 2025]  # list
T = (2021, 2022, 2023, 2024, 2025)  # tuple
user = {"name": "Bob", "age": 40}  # dict
reals = {4.3, 2.0, -9.7, 1.1, 0.0}  # set
naturals = frozenset((1, 2, 3, 4, 5))  # frozenset
python_rules = True  # bool
doubts = None  # None

# 2. Perform type conversions between int, float, and str.
n = float(n)  # n will be 9.0
s = int(s)  # s will be 10
π = str(π)  # π will be "3.14159"

# 3. Use type() to verify the type of each variable before and after conversion.
print("n:", n, "\t\t", type(n))
print("s:", s, "\t\t", type(s))
print("π:", π, "\t", type(π))
