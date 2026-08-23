# time stopping game

import time
import random

def game():
    random_time = int(random.randint(1, 15))
    print("Your random time is:", random_time)    
    start = input("Press enter to start ").upper()

    if start == "":
        timer_start = time.time()
        stop = input("Press enter again to stop ").upper()

        if stop == "":
            timer_stop = time.time()
            final_time = float(timer_stop - timer_start)
            print("You stopped exactly after:", final_time)
            final_time = int(final_time)

            if (final_time == random_time):
                print("You won")

            else:
                print("You lost")

        else:
            print("invalid input")
        
    else:
        print("invalid input")

print()
print("Time Stopping Game")
print("stop the timer at the exact second to win!!")
print("you will still win if u stop the timer in +1 second range")
print()

while True:
    game()
    print()
    again = input("Do you want to play again? (Y/N)").upper()
    if again != "Y":
        print("Thank you for playing.")
        print("Stopping the program")
        break