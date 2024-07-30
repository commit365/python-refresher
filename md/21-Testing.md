
## 21. Testing: Writing and Running Tests with unittest and pytest 

Testing is crucial for ensuring the reliability and correctness of your code. Python provides built-in support for testing through the `unittest` module, and `pytest` is a popular third-party testing framework. 

### unittest 

`unittest` is Python's built-in testing framework, inspired by JUnit. 
#### Basic Test Structure 

```python 
import unittest 

def add(a, b): 
	return a + b 

class TestAddFunction(unittest.TestCase): 
	def test_add_positive_numbers(self):
		self.assertEqual(add(2, 3), 5) 
		
	def test_add_negative_numbers(self):
		self.assertEqual(add(-1, -1), -2) 
	
	def test_add_zero(self): 
		self.assertEqual(add(5, 0), 5) 

if __name__ == '__main__': 
	unittest.main()
```

## Running Tests

```bash
python test_add.py
```

## Assertions

`unittest` provides various assertion methods:

```python
class TestStringMethods(unittest.TestCase): 
	def test_upper(self): 
		self.assertEqual('foo'.upper(), 'FOO') 
	
	def test_isupper(self): 
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper()) 
	
	def test_split(self): 
		s = 'hello world' 
		self.assertEqual(s.split(), ['hello', 'world']) 
		with self.assertRaises(TypeError): 
			s.split(2)
```

## Test Setup and Teardown

```python
class TestDatabase(unittest.TestCase): 
	def setUp(self): 
		self.db = Database() 
	
	def tearDown(self): 
		self.db.close() 
	
	def test_insert(self): 
		self.db.insert("data")
		self.assertEqual(self.db.count(), 1)
```

## pytest

`pytest` is a more advanced testing framework that makes it easy to write simple tests, yet scales to support complex functional testing.

## Installation

```bash
pip install pytest
```

## Basic Test Structure

```python
# test_sample.py 
def add(a, b):     
	return a + b 

def test_add():     
	assert add(2, 3) == 5    
	assert add(-1, -1) == -2    
	assert add(5, 0) == 5
```

## Running Tests

```bash
pytest test_sample.py
```

## Fixtures

Fixtures are used to provide data or objects to tests:

```python
import pytest 

@pytest.fixture 
def sample_data():     
	return [1, 2, 3, 4, 5] 
	
def test_sum(sample_data):     
	assert sum(sample_data) == 15
```

## Parameterized Tests

```python
import pytest 

@pytest.mark.parametrize( 
	"input, expected", 
	[ 
		("3+5", 8), 
		("2+4", 6), 
		("6*9", 54),
	] 
) 

def test_eval(input, expected): 
	assert eval(input) == expected
```

## Test Discovery

pytest automatically discovers tests in files prefixed with `test_` or suffixed with `_test.py`.

## Mocking

Mocking is useful for isolating the code being tested:

```python
from unittest.mock import Mock, patch 

def get_user_data(user_id): 
	# Assume this function makes an API call 
	pass 

def test_get_user_data(): 
	with patch('__main__.get_user_data') as 
mock_get: 
	mock_get.return_value = {"name": "John", "age": 30} 
	result = get_user_data(1) assert result["name"] == "John" mock_get.assert_called_once_with(1)
```

## Code Coverage

To measure code coverage, you can use the `coverage` tool:

```bash
# Install the coverage package 
pip install coverage 

# Run pytest with coverage measurement 
coverage run -m pytest 

# Display the coverage report in the terminal 
coverage report 

# Generate a detailed HTML coverage report
coverage html
```

## Best Practices

1. Write tests before or alongside your code (Test-Driven Development).
2. Keep tests small, focused, and independent.
3. Use descriptive test names that explain what is being tested.
4. Aim for high code coverage, but focus on critical paths.
5. Regularly run your test suite, ideally as part of your CI/CD pipeline.

## Exercise

1. Write a set of unittest tests for a function that calculates the factorial of a number.
2. Create pytest tests for a class that represents a simple bank account with deposit and withdraw methods.
3. Use mocking to test a function that depends on an external API call.

## Key Points

- `unittest` is built into Python and provides a rich set of assertion methods.
- `pytest` offers a simpler syntax and powerful features like fixtures and parameterized tests.
- Mocking is crucial for isolating units of code during testing.
- Code coverage tools help identify untested parts of your codebase.
- Regular testing is essential for maintaining code quality and preventing regressions.
