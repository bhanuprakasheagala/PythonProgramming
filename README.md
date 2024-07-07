# Learning Python for C/C++ Developers

Welcome to my Python learning journey! As a C/C++ programmer, I am exploring Python to enhance my software development skills. This repository documents my learning process, resources, and projects. Below are the key topics I am focusing on, along with brief explanations for each.

## Table of Contents

1. [Introduction to Python](#introduction-to-python)
2. [Basic Syntax and Data Types](#basic-syntax-and-data-types)
3. [Control Structures](#control-structures)
4. [Functions and Modules](#functions-and-modules)
5. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
6. [Exception Handling](#exception-handling)
7. [File Handling](#file-handling)
8. [Standard Libraries](#standard-libraries)


## Introduction to Python

Python is a high-level, interpreted programming language known for its readability and simplicity. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## Basic Syntax and Data Types

### Syntax
- **Indentation**: Python uses indentation to define code blocks.
- **Comments**: Single-line (`#`) and multi-line comments (`'''` or `"""`).

### Data Types
- **Numbers**: Integers, floating-point numbers, and complex numbers.
- **Strings**: Immutable sequences of Unicode characters.
- **Lists**: Ordered, mutable sequences.
- **Tuples**: Ordered, immutable sequences.
- **Dictionaries**: Key-value pairs.
- **Sets**: Unordered collections of unique elements.

## Control Structures

### Conditional Statements
- `if`, `elif`, `else`: For decision-making.

### Loops
- `for`: Iterate over a sequence.
- `while`: Execute as long as a condition is true.

## Functions and Modules

### Functions
- Defined using the `def` keyword.
- Support default, keyword, and variable-length arguments.

### Modules
- Reusable pieces of code.
- Importing using `import` statement.

## Object-Oriented Programming (OOP)

Python's OOP is simpler and more flexible compared to C++. Here are the key concepts:

### Classes and Objects
- **Class**: A blueprint for creating objects. Use the `class` keyword.
- **Object**: An instance of a class.
  
  ```python
  class Dog:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def bark(self):
          return f"{self.name} says woof!"

  my_dog = Dog("Buddy", 3)
  print(my_dog.bark())  # Output: Buddy says woof!
  ```

### Inheritance
- **Inheritance**: Allows a class to inherit attributes and methods from another class. Use the `super()` function to call methods from the parent class.

  ```python
  class Animal:
      def __init__(self, species):
          self.species = species

      def make_sound(self):
          return "Some sound"

  class Dog(Animal):
      def __init__(self, name, age):
          super().__init__("Dog")
          self.name = name
          self.age = age

      def make_sound(self):
          return f"{self.name} says woof!"

  my_dog = Dog("Buddy", 3)
  print(my_dog.make_sound())  # Output: Buddy says woof!
  ```

### Polymorphism
- **Polymorphism**: Methods in different classes with the same name can be used interchangeably.

  ```python
  class Cat(Animal):
      def make_sound(self):
          return "Meow"

  def animal_sound(animal):
      print(animal.make_sound())

  dog = Dog("Buddy", 3)
  cat = Cat("Kitty")
  animal_sound(dog)  # Output: Buddy says woof!
  animal_sound(cat)  # Output: Meow
  ```

### Encapsulation
- **Encapsulation**: Restricting access to certain attributes and methods. Use a single underscore (`_`) for protected members and double underscore (`__`) for private members.

  ```python
  class Car:
      def __init__(self, model, year):
          self.model = model
          self.__year = year

      def get_year(self):
          return self.__year

  my_car = Car("Toyota", 2015)
  print(my_car.model)      # Output: Toyota
  print(my_car.get_year()) # Output: 2015
  # print(my_car.__year)   # Raises AttributeError
  ```

## Exception Handling

Python uses `try`, `except`, `else`, and `finally` blocks to handle exceptions, providing a cleaner way to manage errors compared to C++'s try-catch blocks.

### Try-Except Block
- Basic structure for handling exceptions.

  ```python
  try:
      x = 1 / 0
  except ZeroDivisionError as e:
      print(f"Error: {e}")
  else:
      print("No error occurred")
  finally:
      print("This will always execute")
  ```

### Custom Exceptions
- Creating user-defined exceptions.

  ```python
  class CustomError(Exception):
      pass

  try:
      raise CustomError("This is a custom error")
  except CustomError as e:
      print(f"Caught custom error: {e}")
  ```

## File Handling

Python provides built-in functions to handle file operations, making it straightforward to read from and write to files.

### Reading and Writing Files
- Basic operations with `open()`, `read()`, `write()`, and `close()`.

  ```python
  # Writing to a file
  with open("example.txt", "w") as file:
      file.write("Hello, World!")

  # Reading from a file
  with open("example.txt", "r") as file:
      content = file.read()
      print(content)  # Output: Hello, World!
  ```

### Context Managers
- Using `with` statement for better resource management.

  ```python
  with open("example.txt", "r") as file:
      content = file.read()
      print(content)
  ```

## Standard Libraries

Python's standard library provides a rich set of modules and functions for various tasks, reducing the need for external libraries.

### Common Libraries
- **os**: Interacting with the operating system.
- **sys**: System-specific parameters and functions.
- **datetime**: Date and time manipulation.
- **math**: Mathematical functions.
- **json**: JSON serialization and deserialization.
