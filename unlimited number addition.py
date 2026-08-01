# unlimited user input addition calculator

print("<Calculator> \n      some points:" .center(35))
print("1. This calculator can add unlimited numbers.")
print("2. Type Y if u wish to add more numbers ")
print("3. Type N if u want to see the result and the set of numbers")
print("4. Type 'quit' at any point to exit the program")
print("5. type X to see all ur inputs")


def ksa(list):
    list = []
    ask = "hmm"
    i = 1
    while True:
        print("this is your number ", i)
        num = float(input("Enter your number "))
        ask = input("do u want to add another number? (Y/N or QUIT) ").upper()
        list.append(num)
        if ask == "Y":
            i += 1
            continue

        elif ask == "N":
            print("the sum of the give numbers is: ",sum(list))
            print(list)
            print("if you wish, u can still add numbers")
            i += 1
            continue

        elif ask == "QUIT":
            print("You have exited from the calculator")
            list = []
            return

        elif ask == "X":
            print("your inputs are: ", list)

        else:
            print("only type Y/N or quit")
            print(list)

ksa(list)
