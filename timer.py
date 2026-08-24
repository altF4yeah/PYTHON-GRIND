# timer

import time

def timer():
    sec = int(input("When you want to stop this timer? (in seconds) "))

    while sec>0:
        mins = (sec % 3600)// 60
        seconds = sec % 60
        hours = sec // 3600

        if sec >= 3600:
            print(f"{hours:02d}:{mins:02d}:{seconds:02d}", end="\r")
        else:
            print(f"{mins:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
        sec -= 1
        
    print()
    print("Time's UP")

while True:
    timer()
    choice = input("Do you want to play again? (Y/N) ").lower()
    if choice != "y":
        break