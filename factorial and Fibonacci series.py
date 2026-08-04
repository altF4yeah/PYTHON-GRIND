# practice of Recursion
# Factorial and Fibonacci series Calculator

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def fibo(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibo(m-1) + fibo(m-2)

print("=" * 60)
print("Factorial and Fibonacci series Calculator")
print("=" * 60)

choice = "x"
while True:
    print()
    print("You can press Q to stop the program")
    print()
    print("A. Factorial Calculator")
    print("B. Fibonacci series Calculator")
    print()
    choice = input("choose (A or B): ").upper()
    if choice == "A":
        print("opening Factorial Calculator")
        n = int(input("Enter whose factorial value you need to find: "))
        fn = int(fact(n))
        print("factorial value of", n, "=", fn)
        
    elif choice == "B":
        print("opening Fibonacci series Calculator")
        m = int(input("Enter the number whose Fibonacci value you need to find: "))
        fm = int(fibo(m))
        print("Fibonacci value of", m, "=", fm)
    elif choice == "Q":
        print("Stopping the program...")
        print("program stopped.")
        break

    else:
        print("Invalid Input!!")
        print("You can only type either A or B")
        print("or maybe Q to stop the program :(")
        continue