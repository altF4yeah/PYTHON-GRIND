# Magic 8ball 

import random

print("&"*29)
print("()()()()Magic 8-ball()()()()")
print("&"*29)

print()
print("Ask a yes-or-no question, and I will shake the Magic 8 Ball for you.")
print("(enter q to stop the program)")
print()

List = [
  "It is certain",
  "It is decidedly so",
  "Without a doubt",
  "Yes definitely",
  "You may rely on it",
  "As I see it, yes",
  "Most likely",
  "Outlook good",
  "Yes",
  "No",
  "Signs point to yes",
  "Reply hazy, try again",
  "Ask again later",
  "Better not tell you now",
  "Cannot predict now",
  "Concentrate and ask again",
  "Don't count on it",
  "My reply is no",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful"
]

while True:

    inp = input("Ask me any question: ").lower().strip()
    x = random.choice(List)

    if inp == "q":
        print()
        print("Stopping the program...")
        print()
        break

    print()
    print(">>>>", x)
    print()