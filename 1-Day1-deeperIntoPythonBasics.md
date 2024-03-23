# **Python Learning Lab: Day 1 - Dive Deeper into Python Basics**
If you would like to learn more on day 1, please join with me. Working through a few examples together will help us improve our understanding. Let's get started!

1. **Calculate the Area of a Circle**:
   ```python
   radius = 5
   pi = 3.14159
   area = pi * (radius ** 2)
   print(f"The area of the circle is {area:.2f} square units.")
   ```

2. **Check if a Number is Even or Odd**:
   ```python
   number = 17
   if number % 2 == 0:
       print(f"{number} is even.")
   else:
       print(f"{number} is odd.")
   ```

3. **Find the Largest Among Three Numbers**:
   ```python
   def find_largest(a, b, c):
       return max(a, b, c)

   num1, num2, num3 = 12, 8, 15
   largest_number = find_largest(num1, num2, num3)
   print(f"The largest number among {num1}, {num2}, and {num3} is {largest_number}.")
   ```
This example prompted me to ask a few questions: what is max(), and how does it work?

- **What is `max()`?**
   - The `max()` function is a built-in Python function.
   - It is used to find the maximum value among a set of values (numbers, strings, or other comparable objects).

- **How Does `max()` Work?**
   - Syntax: `max(arg1, arg2, ..., argN)`
   - It takes one or more arguments (separated by commas).
   - It returns the largest value from the provided arguments.
   - The arguments can be numbers, strings, or any comparable objects.
   - For numbers, it compares their numeric values.
   - For strings, it compares lexicographically (based on ASCII values).

- **Examples**:
   - Numeric Example:
     ```python
     numbers = [10, 5, 20, 15]
     largest_number = max(numbers)
     print(f"The largest number is {largest_number}")
     ```
     Output: "The largest number is 20"

   - String Example:
     ```python
     names = ["Alice", "Bob", "Charlie", "Zara"]
     longest_name = max(names)
     print(f"The longest name is {longest_name}")
     ```
     Output: "The longest name is Zara"

- **Custom Objects (with Key Function)**:
   - You can use a custom key function to determine how the comparison is done.
   - For example, to find the person with the highest age:
     ```python
     people = [
         {"name": "Alice", "age": 30},
         {"name": "Bob", "age": 25},
         {"name": "Charlie", "age": 35}
     ]
     oldest_person = max(people, key=lambda p: p["age"])
     print(f"The oldest person is {oldest_person['name']} ({oldest_person['age']} years old)")
     ```
     Output: "The oldest person is Charlie (35 years old)"

Remember that `max()` is a powerful tool for finding the maximum value in various contexts, and it's widely used in Python!


Remember to modify and experiment with these examples. Happy coding! 🐍💡

## **Reference**
- [Python Examples | Programiz. ](https://www.programiz.com/python-programming/examples.)
- [(2) 10 Python Practice Exercises for Beginners With Detailed Solutions. ](https://learnpython.com/blog/python-practice-exercises-for-beginners/.)
- [(3) Learn Python Programming - ](https://www.explorepython.com/.)
- [Python Online Practice: 79 Unique Coding Exercises (2023) ](https://www.dataquest.io/blog/python-practice/.)
- [Python Exercises, Practice, Challenges – PYnative.](https://pynative.com/python-exercises-with-solutions/.)