#!/home/rajith/anaconda3/bin/python3
def calssify_age(age):
    if age <=1:
        return "Infant"
    elif 1 < age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    else:
        return "Adult"
print(calssify_age(13))
