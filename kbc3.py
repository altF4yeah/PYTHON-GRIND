# kbc with loops and stuff

import random

questions = [
    [
        "Which planet is known as the Red Planet?",
        "1.> Earth",
        "2.> Jupiter",
        "3.> Mars",
        "4.> Saturn",
        3,
    ],
    [
        "What is the capital of France?",
        "1.> Berlin",
        "2.> Madrid",
        "3.> Paris",
        "4.> Rome",
        3,
    ],
    [
        "Who wrote the play Romeo and Juliet?",
        "1.> Charles Dickens",
        "2.> Jane Austen",
        "3.> William Shakespeare",
        "4.> Mark Twain",
        3,
    ],
    [
        "What is the boiling point of water at sea level in degrees Celsius?",
        "1.> 50",
        "2.> 90",
        "3.> 100",
        "4.> 120",
        3,
    ],
    [
        "Which is the largest mammal in the world?",
        "1.> Elephant",
        "2.> Giraffe",
        "3.> Blue Whale",
        "4.> Rhinoceros",
        3,
    ],
    [
        "In which continent is the Sahara Desert located?",
        "1.> Asia",
        "2.> South America",
        "3.> Africa",
        "4.> Australia",
        3,
    ],
    [
        "Which gas do plants primarily absorb from the atmosphere for photosynthesis?",
        "1.> Oxygen",
        "2.> Nitrogen",
        "3.> Carbon Dioxide",
        "4.> Hydrogen",
        3,
    ],
    [
        "How many colors are there in a rainbow?",
        "1.> 5",
        "2.> 6",
        "3.> 7",
        "4.> 8",
        3,
    ],
    [
        "Who is known as the Father of the Indian Constitution?",
        "1.> Mahatma Gandhi",
        "2.> Jawaharlal Nehru",
        "3.> Dr. B.R. Ambedkar",
        "4.> Sardar Patel",
        3,
    ],
    [
        "Which instrument is used to measure atmospheric pressure?",
        "1.> Thermometer",
        "2.> Seismograph",
        "3.> Barometer",
        "4.> Hygrometer",
        3,
    ],
    [
        "What is the primary language spoken in Brazil?",
        "1.> Spanish",
        "2.> English",
        "3.> Portuguese",
        "4.> French",
        3,
    ],
    [
        "Which organ in the human body primarily filters waste from the blood?",
        "1.> Heart",
        "2.> Lungs",
        "3.> Kidneys",
        "4.> Stomach",
        3,
    ],
    [
        "Which of these is the smallest state in India by area?",
        "1.> Sikkim",
        "2.> Tripura",
        "3.> Goa",
        "4.> Mizoram",
        3,
    ],
    [
        "The Great Wall is a famous historical monument located in which country?",
        "1.> Japan",
        "2.> India",
        "3.> China",
        "4.> Russia",
        3,
    ],
    [
        "What is the hardest natural substance on Earth?",
        "1.> Gold",
        "2.> Iron",
        "3.> Diamond",
        "4.> Platinum",
        3,
    ],
]

hint = [
    ["It is named after the Roman god of war and has a rusty reddish color."],
    ["It is famous for the Eiffel Tower and is often called the City of Light."],
    ["He is famously known as the 'Bard of Avon.'"],
    ["It is the square of ten."],
    ["It is a marine animal and its tongue alone can weigh as much as an elephant."],
    ["It is the second-largest continent and is home to the Nile River."],
    ["It is the gas that humans and animals exhale when breathing out."],
    ["Think of the acronym VIBGYOR to remember them."],
    ["He was the chairman of the Drafting Committee for this historical document."],
    ["The name of this meteorological instrument begins with the letter 'B'."],
    ["It is the exact same language that is spoken in Portugal."],
    ["They are a pair of bean-shaped organs located near the middle of the back."],
    ["It is famously known for its beaches and was a Portuguese colony until 1961."],
    ["This country is known for its giant pandas and the Forbidden City."],
    ["It is a brilliant precious stone formed from pure carbon under extreme pressure."],
    ["It is a chemical element that accounts for about 78% of the air we breathe."]
]

