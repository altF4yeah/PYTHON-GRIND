# Multi function Calculator 


print("=" * 60)
print("Multi-function Calculator".center(60))
print("=" * 60)


choice = 0
while True:
    print("You can press 0 in ur choose option to stop this program.")
    print(">> What You wanna Calculate")
    print("1. Body Mass Index")
    print("2. Quadratic Equation")
    print("3. Pythagorean Theorem")
    print("4. Ideal Gas Law")
    print("5. Newton's second law of motion")
    print()
    choice = int(input("Choose (1-5): "))
    print()

    if choice == 1:
        print()
        print("Opening Body Mass index Calculator")
        print()
        weight = float(input("Enter weight (in Kg): "))
        height = float(input("Enter height (in m):"))

        print("your entered weight is", weight)
        print("your entered height is", height)
        print()
        print("BMI =", weight/(height)**2)
        print()

    elif choice == 2:
        print()
        print("Opening Quadratic Equation Calculator")
        print()
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b:"))
        c = float(input("Enter value of c:"))

        print("your entered value of a", a)
        print("your entered value of b", b)
        print("your entered value of c", c)
        print()
        print("after applying the quadratic equation")
        print("x =", ((0-b)+((b**2)-4*a*c)**0.5)/(2*a), "and", ((0-b)-((b**2)-4*a*c)**0.5)/(2*a))
        print()

    elif choice == 3:
        print()
        print("Opening Pythagorean Theorem Calculator")
        print()
        per = float(input("Enter length of perpendicular: "))
        bas = float(input("Enter length of base: "))

        print("your entered perpendicular is", per)
        print("your entered base is", bas)
        print()
        print("Hypotenuse =", ((per**2)+(bas**2))**0.5)
        print()

    elif choice == 4:
        print()
        print("Opening Ideal Gas Law Calculator")
        print()
        print("Just press 0 on the finding variable")
        P = float(input("enter value of P: "))
        V = float(input("enter value of V: "))
        N = float(input("enter value of N: "))
        R = float(input("enter value of R: "))
        T = float(input("enter value of T: "))
        pvnrt = input("Value of what you wanna find ").lower()

        if pvnrt == "p":
            print("Value of p is", (N*R*T)/V)
            print()
        elif pvnrt == "v":
            print("Value of v is", (N*R*T)/P)
            print()
        elif pvnrt == "n":
            print("Value of n is", (P*V)/(R*T))
            print()
        elif pvnrt == "r":
            print("Value of r is", (P*V)/(N*T))
            print()
        elif pvnrt == "t":
            print("Value of t is", (P*V)/(N*R))
            print()
        else:
            print("Not valid ")
            print()

    elif choice == 5:
        print()
        print("Opening 'Newton's Second law of motion' Calculator")
        print()
        mass = float(input("Enter mass: "))
        acc = float(input("Enter acceleration: "))

        print("your entered mass is", mass)
        print("your entered acc is", acc)
        print()
        print("Force =", mass*acc)

    elif (choice == 0):
        print("stopping the program....")
        print("program stopped.")
        break

    else:
        print("Not Valid input, (only enter 1-5)")
        print()
        continue