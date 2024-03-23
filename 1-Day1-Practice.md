# **Python Learning Lab: Day 1 - Introduction to Python**

Welcome to Python learning journey! Let's start with the basics:

## **1. What is Python?**
- Python is a friendly programming language.
- It's used for web development, software development , automate tasks, and analyze data etc.

## **2. Installing Python**
### **Linux Installation**
1. **Check if Python is Installed**:
    - Open a terminal and type the following command:
        ```bash
        python3
        ```
    - If Python is installed, you'll see the Python interactive shell (`>>>`). Type `exit()` to exit.

2. **Install Python (if needed)**:
    - **For Ubuntu/Debian (using `apt`)**:
        ```bash
        sudo apt update
        sudo apt install python3
        ```

    - **For CentOS/RHEL (using `yum`)**:
        ```bash
        sudo yum install python3
        ```
*(Ensure you have the repo configured)*

## **3. Running Python Code**
### **Interactive Shell (REPL)**
- Open a terminal and type:
    ```bash
    python3
    ```
- Try commands directly and see results instantly.

### **Script Execution**
1. Create a text file (e.g., `hello.py`) using a text editor.
2. Add this code:
    ```python
    print("Hello, World!")
    ```
3. Run it with:
    ```bash
    python3 hello.py
    ```

## **4. Basic Syntax and Data Types**
### **Comments**
- Use `#` for comments.
- Example:
    ```python
    # This is a comment
    ```

### **Variables and Printing**
1. Declare variables without specifying types:
    ```python
    name = "Alice"
    age = 30
    ```
2. Print a message using variables (two ways):
    ```python
    # Method 1: Using f-strings
    print(f"Hello, {name}! You are {age} years old.")

    # Method 2: Concatenating strings
    print("Hello, " + name + "! You are " + str(age) + " years old.")
    ```

## **Additional Example: Arithmetic Operations**
```python
# Calculate the area of a rectangle
length = 5
width = 3
area = length * width
print(f"The area of the rectangle is {area:.2f} square units.")
```

*In this example, I was confused as to why 'f' is added in print(f"The area of the circle is {area:.2f} square units.").Afterr few google search I was able to get it.Here is what I found.*

The `f` before the string in the example `print(f"The area of the circle is {area:.2f} square units.")` stands for **f-strings** (formatted string literals). Let me explain:

1. **Formatted String Literals (f-strings)**:
   - F-strings allow you to embed expressions inside string literals.
   - They are useful for creating dynamic strings with variables, calculations, and formatting.
   - The syntax is: `f"string {expression}"`, where `{expression}` is evaluated and inserted into the string.
   - The `:.2f` inside `{area:.2f}` specifies that the `area` variable should be formatted as a floating-point number with 2 decimal places.

2. **Example Explanation**:
   - In the example, `{area:.2f}` means:
       - `area`: The value of the `area` variable.
       - `:.2f`: Format the value as a floating-point number with 2 decimal places.
   - So, if `area` is, say, `78.456`, it will be displayed as `78.46`.

F-strings make it easy to create readable and concise strings with dynamic content. Feel free to use them in your Python code!

### **Difference Between Methods**
- **Method 1 (f-strings)**:
    - Preferred for its readability and simplicity.
    - Variables are directly embedded within the string using curly braces `{}`.
    - Requires Python 3.6 or later.

- **Method 2 (string concatenation)**:
    - Involves joining strings using `+`.
    - Requires explicit conversion of non-string variables (e.g., `str(age)`).



## **Reference Documents**
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html): Official Python tutorial covering essential concepts.
- [Mastering Python in 7 Days](https://medium.com/@rizmulya/mastering-python-in-7-days-a-step-by-step-guide-for-beginners-table-of-contents-aac0cfde5b59): A step-by-step guide for beginners.
- [Introduction to Python Programming Course Notes](https://www.stat.berkeley.edu/~spector/python.pdf): Comprehensive course notes.
- [Real Python Learning Path](https://realpython.com/learning-paths/python3-introduction/): Learn Python fundamentals.