flippedq = [
    
        "Which gas makes up the majority of Earth's atmosphere?",
        "1.> Oxygen",
        "2.> Carbon Dioxide",
        "3.> Nitrogen",
        "4.> Hydrogen",
        3,
]

ammount = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000,
]

bal = 0
options = [1, 2, 3, 4]
ll_1 = 0
ll_2 = 0
ll_3 = 0
ll_4 = 0

print()
print("<<<<<<<<<<<<<<<<<>KBC<>>>>>>>>>>>>>>>>>>")
print()
print("Points to note:")
print("1. press 0 to quit at anypoint of the game")
print("2. There are 3 checkpoints")
print("at rs 10k, 3.2L, 1Cr")
print("3. press 5 to see lifeline options list")
print()
print("Life-lines Summary:")
print("50-50, eliminates 2 wrong options")
print("Hint, shows a hint relevent to that question")
print("Double dip, turns on double dip mode where u can guess once")
print("Flip the question, change the current question")

def ll1():
    print("You have choosed 50-50 lifeline.")
    print("Deleting 2 wrong options...")
    print()
    print(question[1])
    print(question[3])

def ll2():
    print("You have choosed Hint lifeline")
    print("Generating a hint...")
    print()
    print(hint[i])

def ll3():
    print("You have choosed Double Dip lifeline")
    print("Double dip is on, Guess mode is on")
    print()
    dip = int(input("Enter Your guess option"))
    if dip == 3:
        print("Your guess is correct")
        return
    else:
        print("Your guess is wrong")

def ll4():
    print("You have choosed Flip the question lifeline")
    print("Flipping the question...")
    print()
    print(flippedq[0])
    print(flippedq[1], flippedq[2])
    print(flippedq[3], flippedq[4])
    print()
    print(hint[-1])


for i in range(0, len(questions)):

    print()
    print(f"Question for rs.{ammount[i]}")
    print()

    question = questions[i]
    print(question[0])
    print(question[1], question[2])
    print(question[3], question[4])

    while True:
        option = int(input("Enter your answer: (1-4) "))
        print()

        if option == 5:
            print("lifeline list selected:")
            print("1. 50-50" + ("(Already Used)" if ll_1 == 1 else ""))
            print("2. Hint" + ("(Already Used)" if ll_2 == 1 else ""))
            print("3. Double Dip" + ("(Already Used)" if ll_3 == 1 else ""))
            print("4. flip the question" + ("(Already Used)" if ll_4 == 1 else ""))
            print()

            llchoice = int(input("Enter your choice: (1-4) "))

            if llchoice == 1:
                if ll_1 == 1:
                    print("You've already used the 50-50 lifeline!")
                    print()
                else:
                    ll1()
                    ll_1 = 1
                continue

            elif llchoice == 2:
                if ll_2 == 1:
                    print("You've already used the Hint lifeline!")
                    print()
                else:
                    ll2()
                    ll_2 = 1
                continue

            elif llchoice == 3:
                if ll_3 == 1:
                    print("You've already used the Double Dip lifeline!")
                    print()
                else:
                    ll3()
                    ll_3 = 1
                continue

            elif llchoice == 4:
                if ll_4 == 1:
                    print("You've already used the Flip the question lifeline!")
                    print()
                else:
                    ll4()
                    ll_4 = 1
                continue

        break

    if option == question[5]:
        print(f"Correct answer!, you have won rs.{ammount[i]}")

        if i == 4:
            bal = 10000
        elif i == 9:
            bal = 320000
        elif i == 14:
            bal = 10000000

    elif option == 0:
        print("User Decided to quit the game")
        break

    else:
        print("Oops Wrong answer :(")
        break

print(f"\nYour final takeover amount is rs.{bal}")
