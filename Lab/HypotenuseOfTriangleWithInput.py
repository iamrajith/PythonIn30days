#!/home/rajith/anaconda3/bin/python3
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