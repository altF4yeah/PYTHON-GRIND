# simple stopwatch

import time

print("^"*10)
print("Stopwatch")
print("^"*10)

while True:
    print()
    x = input("Do you want to start the stopwatch?? (Y/N): ").lower()
    if x == "y":
        print("....")
        print("Stopwatch started")
        print()
        start = time.time()

        stop = input("enter Q to stop the timer. ").lower()
        if stop == "q":
            end = time.time()
            print("Stopwatch stopping...")

            t = end-start
            h = int(t//3600)
            m = int((t%3600)//60)
            s = int(t%60)
            ms = int((t%1)*1000)

            print(f"{h} hours {m} minutes {s} seconds and {ms} millisecond have passed")
        else:
            print()
            print("Enter a valid input")

    elif x == "n":
        print("Stopping the program")
        break

    else:
        print()
        print("Enter a valid input")