# Number Guessing game with attempt counter

print("Number Guessing Game".center(50))
print("points to remember:")
print("1. You have to guess a random number to win")
print("2. there is also an attempt counter to see your number of attempts!!")
print("3. hint: the number is of 2digit")

i=0
attempts = 0

while True:
    i = int(input("enter a number: "))
    if (i != 48):
        print("Try again")
        attempts += 1
        print("Number of attempts =", attempts)
        continue
    else:
        print("GGs, this is the correct number")
        print("Your total number of attempts are", attempts)
        break