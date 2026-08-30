# alarm

import datetime
import time
import threading

L = []

def alarm_set():
    print("Set your alarm time in 24hr format (HH:MM:SS) format: ")
    alarm_time = input("(Example 07:30:00) ").strip()
    L.append(alarm_time)

    print(f"Your alarm of {alarm_time} has added to your alarms")

def check_alarm():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        for i in L:
            if i == current_time:
                print()
                print()
                print("The alarm is ringing")
                print(i)
        time.sleep(1)

def view_alarm():
    print()
    if len(L) == 0:
        print("No alarm found... please set an alarm first")
        print()
    else:
        print("Your current alarms are:")
        for i in range(0, len(L)):
            print(i+1, L[i])

def edit_alarm():
    print()
    if len(L) == 0:
        print("No alarm found... please set an alarm first")
        print()
    else:
        index = int(input("Enter the index number of the alarm to edit"))
        print("Your Selected alarm is: ")
        print(index, L[index-1])

        recheck = input("type YES to confirm ").upper()
        if recheck == "YES":
            new_alarm = input("Enter the new alarm: ")
            L[index-1] = new_alarm

            print("Saving...")
            time.sleep(1)
            print("Saved Successfully")

def delete_alarm():
    print()
    if len(L) == 0:
        print("No alarm found... please set an alarm first")
        print()
    else:
        index = int(input("Enter the index number of the alarm to delete"))
        print("Your Selected alarm is: ")
        print(index, L[index-1])

        recheck = input("type YES to confirm ").upper()
        if recheck == "YES":
            del L[index-1]
            print()

            print("Deleting the alar...")
            time.sleep(1)
            print("Alarm Successfully deleted")

def main():
    print()
    print("=" * 30)
    print("Alarm".center(20))
    print("=" * 30)
    print()

    threading.Thread(target=check_alarm, daemon=True).start()

    while True:
        print()
        print("1. Set an alarm")
        print("2. View your alarms")
        print("3. Edit your alarms")
        print("4. Delete your alarms")
        print("5. Exit")
        print()

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            alarm_set()

        elif choice == 2:
            view_alarm()

        elif choice == 3:
            edit_alarm()

        elif choice == 4:
            delete_alarm()

        elif choice == 5:
            print("Closing the alarm app!")
            for i in range(1,4):
                print("Stopping", "."*i)
                time.sleep(1)
            print("Program Stopped.")
            break

        else:
            print("Invalid Input!, try again")
            continue

main()