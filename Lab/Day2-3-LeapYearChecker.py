#!/home/rajith/anaconda3/bin/python3
year = int(input("Enter the year:"))

if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0 ):
    print(f"The year {year} is leap year.")
else:
    print(f"The year {year} is not a leap year.")