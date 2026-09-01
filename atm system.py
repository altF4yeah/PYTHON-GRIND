# ATM System

bal = 0
account = 0
user = None
pwd = None
disp = None


def create():
    global bal, user, disp, pwd

    print("You have chosen the Create Account option.")
    email = input("Enter Your email id: ")
    phone = input("Enter Your Phone number: ")
    age = int(input("Enter your age "))

    if age <= 18:
        print("You need to be 18 in order to make an account")
        return
    else:
        print("Valid Age")

    user = input("Choose Your Username: ")
    disp = input("Enter your display name: ")

    while True:
        pwd = input("Choose Your Password: ")
        pwdc = input("Re-enter your pass: ")

        if pwd == pwdc:
            print("Password Confirmed!")
            break
        else:
            print("Password didn't match, try again")
            continue

    print("Account Created!!")
    bal = float(input("Enter Your Initial Balance: "))

def login():
    global account

    print("You have choosen the Login option")
    print()

    if user is None:
        print("No account found. Please create an account first.")
        return

    while True:
        username = input("Enter your username: ")
        password = input("Enter Your password: ")
        print()

        if username == user and password == pwd:
            print("Both password and username is correct!")
            print("Account Logged in")
            account = 1
            break
        else:
            print("Oops Username or password is incorrect")
            print("Try again")
            continue

def check():
    print("You have choosen the Check Balance option")
    print()
    if account == 1:
        print(f"Your account {disp} is logged in ")
        print(f"Your current balance is: {bal}rs")
    else:
        print("Your account is not logged in")

def deposit():
    global bal

    print("You have chosen the Deposit Money option")
    print()
    if account == 1:
        print(f"Your account {disp} is logged in ")
        dep = float(input("Enter Your deposit amount "))
        bal += dep
        print("After deposit your current balance is", bal, "rs")
    else:
        print("Your account is not logged in")

def withdraw():
    global bal

    print("You have chosen the Withdraw Money option")
    print()
    if account == 1:
        print(f"Your account {disp} is logged in ")
        draw = float(input("Enter your withdraw amount "))
        if draw > bal:
            print("Insufficient balance!")
        else:
            bal -= draw
            print("After withdraw your current balance is", bal, "rs")
    else:
        print("Your account is not logged in")

def logout():
    global account

    print("You have chosen the Logout option")
    print()
    if account == 1:
        print(f"Logging out from {disp} account")
        account = 0
    else:
        print("Your account not logged in anyway")

def main():
    print()
    print("=" * 50)
    print("XYZ ATM".center(45))
    print("=" * 50)
    print()

    print("What task you want to do today? ")

    while True:
        print()
        print("1. Create Account")
        print("2. Login")
        print("3. Check Balance")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Logout")
        print()

        task = int(input("Select the number according to your task "))
        print()

        if task == 1:
            create()
        elif task == 2:
            login()
        elif task == 3:
            check()
        elif task == 4:
            deposit()
        elif task == 5:
            withdraw()
        elif task == 6:
            logout()
            break
        else:
            print("Invalid option, please try again.")

main()