# Age Calculator

from datetime import date

print()
print("AGE Calculator".center(50))
print("Enter Your date  of birth and this program will tell how old r u")
print()

Y = int(input("enter your birth year (in YYYY format): "))
M = int(input("enter your birth month (in MM format): "))
D = int(input("enter your birth date (in DD format): "))

print()
print("Your Bday is on:", D, "/", M, "/",  Y)

x = date.today()
a = int(x.strftime("%Y"))
b = int(x.strftime("%m"))
c = int(x.strftime("%d"))

print("Today's date is:", c, "/", b, "/", a)
print()

years = a-Y
month = b-M
days = c-D

if days<0:
    month -= 1
    days += 30

if month<0:
    years -= 1
    month += 12


print("your current age is: ")
print(f"{years} years, {month} month and {days} days")

