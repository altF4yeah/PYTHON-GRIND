# Pomodoro timer

import time

pomo = 50*60
sb = 10*60
lb = 30*60
cycle = 3

def settings_show():

    print()
    print("Current Setting:")
    print("pomo", pomo/60, "mins")
    print("Short Break", sb/60, "mins")
    print("Long Break", lb/60, "mins")
    print("Cycle", cycle)

def default_setting():
    global pomo, sb, lb, cycle

    pomo = 50*60
    sb = 10*60
    lb = 30*60
    cycle = 3
    settings_show()

def custom_setting():
    global pomo, sb, lb, cycle

    pomo = int(input("Enter pomodoro time (in mins)"))*60
    sb = int(input("Enter Short Break time (in mins)"))*60
    lb = int(input("Enter Long Break time (in mins)"))*60
    cycle = int(input("Enter Number of Cycles: "))
    settings_show()

def settings():

    print()
    print("1/ Default Settings ")
    print("2/ Create New")
    print("3/ Back")
    print()

    choice = int(input("Enter Your Choice (1-3) "))

    if choice == 1:
        default_setting()

    elif choice == 2:
        custom_setting()

    elif choice == 3:
        return

def timer(duration):
    remaining = duration
    while remaining > 0:
        
        hours = remaining // 3600
        mins = (remaining % 3600) // 60
        seconds = remaining % 60

        if remaining >= 3600:
            print(f"{hours:02d}:{mins:02d}:{seconds:02d}", end="\r")
        else:
            print(f"{mins:02d}:{seconds:02d}", end="\r")

        time.sleep(1)
        remaining -= 1

def start_cycle():

    i = 1
    while True:
        timer(pomo)
        print("Pomodoro Finished! Short Break Starting")

        timer(sb)
        print("Short Break is Over! Pomodoro Starting")

        print("Cycle number", i)

        if i % cycle == 0:
            print("Cycle Over!!! Starting Long Break")
            timer(lb)

        i += 1

        choice = input("Continue? (Y to continue, E to exit to menu) ").lower()
        if choice == "e":
            return
        elif choice == "y":
            continue
        else:
            print("Invalid input, continuing anyway...")

def main():

    print()
    print("+"*30)
    print("Pomodoro Timer".center(20))
    print("+"*30)
    print()

    while True:
        print()
        print("1. Start Cycle")
        print("2. Settings")
        print("3. Exit")
        print()

        choice = int(input("Enter your choice(1-3) "))

        if choice == 1:
            start_cycle()
            
        elif choice == 2:
            settings()

        elif choice == 3:
            print("Exiting the program,,,")
            break

        else:
            print("Invalid Input")
            continue

main()