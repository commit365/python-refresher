
## 10. Object-Oriented Programming: Classes, Objects, Inheritance, and Polymorphism 

Object-Oriented Programming (OOP) is a programming paradigm that uses objects to structure code. Python is a multi-paradigm language that fully supports OOP. 

### Classes and Objects 

#### Defining a Class 

```python
class Dog:     
	def __init__(self, name, age):        
		self.name = name        
		self.age = age     
	
	def bark(self):        
		return f"{self.name} says Woof!"
``` 

## Creating Objects

```python
my_dog = Dog("Buddy", 3) 
print(my_dog.name)  # Output: Buddy 
print(my_dog.bark())  # Output: Buddy says Woof!
```

## Class and Instance Variables

```python
class Car:     
	wheels = 4  # Class variable     
	
	def __init__(self, make, model):        
		self.make = make  # Instance variable        
		self.model = model  # Instance variable
```

## Methods

## Instance Methods

```python
class Rectangle:     
	def __init__(self, width, height):        
		self.width = width        
		self.height = height     
	
	def area(self):        
		return self.width * self.height
```

## Class Methods

```python
class Circle:     
	pi = 3.14159     
	
	@classmethod    
	def from_diameter(cls, diameter):        
		return cls(diameter / 2)     
	
	def __init__(self, radius):        
		self.radius = radius
```

## Static Methods

```python
class MathOperations:     
	@staticmethod    
	def add(x, y):        
		return x + y
```

## Inheritance

```python
class Animal: 
	def __init__(self, name): 
		self.name = name 
	def speak(self): 
		pass 

class Cat(Animal): 
	def speak(self): 
		return f"{self.name} says Meow!" 
		
class Dog(Animal): 
	def speak(self): 
		return f"{self.name} says Woof!"
```

## Polymorphism

```python
def animal_sound(animal):     
	return animal.speak() 
	
cat = Cat("Whiskers") 
dog = Dog("Rex") 

print(animal_sound(cat))  # Output: Whiskers says Meow! 
print(animal_sound(dog))  # Output: Rex says Woof!
```

## Encapsulation

Use double underscores for name mangling (private attributes):

```python
class BankAccount:     
	def __init__(self, balance):        
		self.__balance = balance     
	
	def deposit(self, amount):        
		self.__balance += amount     
		
	def get_balance(self):        
		return self.__balance
```

## Multiple Inheritance

```python
class Flyable:     
	def fly(self):        
		return "I can fly!" 
		
class Swimmable:     
	def swim(self):        
		return "I can swim!" 

class Duck(Animal, Flyable, Swimmable):     
	pass
```

## Abstract Base Classes

```python
from abc import ABC, abstractmethod 

class Shape(ABC):     
	@abstractmethod    
	def area(self):        
		pass 

class Square(Shape):     
	def __init__(self, side):        
		self.side = side     
	
	def area(self):        
		return self.side ** 2
```

## Exercise

1. Create a `Vehicle` class with attributes for `make`, `model`, and `year`.
2. Add a method `description()` that returns a string describing the vehicle.
3. Create two subclasses: `Car` and `Motorcycle`. Add specific attributes and methods to each.
4. Implement a `start_engine()` method in both subclasses that returns a unique sound for each vehicle type.
5. Create instances of both `Car` and `Motorcycle` and demonstrate polymorphism by calling their methods.

## Key Points

- Classes are blueprints for objects.
- Inheritance allows creating new classes based on existing ones.
- Polymorphism enables using objects of different types through a common interface.
- Encapsulation helps in hiding internal details of a class.
- Python supports multiple inheritance.
- Abstract base classes define a common interface for derived classes.
