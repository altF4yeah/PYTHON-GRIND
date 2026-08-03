# KBC

print("KBC".center(50))
print("Rules")
print("1. you can press Q at any point to quit the game")
print("2. each questions contains 10000 points") 
print("3. Score a minimum of 70000 to win this game") 
print("4. the total number of questions is 10") 
print("5. if you manage to get a perfect score u should be happy") 
print("6. Type the Option (A/B/C/D) to enter your answer")

q1 = "Q1. Which of these gases was first discovered in the Sun's atmosphere before it was found on Earth? \n A. Oxygen \n B. nitrogen \n C. Helium \n D. Argon"

q2 = "Q2. In the Indian epic Ramayana, who was the father of King Ravana? \n A. Sage Agastya \n B. Sage Vishrava \n C. Sage Bharadwaj \n D. Sage Pulastya"

q3 = "Q3. Which Indian state was the first to implement the Panchayati Raj system in 1959? \n A. Gujarat \n B. Maharashtra \n C. Rajasthan \n D. Karnataka"

q4 = "Q4. What is the chemical/scientific name of Vitamin B12? \n A. Pyridoxine \n B. Thiamine \n C. Cyanocobalamin \n D. Riboflavin"

q5 = "Q5. In 1905, which British Viceroy was responsible for the Partition of Bengal? \n A. Lord Curzon \n B. Lord Dalhousie \n C. Lord Canning \n D. Lord Mountbatten"

q6 = "Q6. Which mountain pass connects the Indian state of Sikkim with the Tibet Autonomous Region of China? \n A. Rohtang Pass \n B. Nathu La \n C. Shipki La \n D. Zoji La"

q7 = "Q7. Who was the first Indian to be elected as a member of the British House of Commons? \n A. Gopal Krishna Gokhale \n B. Dadabhai Naoroji \n C. Womesh Chandra Bonnerjee \n D. Surendranath Banerjee"

q8 = "Q8. The historical Sanskrit play 'Mudrarakshasa', which narrates the rise of Chandragupta Maurya, was written by whom? \n A. Kalidasa \n B. Banabhatta \n C. Vishakhadatta \n D. Bhasa"

q9 = "Q9. Which layer of Earth's atmosphere contains the highest concentration of Ozone? \n A. Troposphere \n B. Stratosphere \n C. Mesosphere \n D. Thermosphere"

q10 = "Q10. Who was the first Indian woman to win an individual medal at the Olympic Games? \n A. P. T. Usha \n B. Karnam Malleswari \n C. Saina Nehwal \n D. Mary Kom"

