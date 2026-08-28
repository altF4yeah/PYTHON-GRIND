#Password Evaluator

def evaluator(pwd):
    uc = False
    lc = False
    num = False
    spec = False

    for i in pwd:

        if i.isupper():
            uc = True

        elif i.islower():
            lc = True

        elif i.isdigit():
            num = True

        else:
            spec = True

    score = 0

    if len(pwd) >= 8:
        score += 1

    if uc:
        score += 1

    if lc:
        score += 1

    if num:
        score += 1

    if spec:
        score += 1

    if score <= 2:
        print("Weak Password!!, Change it immediately")

    elif score <= 4:
        print("Medium Password!, Change it soon")

    else:
        print("Strong Password!!")

def main():
    print()
    print("<"*15,">"*15)
    print("Password Evaluator".center(30))
    print("<"*15,">"*15)
    print()

    while True:
        pwd = input("Enter Your password that you wanna evaluate: ")
        evaluator(pwd)

        choice = input("Do you want to play again? (Y/N) ").lower()
        if choice == "y":
            continue
        elif choice == "n":
            print("Stopping the program...")
            break
        else: 
            print("Invalid Input, continuing anyway...")
            

main()