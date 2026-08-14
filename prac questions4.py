"""
Question:
Rekha is preparing for a coding interview, and one of the tasks assigned to her is
to write a program that checks whether a given number is prime. If the number is
not prime, the program should print "Not prime". If the number is prime, it should
calculate and display the cube root of that number, rounded to 1 decimal place.

Input format:
The input consists of an integer num, representing the number to be checked.

Output format:
If the number is not prime, print "Not prime".
If the number is prime, print the cube root of the number rounded to 1 decimal place.

Code constraints:
2 <= num <= 1500

Sample test cases:
Input 1: 5      Output 1: 1.7
Input 2: 9      Output 2: Not prime
"""

# Answer
num = int(input())
if num < 2:
    print("Not prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print(round(num**(1/3), 1))


"""
Question:
Sita, an intern at a software company, has been tasked with writing a program to
determine the quarter of the year based on the month number. She was given
the following task:

- If the month is between 1 and 3, it should return "Q1".
- If the month is between 4 and 6, it should return "Q2".
- If the month is between 7 and 9, it should return "Q3".
- If the month is between 10 and 12, it should return "Q4".
- If the month is not between 1 and 12, it should return "Invalid month".

Sita has written the code, but there seems to be a logical flaw that needs to be
fixed. Your task is to debug and implement a solution that correctly assigns a
quarter to the month number.

Input format:
The input consists of an integer month, representing the month of the year (1 to 12).

Output format:
The output should print one of the following: "Q1" or "Q2" or "Q3", or "Q4" if the
month is between 1 to 12.
"Invalid month" if the month is outside the range of 1 to 12.

Code constraints:
1 <= month <= 15

Sample test cases:
Input 1: 2    Output 1: Q1
Input 2: 5    Output 2: Q2
Input 3: 8    Output 3: Q3
Input 4: 11   Output 4: Q4
Input 5: 13   Output 5: Invalid month
"""

# Answer
month = int(input())
if month == 1 or month == 2 or month == 3:
    print("Q1")
elif month == 4 or month == 5 or month == 6:
    print("Q2")
elif month == 7 or month == 8 or month == 9:
    print("Q3")
elif month == 10 or month == 11 or month == 12:
    print("Q4")
else:
    print("Invalid month")


"""
Question:
Arjun is a software developer who is working on a project to categorize people
based on their age group. He is facing an issue with the code he has written to
classify people into different age categories. The current code has a bug that
needs to be fixed in order to correctly categorize the age groups.

Your task is to debug the code and implement a solution that properly
categorizes people into the following groups:

- "Child" if age <= 12
- "Teenager" if age <= 19
- "Adult" if age <= 64
- "Senior" if age > 64

You need to fix the error in the code provided and ensure the program outputs
the correct category for a given age.

Input format:
The input consists of an integer age, representing the age of the person.

Output format:
The output prints the category of the person: either "Child", "Teenager", "Adult", or
"Senior".

Code constraints:
1 <= age <= 150

Sample test cases:
Input 1: 5     Output 1: Child
Input 2: 18    Output 2: Teenager
Input 3: 22    Output 3: Adult
Input 4: 65    Output 4: Senior
"""

# Answer
age = int(input())
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

"""
Question:
Harold analyzes stock investment options and bases his decision on the risk
factor and projected annual return of the investment.

1. If the risk factor of an investment is below 3 (on a scale of 1-10), and if the
   projected annual return is over 8%, Harold will invest 10,000 dollars.
2. If the risk factor is below 3 but the annual return does not exceed 8%, he will
   invest 5,000 dollars.
3. If the risk factor is between 3 and 7, and the projected return is over 10%, he
   invests 7,000 dollars.
4. If the above conditions are not met he will not invest.

Help Harold in analyzing the stock.

Input format:
The first line of input consists of a float F, representing the risk factor.
The second line consists of a float P, representing the projected annual return
percentage.

Output format:
The output displays "Investment amount: " followed by an integer representing the
amount Harold decides to invest.

Code constraints:
1.0 <= F <= 10.0
5.0 <= P <= 15.0

Sample test cases:
Input 1: 5.7 / 12.7    Output 1: Investment amount: 7000
Input 2: 2.3 / 7.2     Output 2: Investment amount: 5000
Input 3: 6.7 / 6.6     Output 3: Investment amount: 0
Input 4: 1.3 / 10.1    Output 4: Investment amount: 10000
"""

# Answer
F = float(input())
P = float(input())

if F < 3 and P > 8:
    ia = 10000
elif F < 3 and P < 8:
    ia = 5000
elif F > 3 and F < 7 and P > 10:
    ia = 7000
else:
    ia = 0

print("Investment amount:", ia)