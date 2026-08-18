# password guesser

print("*"*20)
print("Password Guesser")
print("*"*20)

print("Note:")
print("This Guesser IS case sensitive")
print("Only '_' (underscore) is allowed as special character")


def guess():
    pas = input("\nEnter Your Password (3 digit) ")

    if len(pas) != 3:
        print("password can only be 3digit long")

    x = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890_'

    attempt = "hi"
    tryy = 0

    xlen = len(x)

    for a in range(xlen):
        for b in range(xlen):
            for c in range(xlen):
                attempt = x[a] + x[b] + x[c]
                tryy += 1
                print (attempt, "   (try", tryy, ")")

                if attempt == pas:
                    print("Got it!!")
                    print("total tries =", tryy)
                    return

guess()
                