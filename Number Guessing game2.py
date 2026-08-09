# random Number Guessing game 

import random

print("*"*30)
print("Number Guessing game")
print("*"*30)
print()

print("0 to stop the game\n")
print("Select Difficulty Level")
print("1. Easy  (1-Digit number)")
print("2. Medium  (2-Digit number)")
print("3. Hard  (3-Digit number)")

diff = int(input("\n1/2/3 "))
attempts = 0
while True:
    if diff == 1:
        print("(Gamemode Easy)")
        ediff = random.randint(1,9)
        guess = int(input("Enter Your guess: "))
        if guess != ediff:
            print("Try again")
            attempts += 1
            print("attempt", attempts)
        elif guess == ediff:
            print("GG, You win!!!")
            print("total attempts =", attempts)
            break
        print()
    elif diff == 2:
        print("(Gamemode Medium)") 
        mdiff = random.randint(10,99)
        guess = int(input("Enter Your guess: "))
        if guess != mdiff:
            print("Try again")
            attempts += 1
            print("attempt", attempts)
        elif guess == mdiff:
            print("GG, You win!!!")
            print("total attempts =", attempts)
            break
        print()
    elif diff == 3:
        print("(Gamemode Hard)")
        hdiff = random.randint(100,999)
        guess = int(input("Enter Your guess: "))
        if guess != hdiff:
            print("Try again")
            attempts += 1
            print("attempt", attempts)
        elif guess == ediff:
            print("GG, You win!!!")
            print("total attempts =", attempts)
            break
        print()
    elif diff == 0:
        print("Stopping the program...")
        break
    else:
        print("You can only choose 0/1/2/3")