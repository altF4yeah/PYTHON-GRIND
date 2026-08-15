"""
Question:
John is passionate about maintaining a healthy lifestyle and has recently started
using a fitness tracker to monitor his body fat percentage. He inputs his height
and waist measurements into the tracker, and the program calculates and
categorizes his body fat percentage based on certain criteria.

Design a body fat percentage calculation is as follows.
BF% = 64 - ( 20 * (height/waist) )

The list below comes from the American Council and shows the average
percentages in specified groups.
1. "Essential fat" if body fat percentage is between 2% and 5% (inclusive).
2. "Athletes" if body fat percentage is between 6% and 13% (inclusive).
3. "Fitness" if the body fat percentage is between 14% and 17% (inclusive).
4. "Average" if body fat percentage is between 18% and 24% (inclusive).
5. "Obese" for above 25+

Input format:
The first line of input consists of a floating-point value representing the person's
height.
The second line of input consists of a floating-point value representing the
person's waist measurement.

Output format:
The first line output displays the calculated body fat percentage as a floating-
point number followed by "%". (rounded to two decimal places)
The second line output displays the descriptive category based on the body fat
percentage, such as "Essential fat," "Athletes," "Fitness," "Average," or "Obese."

Code constraints:
40.0 <= Waist <= 250.0

Sample test cases:
Input 1: 120.0 / 40.0   Output 1: 4.00% / Essential fat
Input 2: 120.0 / 60.0   Output 2: 24.00% / Average
Input 3: 120.0 / 45.8   Output 3: 11.60% / Athletes
Input 4: 120.3 / 79.5   Output 4: 33.74% / Obese
Input 5: 150.0 / 60.0   Output 5: 14.00% / Fitness
"""

# Answer
h = float(input())
w = float(input())

bf = 64 - (20*(h/w))

print(f"{bf:.2f}%")

if bf >= 2 and bf <= 5:
    print("Essential fat")
elif bf >= 6 and bf <= 13:
    print("Athletes")
elif bf >= 14 and bf <= 17:
    print("Fitness")
elif bf >= 18 and bf <= 24:
    print("Average")
else:
    print("Obese")

"""
Question:
Rekha is working in a company and receives a salary along with a performance-based
bonus. However, she is only eligible for the bonus if she has more than 5 years of
service. Based on her salary, years of service, bonus percentage, and the tax
percentage, you need to help her calculate her net salary. If Rekha's years of
service exceed 5, she will receive a bonus; otherwise, she won't. Help her to
implement the task.

Formula:
- net_bonus = (bonus_percentage / 100) * salary
- tax_amount = (tax_percentage / 100) * (salary + net_bonus)
- net_salary = salary + net_bonus - tax_amount

Input format:
The input consists of four lines:
The first line of input consists of a double salary, representing Rekha's salary.
The second line of input consists of an integer years_of_service, representing
Rekha's years of service in the company.
The third line of input consists of a double bonus_percentage, representing the
percentage of bonus she is eligible for.
The fourth line of input consists of a double tax_percentage, representing the tax
percentage to be deducted from her salary and bonus.

Output format:
The output displays the following format:
The first line of output prints: "You have earned a bonus of" net_bonus "units."
(if eligible for the bonus) or "Sorry, you are not eligible for a bonus."
The second line prints: "Tax Amount:" tax_amount "units"
The third line prints: "Net Salary:" net_salary "units"

Code constraints:
1.0 <= salary <= 10^5
1 <= year <= 100
1.0 <= bonus <= 10^5
1.0 <= tax percentage <= 10^5

Sample test cases:
Input 1: 50000.00 / 6 / 10.00 / 15.00
Output 1: You have earned a bonus of 5000.0 units.
          Tax Amount: 8250.0 units
          Net Salary: 46750.0 units

Input 2: 30000.00 / 3 / 8.00 / 12.00
Output 2: Sorry, you are not eligible for a bonus.
          Tax Amount: 3600.0 units
          Net Salary: 26400.0 units
"""

# Answer
a = float(input())
yos = int(input())
bp = float(input())
tp = float(input())

if yos > 5:
    nb = (bp/100)*a
    print(f"You have earned a bonus of {nb:.1f} units.")
else:
    nb = 0.0
    print(f"Sorry, you are not eligible for a bonus.")

ta = (tp/100) * (a+nb)
ns = (a+nb)-ta

print(f"Tax Amount: {ta:.1f} units")
print(f"Net Salary: {ns:.1f} units")

"""
Question:
As a junior developer working on a text analysis project, your task is to create a
program that displays the consonants in a sentence provided by the user, separated
by spaces.

You need to implement a program that takes a sentence as input and prints the
consonants while skipping vowels and non-alphabetic characters using only control
statements.

Input format:
The first line of input consists of a string input_sentence representing the
sentence.

Output format:
The first line of output prints space-separated consonants present in the sentence.

Code constraints:
1 <= length of the string <= 100
The string may include letters (both uppercase and lowercase), digits, punctuation,
and spaces.

Sample test cases:
Input 1: Hello World!
Output 1: H l l W r l d
"""

# Answer
inp = input()

vowels = "aeiouAEIOU"

result = ""

for x in inp:
    if ('a' <= x <= 'z') or ('A' <= x <= 'Z'):
        if x not in vowels:
            result = result + x + " "

print(result.strip())

"""
Question:
Aarav is fascinated by the concept of summing numbers separately based on their
properties. He plans to write a program that calculates the sum of even numbers
and odd numbers separately from 1 to a given positive integer.

Aarav wants to input an integer value to represent the upper limit of the range.
Help Aarav by developing a program that computes and displays the sum of even and
odd numbers separately.

Input format:
The input consists of a single integer N, where N is the upper limit of the range.

Output format:
The output consists of two lines:
The first line displays the sum of even numbers from 1 to N.
The second line displays the sum of odd numbers from 1 to N.

Refer to the sample output for the exact format.

Code constraints:
1 <= N <= 30

Sample test cases:
Input 1: 10
Output 1: Sum of even numbers from 1 to 10 is 30
          Sum of odd numbers from 1 to 10 is 25

Input 2: 5
Output 2: Sum of even numbers from 1 to 5 is 6
          Sum of odd numbers from 1 to 5 is 9
"""

# Answer
N = int(input())

x = 0
y = 0

for i in range(1, N+1):
    if i%2 == 0:
        x += i
    else:
        y += i

print(f"Sum of even numbers from 1 to {N} is {x}")
print(f"Sum of odd numbers from 1 to {N} is {y}")