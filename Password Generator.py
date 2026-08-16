# Password Generator 

import random

print("!"*30)
print("Password Generator")
print("!"*30)
print()

print("Creating a Strong password is very important in this era")
print()
print('According to "America Cyber Defense Agency"')
print("These are some basic rules you should follow while creating a password")
print("1. Make them long")
print("2. Make them random")
print("3. Make them unique")

low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
sp = "!#$%&'()*+,-./:;<=>?@[]^_ {|}~`."


a = low + up + num + sp

while True:
    pwd = "".join(random.sample(a,16))

    inp = input("Press Y to see a sample password (N to quit):").lower()

    if inp == "y":
        print()
        print(pwd)
        print()

    elif inp == "n":
        print()
        print("Program Stopped.")
        break

    else:
        print()
        print("Enter a valid input(Y or N)")
        continue