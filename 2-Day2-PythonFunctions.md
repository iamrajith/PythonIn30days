# 30 Days of Python: Day 2 - Python Functions

Welcome to Day 2 of the **30 Days of Python** programming challenge! In this journey, we'll explore Python step by step, covering essential topics and practical examples. Whether you're a beginner or refreshing your skills, let's dive into Python functions today.

## Table of Contents
1. [Introduction](#introduction)
2. [What Are Functions?](#what-are-functions)
3. [Defining Functions](#defining-functions)
4. [Function Parameters](#function-parameters)
5. [Return Values](#return-values)
6. [Examples](#examples)
7. [References](#references)

## Introduction
Python is a high-level, open-source programming language known for its readability and versatility. Functions play a crucial role in Python, allowing us to organize code, reuse logic, and make our programs more modular.

## What Are Functions?
- Functions are blocks of code that perform specific tasks.
- They allow us to break down complex problems into smaller, manageable pieces.
- Functions can take input (arguments) and return output (values).

## Defining Functions
To define a function, use the `def` keyword followed by the function name, parentheses, and a colon. The function body is indented.

```python
def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")

# Call the function
greet("Alice")
```

## Function Parameters
- Parameters are placeholders for values passed to a function.
- You can have multiple parameters separated by commas.
- Default values can be assigned to parameters.

```python
def add(a, b=0):
    """Add two numbers."""
    return a + b

result = add(5, 3)  # 8
```

## Return Values
- Use the `return` keyword to send a value back from a function.
- Functions can return multiple values (as a tuple).

```python
def divide(a, b):
    """Divide two numbers."""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

result = divide(10, 2)  # 5.0
```

## Examples
1. **Age Classifier**:
   - Classify a person's age as infant, child, teenager, or adult.
   - Example:
     ```python
     def classify_age(age):
         if age <= 1:
             return "Infant"
         elif 1 < age < 13:
             return "Child"
         elif 13 <= age < 20:
             return "Teenager"
         else:
             return "Adult"

     print(classify_age(25))  # Adult
     ```

2. **Calculate Hypotenuse**:
   - Compute the hypotenuse of a right triangle using the Pythagorean theorem.
   - Example:
     ```python
     def hypotenuse(a, b):
         return (a**2 + b**2) ** 0.5

     print(hypotenuse(3, 4))  # 5.0
     ```

3. **Custom Greeting**:
   - Create a personalized greeting.
   - Example:
     ```python
     def custom_greeting(name, age):
         return f"Hello, {name}! You are {age} years old."

     print(custom_greeting("Bob", 40))
     ```

## References
1. [30 Days of Python GitHub Repository](https://github.com/Asabeneh/30-Days-Of-Python)
2. [Learn Python in 30 Days PDF](https://heavycoding.com/learn-python-in-30-days-pdf/)
3. [Python Learning Roadmap in 30 Days](https://github.com/HalilDeniz/Python30Days)
4. [Learn Python in 30 Days](https://datagy.io/learn-python-in-30-days/)
5. [30 Days of Python!](https://pwskills.com/blog/30-days-of-python/)