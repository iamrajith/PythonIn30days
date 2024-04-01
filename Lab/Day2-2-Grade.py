#!/home/rajith/anaconda3/bin/python3
score = float(input("enter the exam score:"))

if score >= 90:
    print("You got A grade")
elif score >= 80:
    print("You got B grade")
elif score >= 70:
    print("You got C grade")
elif score >= 60:
    print("You got D grade")
else:
    print("You failed this time, better luck for the next time")