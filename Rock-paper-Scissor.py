# Not Rigged Rock Paper Scissor

import random


print("-"*60)
print("ROCK PAPER SCISSORS GAME!!")
print("-"*60)
print()

def game():
    x = ["rock", "paper", "scissors"]
    score = 0
    while True:
        inp = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower().strip()

        if inp == "quit":
            print("Thanks for playing!!")
            print("Your total Score is", score)
            break

        if inp not in x:
            print("Invalid Input, Please Try Again")
            continue

        pc = random.choice(x)
        print(f"I choose: {pc} ")

        if inp == pc:
            print("It's a draw.")
            print("curent score =", score)

        elif (inp == "rock" and pc == "scissors") or (inp == "paper" and pc == "rock") or (inp == "scissors" and pc == "rock"):
            print("You WINNNN!!!!")
            score += 1
            print("curent score =", score)

        else:
            print("You Lost :(")
            print("curent score =", score)

game()