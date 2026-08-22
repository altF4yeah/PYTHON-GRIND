# blackjack

import random

def draw_card():
    suits = ['♥', '♦', '♣', '♠']
    num = random.randint(1,13)
    card = random.choice(suits)
    if num == 1:
        name = "A"+ card
        value = 1

    elif num == 11:
        name = "J" + card
        value = 10

    elif num == 12:
        name = "Q" + card
        value = 10

    elif num == 13:
        name = "K" + card
        value = 10

    else:
        name = str(num) + card
        value = num

    return {
        "name": name,
        "value": value
    }


print()
print(">>>BLACKJACK<<<")
print()

while True:
    dhand = []
    mhand = []
    oo = 0

    for i in range(2):
        dhand.append(draw_card())
        mhand.append(draw_card())

    while True:
        tm = sum(i["value"] for i in mhand)
        mname = [i["name"] for i in mhand]

        print(f"Your hand is {mname} and total is {tm}")
        print(f"Dealer Shows {dhand[0]["name"]}")

        if tm > 21:
            print("You went over 21!!, Dealer's hand wins")
            oo = 1
            break
            
        print()
        x = input("Hit or Stand: ").upper()
        print()
        if x == "HIT":
            mhand.append(draw_card())
        elif x == "STAND":
            break


    if tm <= 21:
        print("Dealer's Turn")

        while sum(i["value"] for i in dhand) < 17:
            dhand.append(draw_card())
            print("Dealer hits",)
            print()

    td = sum(i["value"] for i in dhand)
    dname = [i["name"]for i in dhand]
        
    print(f"Final Dealer hand: {dname} (Total: {td})")
    print(f"Your final hand: {mname} (Total: {tm})")
    print()

    if oo == 0:
        if (21 - tm) < (21 - td): 
            print("You are closer to 21. Your hand wins!")

        elif td>21:
            print("Dealer got more than 21!!, Your hand wins")

        elif td == tm:
            print("It's a DRAW")

        else:
            print("Dealer is closer to 21. Dealer wins!")

    again = input("\nPlay another round? (Y/N): ").upper()
    if again != "Y":
        print("Thanks for playing!")
        break

