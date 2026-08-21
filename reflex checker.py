import time
import random

def reflex():
    x_time = int(random.randint(1, 7))
    time.sleep(x_time)
    start_time = time.time()
    ent = input("Press Enter")

    if ent == "":
        end_time = time.time()
        final_time = int((end_time - start_time) * 1000)
        if final_time == 0:
            print("Clicked too soon")
        else:
            print(f"Your reflex is: {final_time}ms")
            print()


print()
print(";;;;REFLEX CHECKER;;;;")
print()

while True:
    ready = input("Press Enter if you are ready! ")
    if ready == "":
        reflex()
        print()
        again = input("Press Y to play again: ").upper()
        if again != "Y":
            break
    else:
        print("Invalid Input")
        continue