# rock paper scissors
def a():
    print("L u lost")

r = "rock"
p = "paper"
s = "scissor"
x = "love you"

while (x == r or p or s):
    x = input("ROCK PAPER SCISSOR: " ).lower()

    if (x == r):
        print(p)
        a()
    elif(x == p):
        print(s)
        a()
    elif(x == s):
        print(r)
        a()
    else:
        print("You can only choose ROCK, PAPER OR SCISSOR" )