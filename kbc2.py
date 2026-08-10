# kbc using dictionary

print("-"*30)
print("")
print("-"*30)

print()
print("Rules")
print("1. you can press Q at any point to quit the game")
print("2. each questions contains 10000 points") 
print("3. Score a minimum of 70000 to win this game") 
print("4. the total number of questions is 10") 
print("5. if you manage to get a perfect score u should be happy") 
print("6. Type the Option (A/B/C/D) to enter your answer")
print()

kbc = {
"1. \n What is the capital of France? \n A. Berlin \n B. Madrid \n C. Paris \n D. Rome" : "C",

"2. \n Which planet is known as the Red Planet? \n A. Venus \n B. Mars \n C. Jupiter \n D. Saturn" : "B",

"3. \n How many continents are there on Earth? \n A. 5 \n B. 6 \n C. 7 \n D. 8" : "C",

"4. \n What is the largest ocean on Earth? \n A. Atlantic Ocean \n B. Indian Ocean \n C. Arctic Ocean \n D. Pacific Ocean" : "D",

"5. \n Which element does 'O' represent on the periodic table? \n A. Gold \n B. Oxygen \n C. Osmium \n D. Silver" : "B",

"6. \n Who painted the Mona Lisa? \n A. Vincent van Gogh \n B. Pablo Picasso \n C. Leonardo da Vinci \n D. Claude Monet" : "C",

"7. \n What is the hardest natural substance on Earth? \n A. Gold \n B. Iron \n C. Diamond \n D. Platinum" : "C",

"8. \n Which gas do plants absorb from the atmosphere for photosynthesis? \n A. Oxygen \n B. Carbon Dioxide \n C. Nitrogen \n D. Hydrogen" : "B",

"9. \n What is the smallest country in the world by land area? \n A. Monaco \n B. San Marino \n C. Vatican City \n D. Liechtenstein" : "C",

"10. \n How many sides does a hexagon have? \n A. 5 \n B. 6 \n C. 7 \n D. 8" : "B"
}


score = 0
for k in kbc:
    print(k)
    x = input("Enter Your option: ").upper().strip()

    if x==kbc[k]:
        print("gg")
        score += 1
    elif x == "Q":
        print()
        print("ok")
        print("You quit at score", score)
        break
    elif x != "Q":
        print("you lost")
        print("Your total score is", score)
        break
    else:
        print("Invalid Input")