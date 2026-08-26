import webbrowser
import time

def urlyt():
    yt = input("Enter the profile name: ")
    url_yt = f"https://www.youtube.com/@{yt}"

    for i in range (3, 0, -1):
        print(f"Opening Youtube in {i} \n")
        time.sleep(1)
    print("Opening Youtube...")
    webbrowser.open(url_yt)

def urlig():
    ig = input("Enter the profile name: ")
    url_ig = f"https://www.instagram.com/{ig}"

    for i in range (3, 0, -1):
        print(f"Opening Instagram in {i} \n")
        time.sleep(1)
    print("Opening Instagram...")
    webbrowser.open(url_ig)

def urlgh():
    gh = input("Enter the profile name: ")
    url_gh = f"https://github.com/{gh}"

    for i in range (3, 0, -1):
        print(f"Opening GitHub in {i} \n")
        time.sleep(1)
    print("Opening Github...")
    webbrowser.open(url_gh)

def main():
    print()
    print("-------------------------Profile-URL-Opener-------------------------")
    print()

    while True:
        print("1. Youtube")
        print("2. Instagram")
        print("3. GitHub")

        choice = input("Enter your choice (1-3) (Q to stop) ").lower()

        if choice in ["1", "yt","youtube"] :
            urlyt()

        elif choice in ["2", "ig", "instagram"]:
            urlig()

        elif choice in ["3", "gh", "github"]:
            urlgh()

        elif choice in ["0", "q", "quit"]:
            for i in range (3, 0, -1):
                print(f"Closing the program in {i} \n")
                time.sleep(1)
            print("CLosing...")
            break

        else:
            print("Invalid Input, Try again")
            continue

main()