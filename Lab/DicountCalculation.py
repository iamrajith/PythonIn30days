#!/home/rajith/anaconda3/bin/python3
def calculate_discount(age):
    if age <= 3 :
        print("Infants below age 3 years, no entry fee")
    elif age <= 6 :
        print("Children between the ages of 3 and 6 can enjoy a discount of 75%.")
    elif age <= 13 :
        print("Children aged between 6 and 13 are eligible to receive a 50% discount")
    elif age <= 15 :
        print("Children between the ages of 13 and 15 are eligible for a 25% discount.")
    elif age <= 45 :
        print("The actual fare applies to individuals aged between 15 and 45 years old.")
    elif age <= 60 :
        print("For individuals aged between 60 and 75, there is a 50% discount available.")
    else:
        print("Fro those who are above 75 can enjoy 75% off")

input_age = int(input("Please specify your age :"))
print(f"{calculate_discount(input_age):}.")

