time = int(input("enter the current time (in 24hr system and only hrs)"))
if (time > 5 and time <= 12):
    print("good morning")
    if (time > 5 and time <=8):
        print("early morning")
    else :
        print("late morning")
elif (time > 12 and time <= 17):
    print("Good afternoon")
elif (time > 17 and time <= 21):
    print("good evening")
elif (time > 21 and time < 24 and time >=5):
    print("good night")
else :
    print("good midnight")