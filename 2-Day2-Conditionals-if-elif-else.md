Certainly! Let's explore some practical lab exercises to reinforce your understanding of conditionals (if, elif, else) in Python. These exercises cover various scenarios and will help you practice using decision-making statements effectively.

### **1. Checking Even or Odd**
Write a Python program that takes an integer as input and prints whether it is even or odd using an `if-else` statement.

```python
# Check if a number is even or odd

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
```

Example usage:
- Input: `12`, Output: `12 is even.`
- Input: `15`, Output: `15 is odd.`

### **2. Grade Calculator**
Create a Python program that calculates and displays the grade of a student based on their score. The grading criteria are as follows:
- Score >= 90: A
- 80 <= Score < 90: B
- 70 <= Score < 80: C
- 60 <= Score < 70: D
- Score < 60: F

```python
# Calculate and display the grade
score = float(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

Example usage:
- Input: `75`, Output: `C`
- Input: `89`, Output: `B`

### **3. Leap Year Checker**
Write a Python program that checks if a given year is a leap year or not. A leap year is divisible by 4, except for years divisible by 100 but not divisible by 400.

```python
# Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```
