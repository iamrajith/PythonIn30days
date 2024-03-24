#!/home/rajith/anaconda3/bin/python3
def divide(a,b):
    "Divide two numbers"
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
result = divide(10, 2)

print(f"The result is {result:.2f}.")