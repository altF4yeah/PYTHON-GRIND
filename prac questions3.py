"""
================================================================================
Problem Statement: Single File Programming Question
================================================================================
Joe is planning to invest some money in a savings account that offers compound 
interest. He wants to calculate the compound interest he will earn over a 
certain period.

Help him with a program that takes in the principal amount, the annual interest 
rate, and the period in years, and then computes the compound interest earned.

Explanation:
Compound Interest (CI) = A - P
A = P x (1+(r/100))^t
A = 6500.0 x (1 + (2.4/100))^5
A = 6500.0 x (1.024)^5
A = 6500.0 x 1.125899
A = 7318.349

CI = 7318.349 - 6500.0
CI = 818.35

--------------------------------------------------------------------------------
Input format:
The first line of input consists of a positive floating-point number representing 
the principal amount (principal) - the initial amount Joe invests.
The second line of input consists of a positive floating-point number representing 
the annual interest rate (rate) - the annual interest rate as a percentage.
The third line of input consists of a positive integer representing the period 
(time) - the number of years Joe plans to keep his money invested.

--------------------------------------------------------------------------------
Output format:
The output prints a single```python

================================================================================
Problem Summary: Compound Interest Calculator
================================================================================
Write a program to calculate the compound interest for an investment. The 
program should accept the initial principal balance, the annual interest rate, 
and the investment duration in years, and then output the total compound 
interest earned.

--------------------------------------------------------------------------------
Input format:
The first line of input consists of a positive floating-point number representing 
the principal amount.
The second line of input consists of a positive floating-point number representing 
the annual interest rate as a percentage.
The third line of input consists of a positive integer representing the period 
(time) in years.

--------------------------------------------------------------------------------
Output format:
The output prints a single floating-point number representing the compound interest 
earned over the specified period, rounded to two decimal places.

--------------------------------------------------------------------------------
Code constraints:
100.0 <= principal <= 100000.0
1.0 <= rate <= 10.0
1 <= time <= 10

--------------------------------------------------------------------------------
Sample test cases:

Input 1:
6500.0
2.4
5

Output 1:
818.35
================================================================================
"""


principal = float(input())
rate = float(input())
time = int(input())

A = principal * ((1+(rate/100))**time)
ci = A - principal
print(f"{ci:.2f}")


"""
================================================================================
Problem Summary: Bitwise Diagnostic Operations
================================================================================
Create a program to simulate hardware diagnostic checks on a register value 
using bitwise operations. The program should read an initial register value 
and two shift amounts. It must output the results of three operations: 
1. A left bit-shift (simulating power amplification).
2. A right bit-shift (simulating power reduction).
3. A bitwise NOT/complement operation (simulating fault detection).

--------------------------------------------------------------------------------
Input format:
The first line of input consists of an integer representing the current value 
stored in the register.
The second line of input consists of an integer representing the number of 
positions to shift left.
The third line of input consists of an integer representing the number of 
positions to shift right.

--------------------------------------------------------------------------------
Output format:
The first line of output prints "Left Shifted: " followed by an integer 
representing the result of the left shift operation.
The second line of output prints "Right Shifted: " followed by an integer 
representing the result of the right shift operation.
The third line of output prints "Complement: " followed by an integer 
representing the bitwise NOT result.

--------------------------------------------------------------------------------
Code constraints:
1 <= Register Value <= 255
1 <= Left Shift Amount <= 5
1 <= Right Shift Amount <= 5

--------------------------------------------------------------------------------
Sample test cases:

Input 1:
32
4
2

Output 1:
Left Shifted: 512
Right Shifted: 8
Complement: -33

Input 2:
48
2
3

Output 2:
Left Shifted: 192
Right Shifted: 6
Complement: -49
================================================================================
"""


a = int(input())
b = int(input())
c = int(input())

d = a << b
e = a >> c
f = ~a

print(f"Left Shifted: {d}")
print(f"Right Shifted: {e}")
print(f"Complement: {f}")

"""
================================================================================
Problem Statement: Single File Programming Question
================================================================================
Isabelle is a gemstone dealer who buys raw uncut gems and prices them for resale. 
Gemstones are priced by the carat, where 1 carat equals 0.2 grams. For each gem 
she acquires, she weighs it in grams, looks up the market price per carat, and 
then calculates the total number of carats and the total market value of the gem.

The formulas used are:
Carats = Raw Weight (grams) / 0.2
Total Value = Carats * Price per Carat

Both results must be rounded to 2 decimal places.
Isabelle needs a program that reads the raw weight in grams and the price per 
carat, then outputs the carat count and the total value.

--------------------------------------------------------------------------------
Input format:
The first line of input consists of a float value representing the raw weight 
of the gemstone in grams.
The second line of input consists of a float value representing the price per 
carat in currency units.

--------------------------------------------------------------------------------
Output format:
The first line of output prints "Carats: " followed by a float value representing 
the carat count rounded to 2 decimal places.
The second line of output prints "Total Value: " followed by a float value 
representing the total market value rounded to 2 decimal places.

Refer to the sample output for formatting specifications.

--------------------------------------------------------------------------------
Code constraints:
0.2 <= Raw Weight <= 10.0
100.0 <= Price per Carat <= 5000.0

--------------------------------------------------------------------------------
Sample test cases:

Input 1:
1.8
600.0

Output 1:
Carats: 9.00
Total Value: 5400.00

Input 2:
0.4
250.0

Output 2:
Carats: 2.00
Total Value: 500.00
================================================================================
"""

raw_w = float(input())
pp_carat = float(input())

Carats = raw_w / 0.2
total_value = Carats*pp_carat

print(f"Carats: {Carats:.2f}")
print(f"Total Value: {total_value:.2f}")

"""
================================================================================
Problem Statement: Single File Programming Question
================================================================================
Ryan is baking cupcakes for a party and has a recipe that requires 2.5 cups of 
flour, 1.0 cup of sugar, and 0.5 cups of butter to make 15 cupcakes. He wants to 
adjust the ingredient quantities based on the number of cupcakes he actually 
plans to bake.

Help him calculate and display the required amounts of flour, sugar, and butter 
with precision up to two decimal places.

--------------------------------------------------------------------------------
Input format:
The input consists of an integer n, representing the number of cupcakes.

--------------------------------------------------------------------------------
Output format:
The first line prints "Flour: X cups" where X represents the amount of flour 
required for n cookies [cupcakes], as a double value rounded to two decimal places.
The second line prints "Sugar: Y cups" where Y represents the amount of Sugar 
required for n, as a double value rounded to two decimal places.
The third line prints "Butter: Z cups" where Z represents the amount of butter 
required for n, as a double value rounded to two decimal places.

Refer to the sample output for formatting specifications.

--------------------------------------------------------------------------------
Code constraints:
1 <= n <= 100

--------------------------------------------------------------------------------
Sample test cases:

Input 1:
15
Output 1:
Flour: 2.50 cups
Sugar: 1.00 cups
Butter: 0.50 cups

Input 2:
1
Output 2:
Flour: 0.17 cups
Sugar: 0.07 cups
Butter: 0.03 cups

Input 3:
100
Output 3:
Flour: 16.67 cups
Sugar: 6.67 cups
Butter: 3.33 cups

Input 4:
13
Output 4:
Flour: 2.17 cups
Sugar: 0.87 cups
Butter: 0.43 cups
================================================================================
"""

n = int(input())

X = (2.5 / 15)*n
Y = (1 / 15)*n
Z = (0.5 / 15)*n

print(f"Flour: {X:.2f} cups")
print(f"Sugar: {Y:.2f} cups")
print(f"Butter: {Z:.2f} cups")