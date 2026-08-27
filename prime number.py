# prime number checker

def check_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n <1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def next_prime(num):
    for i in range(num,2*num):
        if check_prime(i):
            print(f"The next prime number after {num} is {i}")
            return

def count_primes(ber):
    no = 0
    for i in range(1, ber):
        if check_prime(i):
            no += 1
    print(no)

def prime_for_range(range1, range2):
    for i in range(range1, range2+1):
        if check_prime(i):
            print(i)

def prime_factors(fact):
    for i in range(1,fact):
        if fact % i == 0 and check_prime(i):
            print(i)

def main():
    print()
    print("="*30)
    print("Prime Number".center(20))
    print("="*30)
    print()

    while True:
        print()
        print("1. Check if a number is prime or not")
        print("2. Find the next prime number after a number")
        print("3. Count total number of prime numbers below a number")
        print("4. Find all the prime numbers in a range")
        print("5. Find the prime factors of a number")
        print("6. Exit")
        print()

        choice = int(input("Enter your choice (1-6) "))

        if choice == 1:
            n = int(input("Enter the number: "))
            if check_prime(n):
                print("Yes, its a prime number")
            else:
                print("No, its not a prime number")

        elif choice == 2:
            num = int(input("Enter the number: "))
            next_prime(num)

        elif choice == 3:
            ber = int(input("Enter the number: "))
            count_primes(ber)

        elif choice == 4:
            range1 = int(input("Enter the lower limt of the range: "))
            range2 = int(input("Enter the upper limt of the range: "))
            prime_for_range(range1, range2)

        elif choice == 5:
            fact = int(input("Enter the number: "))
            prime_factors(fact)

        elif choice == 6:
            print("Stopping the program...")
            break

        else:
            print("Invalid Input")
            continue

if __name__ == "__main__":
    main()
    