score = 0
while True:
    st = input(">>type start to initiate the game: ").upper()

    if (st == "START"):
        print(" >>starting the program")

        print(q1)
        ans = input("Choose Your answer ").upper()
        if (ans == "C"):
            print("Correct option!!")
            score += 10000

            print("your current score is ", score)
            print(q2)
            ans = input("Choose Your answer ").upper()

            if (ans == "B"):
                print("Correct option!!") 
                score += 10000

                print("your current score is ", score)
                print(q3)
                ans = input("Choose Your answer ").upper()

                if (ans == "C"):
                    print("Correct option!!") 
                    score += 10000

                    print("your current score is ", score)
                    print(q4)
                    ans = input("Choose Your answer ").upper()

                    if (ans == "C"):
                        print("Correct option!!") 
                        score += 10000

                        print("your current score is ", score)
                        print(q5)
                        ans = input("Choose Your answer ").upper()

                        if (ans == "A"):
                            print("Correct option!!") 
                            score += 10000

                            print("your current score is ", score)
                            print(q6)
                            ans = input("Choose Your answer ").upper()

                            if (ans == "B"):
                                print("Correct option!!") 
                                score += 10000

                                print("your current score is ", score)
                                print(q7)
                                ans = input("Choose Your answer ").upper()

                                if (ans == "B"):
                                    print("Correct option!!") 
                                    score += 10000

                                    print("your current score is ", score)
                                    print(q8)
                                    ans = input("Choose Your answer ").upper()

                                    if (ans == "C"):
                                        print("Correct option!!") 
                                        score += 10000

                                        print("your current score is ", score)
                                        print(q9)
                                        ans = input("Choose Your answer ").upper()

                                        if (ans == "B"):
                                            print("Correct option!!") 
                                            score += 10000

                                            print("your current score is ", score)
                                            print(q10)
                                            ans = input("Choose Your answer ").upper()

                                            if (ans == "B"):
                                                print("COrrect option!!")
                                                score += 10000

                                                print("GGs!!, you got the perfect score!", score)
                                            elif (ans == "Q"):
                                                print("Thanks for playing, Your total score is", score)
                                                if (score >= 70000):
                                                    print("as your score is above 70k, YOU WONNNNNN")
                                                else:
                                                    print("your score is not up to the mark so YOU LOSTTTT")
                                            else:
                                                print("OOPS! this is the wrong answer :(")
                                                print("your total score is", score)
                                                break 
                                            break       
                                        elif (ans == "Q"):
                                            print("Thanks for playing, Your total score is", score)
                                            if (score >= 70000):
                                                print("as your score is above 70k, YOU WONNNNNN")
                                            else:
                                                print("your score is not up to the mark so YOU LOSTTTT")
                                        else:
                                            print("OOPS! this is the wrong answer :(")
                                            print("your total score is", score)
                                            break 
                                        break
                                    elif (ans == "Q"):
                                        print("Thanks for playing, Your total score is", score)
                                        if (score >= 70000):
                                            print("as your score is above 70k, YOU WONNNNNN")
                                        else:
                                            print("your score is not up to the mark so YOU LOSTTTT")            
                                    else:
                                        print("OOPS! this is the wrong answer :(")
                                        print("your total score is", score)
                                        break 
                                    break
                                elif (ans == "Q"):
                                    print("Thanks for playing, Your total score is", score)
                                    if (score >= 70000):
                                        print("as your score is above 70k, YOU WONNNNNN")
                                    else:
                                        print("your score is not up to the mark so YOU LOSTTTT")            
                                else:
                                    print("OOPS! this is the wrong answer :(")
                                    print("your total score is", score)
                                    break 
                                break
                            elif (ans == "Q"):
                                print("Thanks for playing, Your total score is", score)
                                if (score >= 70000):
                                    print("as your score is above 70k, YOU WONNNNNN")
                                else:
                                    print("your score is not up to the mark so YOU LOSTTTT")
                            else:
                                print("OOPS! this is the wrong answer :(")
                                print("your total score is", score)
                                break 
                            break
                        elif (ans == "Q"):
                            print("Thanks for playing, Your total score is", score)
                            if (score >= 70000):
                                print("as your score is above 70k, YOU WONNNNNN")
                            else:
                                print("your score is not up to the mark so YOU LOSTTTT")            
                        else:
                            print("OOPS! this is the wrong answer :(")
                            print("your total score is", score)
                            break 
                        break 
                    elif (ans == "Q"):
                        print("Thanks for playing, Your total score is", score)
                        if (score >= 70000):
                            print("as your score is above 70k, YOU WONNNNNN")
                        else:
                            print("your score is not up to the mark so YOU LOSTTTT")      
                    else:
                        print("OOPS! this is the wrong answer :(")
                        print("your total score is", score)
                        break 
                    break
                elif (ans == "Q"):
                    print("Thanks for playing, Your total score is", score)
                    if (score >= 70000):
                        print("as your score is above 70k, YOU WONNNNNN")
                    else:
                        print("your score is not up to the mark so YOU LOSTTTT")
                else:
                    print("OOPS! this is the wrong answer :(")
                    print("your total score is", score)
                    break 
                break
            elif (ans == "Q"):
                print("Thanks for playing, Your total score is", score)
                if (score >= 70000):
                    print("as your score is above 70k, YOU WONNNNNN")
                else:
                    print("your score is not up to the mark so YOU LOSTTTT")              
            else:
                print("OOPS! this is the wrong answer :(")
                print("your total score is", score)
                break 
            break
        elif (ans == "Q"):
            print("Thanks for playing, Your total score is", score)
            if (score >= 70000):
                print("as your score is above 70k, YOU WONNNNNN")
            else:
                print("your score is not up to the mark so YOU LOSTTTT")
        else:
            print("OOPS! this is the wrong answer :(")
            print("your total score is", score)
            break
        
    elif (st == "Q" or st == "QUIT"):
        print("game stopped.")
        break
    else:
        print("Choose either Start or Quit")
        continue

# Answers: C/B/C/C/A/B/B/C/B/B