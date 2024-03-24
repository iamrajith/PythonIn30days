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

# Check if the script is being run directly
side_a = float(input("Please enter the length of side A: "))
side_b = float(input("Please enter the length of side B: "))

side_c = hypotenuse(side_a, side_b)

print(f"The hypotenuse of the triangle with {side_a} and {side_b} is {side_c:.2f}")