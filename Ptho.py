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
