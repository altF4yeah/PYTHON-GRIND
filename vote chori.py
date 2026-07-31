# VOTEEEEEE IS IMPORTANT 

print("="*60)
print("Welcome to Voting Booth")
print("="*60)

print()
age = int(input("enter your age: "))
print()

if (age >= 18):
    print("yeah you are eligible \n\n voting list")
    print("1. Aam Aadmi Party")
    print("2. Bharatiya Janata Party")
    print("3. Indian National Congress")
    print("4. cockroach janta party")
    print("5. Bahujan samaj party")

    choice = int(input("choose 1-5 "))
    if (choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5):
        print("Vote has been given to BJP ")
    else:
        print("enter valid party")
else:
    print("you are a kid rn, try when u r 18")
