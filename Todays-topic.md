
### **Day 4-6: Control Structures**

#### **1. Loops (for and while)**

##### **a. While Loop**
1. Write a Python program that prints the first **10 even numbers** using a `while` loop.

```python
# Solution:
count = 1
while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1
```

2. Create a `while` loop that calculates the **sum of numbers from 1 to 100**.

```python
# Solution:
total = 0
number = 1
while number <= 100:
    total += number
    number += 1
print(f"Sum of numbers from 1 to 100: {total}")
```

##### **b. For Loop**
1. Generate a list of **squares of numbers from 1 to 10** using a `for` loop.

```python
# Solution:
squares = []
for num in range(1, 11):
    squares.append(num ** 2)
print("Squares of numbers from 1 to 10:", squares)
```

2. Write a program that prints the **factorial of a given number** using a `for` loop.

```python
# Solution:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5  # Change this to any positive integer
print(f"Factorial of {number} is {factorial(number)}")
```

#### **2. Working with Lists and Dictionaries**

##### **a. Lists**
1. Given a list of numbers, write a function that returns the **average value**.

```python
# Solution:
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

my_numbers = [10, 20, 30, 40, 50]
print(f"Average value: {calculate_average(my_numbers)}")
```

2. Create a program that **reverses a list** without using the built-in `reverse()` method.

```python
# Solution:
def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

original_list = [1, 2, 3, 4, 5]
print(f"Reversed list: {reverse_list(original_list)}")
```

##### **b. Dictionaries**
1. Given a dictionary of student names and their corresponding scores, find the **highest scoring student**.

```python
# Solution:
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

highest_score = max(student_scores.values())
top_students = [name for name, score in student_scores.items() if score == highest_score]
print(f"Highest score: {highest_score} by {', '.join(top_students)}")
```

2. Write a function that **merges two dictionaries** into a new one.

```python
# Solution:
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(f"Merged dictionary: {merge_dictionaries(dict1, dict2)}")
```
--------

### **Day 4-6: Control Structures**

#### **1. Loops (for and while)**

##### **a. While Loop**

1. **FizzBuzz Challenge**:
    - Write a Python program that prints numbers from **1 to 100**.
    - For multiples of **3**, print "Fizz" instead of the number.
    - For multiples of **5**, print "Buzz".
    - For numbers that are multiples of both **3 and 5**, print "FizzBuzz".

    ```python
    # Solution:
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    ```

2. **Prime Number Checker**:
    - Create a function that checks whether a given positive integer is a **prime number**.
    - A prime number is only divisible by 1 and itself.

    ```python
    # Solution:
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    user_input = int(input("Enter a positive integer: "))
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
    ```

##### **b. For Loop**

1. **Palindrome Checker**:
    - Write a program that checks if a given word or phrase is a **palindrome** (reads the same backward as forward).
    - Ignore spaces and consider case-insensitivity.

    ```python
    # Solution:
    def is_palindrome(word):
        cleaned_word = word.lower().replace(" ", "")
        return cleaned_word == cleaned_word[::-1]

    user_word = input("Enter a word or phrase: ")
    if is_palindrome(user_word):
        print(f"{user_word} is a palindrome!")
    else:
        print(f"{user_word} is not a palindrome.")
    ```

2. **Sum of Squares**:
    - Calculate the sum of squares of the first **n positive integers**.

    ```python
    # Solution:
    def sum_of_squares(n):
        return sum(i**2 for i in range(1, n + 1))

    n_value = int(input("Enter a positive integer (n): "))
    print(f"Sum of squares for the first {n_value} positive integers: {sum_of_squares(n_value)}")
    ```

#### **2. Working with Lists and Dictionaries**

##### **a. Lists**

1. **Unique Elements in a List**:
    - Given a list, create a new list containing only the **unique elements** (no duplicates).

    ```python
    # Solution:
    def get_unique_elements(my_list):
        return list(set(my_list))

    original_list = [1, 2, 3, 2, 4, 5, 3]
    unique_elements = get_unique_elements(original_list)
    print(f"Unique elements: {unique_elements}")
    ```

2. **List Comprehension**:
    - Generate a list of **squares of even numbers** from 1 to 20 using list comprehension.

    ```python
    # Solution:
    even_squares = [num**2 for num in range(1, 21) if num % 2 == 0]
    print("Squares of even numbers:", even_squares)
    ```

##### **b. Dictionaries**

1. **Word Frequency Counter**:
    - Given a sentence, create a dictionary where keys are words, and values are their **frequency of occurrence**.

    ```python
    # Solution:
    def count_word_frequency(sentence):
        words = sentence.lower().split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

    user_sentence = input("Enter a sentence: ")
    word_frequency = count_word_frequency(user_sentence)
    print("Word frequency:", word_frequency)
    ```

2. **Dictionary Merge**:
    - Merge two dictionaries, giving priority to the second dictionary in case of overlapping keys.

    ```python
    # Solution:
    def merge_dictionaries(dict1, dict2):
        merged_dict = dict1.copy()
        merged_dict.update(dict2)
        return merged_dict

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3,
