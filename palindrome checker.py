# Palindrome checker


while True:
    pal = input("enter a string (type exit to quit) ").lower()
    if (pal == pal[::-1]):
        print("Yeah ur string is a palindrome")
        continue
    elif(pal == "quit"):
        print("ty for using this program")
        break
    else :
        print("nope it's not a palindrome")    
        continue
    