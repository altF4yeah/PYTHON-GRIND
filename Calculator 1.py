x = 1
y = 1
o = "love you"
while (o =="+" or "-" or "*" or "/" or "%" or "^" or "gif"):
    X = float(input("Enter Number 1: "))
    Y = float(input("Enter Number 2: "))
    o = (input("Choose Your operation:\n (+, -, *, /, %, ^, gif) "))

    if (o == "+"):
        print(X+Y)
    elif(o == "-"):
        print(X-Y)
    elif(o == "*"):
        print(X*Y)
    elif(o == "/"):
        print(X/Y)
    elif(o == "%"):
        print(X%Y)
    elif(o == "^"):
        print(X**Y)
    elif(o == "gif"):
        print(X//Y)
    else:
        print("try another operator")
