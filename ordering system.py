# Ordering System

print("^"*40)
print("Welcome to My hotel!!!")
print("^"*40)

print()
print("MENU:")

print("1. Pizza - 200rs")
print("2. Burger - 100rs")
print("3. Pasta - 50rs")
print("4. Coffee - 70rs")
print("5. Ice-cream - 150rs")

order = {
    "pizza":200,
    "burger":100,
    "pasta":50,
    "coffee":70,
    "ice-cream":150
}

bill = 0
receipt = []

while True:
    print()
    inp = input("What items you wanna select for your order?? (enter 'order' to get bill) ").lower().strip()

    if inp == "pizza" or inp == "1":
        print("+1 pizza added in your cart")
        bill += 200
        receipt.append("pizza")

    elif inp == "burger" or inp == "2":
        print("+1 burger added in your cart")
        bill += 100
        receipt.append("Burger")

    elif inp == "pasta" or inp == "3":
        print("+1 pasta added in your cart")
        bill += 50
        receipt.append("pasta")

    elif inp == "coffee" or inp == "4":
        print("+1 coffee added in your cart")
        bill += 70
        receipt.append("coffee")

    elif inp == "ice-cream" or inp == "5":
        print("+1 ice-cream added in your cart")
        bill += 150
        receipt.append("ice-cream")

    elif inp == "order":
        print()
        print("Thank You for ordering")
        print("Here is your bill,", bill)
        for x in receipt:
            print(x)

    else:
        print("Wtf is that item, pls enter a valid item from the menu")

    