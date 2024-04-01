# 30 Days of Python: Day 2 - Python Functions with user input

Let's explore Python functions that calculate the hypotenuse of a triangle using user input. 

1. **Calculate Hypotenuse**:
   - Compute the hypotenuse of a right triangle using the Pythagorean theorem.

```python
# Define a function called "hypotenuse"
def hypotenuse(a, b):
    """
    Calculates the hypotenuse of a right triangle.
    
    Args:
        a (float/int): Length of side A.
        b (float/int): Length of side B.
    
    Returns:
        float: Hypotenuse length.
    """
    return (a**2 + b**2) ** 0.5

# Prompt the user to input the lengths of the two sides
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))

# Print the calculated hypotenuse with two decimal places
print(f"The hypotenuse is approximately {hypotenuse(side_a, side_b):.2f}")
```


2. **Age Classifier**:
   - Classify a person's age as an infant, child, teenager, or adult.

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

     user_age = int(input("Enter your age: "))
     print(f"Your age group is {classify_age(user_age)}")
     ```


Remember to handle user input validation (e.g., non-numeric input) and customize the examples further as needed.

## References
1. [Stack Overflow: Age Classifier Program](https://stackoverflow.com/questions/32528468/how-to-use-if-and-else-statements-to-achieve-age-classifier-program)
2. [PyForSchool: Age Classifier](https://www.pyforschool.com/assignment/conditional/age-classifier.html)
3. [Python OOP Exercise: Person Class with Age Calculation](https://www.w3resource.com/python-exercises/oop/python-oop-exercise-2.php)
4. [CodeEase: Print() Function in Python](https://www.codeease.net/programming/python/print-python-age-input)
5. [GeeksforGeeks: Calculate Age in Years](https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/)
