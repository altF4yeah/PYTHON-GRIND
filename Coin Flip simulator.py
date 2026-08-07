# Coin Flip simulator (streak counter)

import random

x = ["Heads", "Tails"]

print("-"* 30)
print("Coin Flip Simulator")
print("-"* 30)

hstreak = 0
tstreak = 0

while True:

    inp = input("\nDo you want to flip a Coin?? (Y or N) ").upper().strip()
    y = random.choice(x)
    if inp == "Y":
        if y == "Heads":
            print(f"computer choose {y}")
            if tstreak > 0:
                print(">>RIP STREAK<<")
                print(">>Streak reseted.<<")
            hstreak += 1
            tstreak = 0
            print("Your current streak is", hstreak)

        elif y == "Tails":
            print(f"computer choose {y}")
            if hstreak > 0:
                print(">>RIP STREAK<<")
                print(">>Streak reseted.<<")
            tstreak += 1
            hstreak = 0
            
            print("Your current streak is", tstreak)
        
        else:
            print("Rip Streak")
            continue
    
    elif inp == "N":
        print("Stopping the program")
        break
    else:
        print("Invalid Input")
        continue