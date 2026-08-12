"""
================================================================================
Problem Statement: Single File Programming Question
================================================================================
Jack is working on a digital jigsaw puzzle where each piece has unique edge 
values. To solve the puzzle, he needs to match pieces by ensuring the sum of 
the edge values of two pieces, when the first edge value is shifted left by 
2-bit positions, equals a specified target value.

Jack wants to automate this process to quickly verify if two pieces fit 
together according to this rule.

--------------------------------------------------------------------------------
Input format:
The first line of input consists of an integer edge1, representing the edge value 
of the first piece.
The second line consists of an integer edge2, representing the edge value 
of the second piece.
The third line consists of an integer T, representing the target value for a match.

--------------------------------------------------------------------------------
Output format:
The first line ofHere are the scripts formatted with code header blocks summarizing each problem, along with suggested filenames for GitHub.

---



================================================================================
Problem Summary: Digital Jigsaw Piece Matcher
================================================================================
Jack is solving a digital jigsaw puzzle where pieces are matched based on 
edge values. To check if two pieces fit:
1. Shift the edge value of the first piece (edge1) left by 2 bit positions.
2. Add this value to the edge value of the second piece (edge2).
3. Check if the resulting sum equals a target value (T).

Output Specifications:
- Line 1: Print the value of edge1 after a 2-bit left shift.
- Line 2: Print "Match result: " followed by True or False depending on 
  whether the sum equals T.

Constraints:
- 1 <= edge1, edge2 <= 600
- 1 <= T <= 1000

Sample 1:
Input:
5
7
27
Output:
20
Match result: True

Sample 2:
Input:
15
6
45
Output:
60
Match result: False
================================================================================
"""

edge1 = int(input())
edge2 = int(input())
T = int(input())

shift_edge1 = edge1 << 2
match = (shift_edge1 + edge2) == T

print(shift_edge1)
print(f"Match result: {match}")

"""
================================================================================
Problem Statement: Single File Programming Question
================================================================================
Liam and his friends are sharing the cost of a group purchase. The total cost 
of the purchase is subject to a 10% discount. One of the friends receives a 35% 
bonus, which means they will pay a larger portion of the discounted cost. The 
remaining cost is then divided equally among the other friends.

Write a program to:
- Calculate the total cost after applying a 10% discount.
- Determine the amount paid by the friend who receives a 35% bonus.
- Calculate the amount each of the other friends will pay.

--------------------------------------------------------------------------------
Input format:
The first line of input consists of a float value f, representing the total cost.
The second line contains an integer value n, representing the total number of friends.

--------------------------------------------------------------------------------
Output format:
The first line of output displays "Cost after a 10% discount: " followed by the 
discounted cost of the ticket package as a float value formatted to two decimal places.
The second line displays "Friend with a 35% bonus pays: " followed by the bonus 
amount, formatted to two decimal places.
The third line displays "Remaining cost per friend: " followed by the individual 
share, formatted to two decimal places.

--------------------------------------------------------------------------------
Code constraints:
5000.0 <= f <= 30000.00
2 <= n <= 10

--------------------------------------------------------------------------------
Sample test cases:

Sample 1:
Input:
10000.0
5

Output:
Cost after a 10% discount: 9000.00
Friend with a 35% bonus pays: 3150.00
Remaining cost per friend: 1462.50

Sample 2:
Input:
20000.0
4

Output:
Cost after a 10% discount: 18000.00
Friend with a 35% bonus pays: 6300.00
Remaining cost per friend: 3900.00
================================================================================
"""

f = float(input())
n = int(input())

dp = f - (0.1 * f)
bfp = 0.35 * dp
rc = dp - bfp
rcpf = rc / (n-1)

print(f"Cost after a 10% discount: {dp:.2f}")
print(f"Friend with a 35% bonus pays: {bfp:.2f}")
print(f"Remaining cost per friend: {rcpf:.2f}")

"""
================================================================================
Problem Summary: Mathematical Claim Validation (Corrected)
================================================================================
Mandy is debating with her friend Rachel about a mathematical claim: for any 
positive integer n, the ratio of the sum of n and its triple to the integer 
itself is always 4.

Write a program to validate this using logical operators.

--------------------------------------------------------------------------------
Input format:
The input consists of a positive integer n.

--------------------------------------------------------------------------------
Output format:
Line 1: "Sum: " followed by the calculated sum.
Line 2: "Rachel's statement is: " followed by a Boolean value indicating whether 
the statement is correct.

--------------------------------------------------------------------------------
Code constraints:
1 <= n <= 1000

--------------------------------------------------------------------------------
Sample test cases:

Input 1:
12
Output 1:
Sum: 48
Rachel's statement is: True
================================================================================
"""

n = int(input())

total_sum = n + (3 * n)

is_correct = (total_sum / n) == 4

print(f"Sum: {total_sum}")
print(f"Rachel's statement is: {is_correct}")

"""
================================================================================
Problem Summary: Number Datatypes
================================================================================
You are building a program that requires the user to input various 'number datatypes'. 
You need to ensure that the program can correctly handle inputs of different data types.

Write a Python program that gets inputs from the user for all the number datatypes 
and prints out the inputs for each data type.

--------------------------------------------------------------------------------
Input format:
The first line of input consists of an integer as A.
The second line of input consists of a floating point number as B.
The third line of input consists of a complex number as C.

--------------------------------------------------------------------------------
Output format:
The first line should display the input value for the integer data type with 
the prefix "Integer: ".
The second line should display the input value for the floating-point number 
data type with the prefix "Floating-point number: ".
The third line should display the input value for the complex number data type 
with the prefix "Complex number: ".

--------------------------------------------------------------------------------
Code constraints:
A should be an integer.
B should be a floating point number.
C should be a complex number in the format: a+bj or a-bj.

--------------------------------------------------------------------------------
Sample test cases:

Input 1:
-895
15.65
35-6j

Output 1:
Integer: -895
Floating-point number: 15.65
Complex number: (35-6j)
================================================================================
"""

# You are using Python
A = int(input())
B = float(input())
C = complex(input())

print(f"Integer: {A}")
print(f"Floating-point number: {B}")
print(f"Complex number: {C}")