# RPG GAMEEE

import random

moves = ["attack", "block", "heal"]
atk_dmg = [10, 20, 30]
heal_hp = [10, 15, 20]
user_hp = 100
pc_hp = 100

char = input("Enter Name of your character: ")

print()
print(f"Welcome {char}, I heard tales about you around the world")
print("I am glad you came to save this village")
print("'Calculus', this is the name of the villain who keeps attacking our village")
print(f"OH! Here he comes again, PLEASE HELP US {char}")
print()

while True:
    user_move = input(f"What Will {char} do?? \n Attack/Block/Heal ").lower().strip()
    pc_move = random.choice(moves)

    if user_move == "attack" and pc_move == "attack":
        user_hp = user_hp - random.choice(atk_dmg)
        pc_hp = pc_hp - random.choice(atk_dmg)
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "attack" and pc_move == "block":
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        print("Your attack got blocked by Calculus")
        print()
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "attack" and pc_move == "heal":
        pc_hp = pc_hp - random.choice(atk_dmg)
        pc_hp = pc_hp + random.choice(heal_hp)
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "block" and pc_move == "attack":
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        print("You Blocked Calculus attack!!")
        print()
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "block" and pc_move == "block":
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        print("Nothing happened, but both look like fools")
        print()
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "block" and pc_move == "heal":
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        pc_hp = pc_hp + random.choice(heal_hp)
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "heal" and pc_move == "attack":
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        user_hp = user_hp + random.choice(heal_hp)
        user_hp = user_hp - random.choice(atk_dmg)
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "heal" and pc_move == "block":
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        user_hp = user_hp + random.choice(heal_hp)
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    elif user_move == "heal" and pc_move == "heal":
        print()
        print("Calculus choosed to", pc_move, "and", f"{char} choosed", user_move)
        print()
        user_hp = user_hp + random.choice(heal_hp)
        pc_hp = pc_hp + random.choice(heal_hp)
        print("Health Status: ")
        print("Calculus HP:", pc_hp)
        print(f"{char} HP:", user_hp)

    else:
        print("Invalid Input")
        continue

    if user_hp <= 0:
        print()
        print("GAME OVER!!!")
        break

    elif pc_hp <= 0:
        print()
        print(f"I KNEW IT ONLY {char} COULD HAVE SAVED US!! ")
        print("You WON")
        break

    elif pc_hp <= 0 and pc_hp <= 0:
        print("wtf both died should we be happy or sad")
        print("SECRET ENDING!!")
        break
