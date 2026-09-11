'''
============================================================
Question 12: Premium Deals Rearrangement (E-commerce Discounts)
============================================================

Problem Statement:
An e-commerce platform analyzes product discounts. It calculates
the maximum discount value, and considers any product with
discount at least half of the maximum discount as premium deals.

Rearrange the list so that premium deals appear first, followed
by regular deals, while maintaining order.

Input format:
A single line of space-separated integers representing discount
percentages.

Output format:
Print the rearranged discounts such that values greater than or
equal to half of the maximum discount appear first.

Code constraints:
0 <= discount <= 100

Sample test cases:
Input 1:  100 50 25
Output 1: 100 50 25

Input 2:  70 35 14
Output 2: 70 35 14

You are using Python
'''
x = input().split()

L = []
for i in x:
    L.append(int(i))

m = max(L)/2

l = []
r = []

for i in L:
    if i >= m:
        l.append(i)
    else:
        r.append(i)

print(*(l+r))


'''
============================================================
Question 13: GCD of Two Numbers (Without Predefined Functions)
============================================================

Problem Statement:
Pim, a mathematics enthusiast, is working on a project that
requires finding the greatest common divisor (GCD) of two
numbers. He wants to write a program to efficiently compute the
GCD without using any predefined functions.

Write a Python function gcd(a, b) that takes two integers, a and
b, as input and returns their greatest common divisor.

Input format:
The first line of input consists of an integer value a,
representing the first number.
The second line of input consists of an integer value b,
representing the second number.

Output format:
The output displays the greatest common divisor (GCD).

Code constraints:
5 <= a, b <= 500

Sample test cases:
Input 1:
10
5
Output 1: 5

Input 2:
500
50
Output 2: 50

You are using Python
'''
a = int(input())
b = int(input())

L = []
if a>b:
    for i in range(1, b+1):
        if a % i == 0 and b % i == 0:
            L.append(i)

print(L[-1])


'''
============================================================
Question 14: Pairs Summing to Target with an Even Number
============================================================

Problem Statement:
Wendy is organizing a math challenge where participants are
required to find pairs of numbers from a given list (N) that
add up to a specific target. However, Wendy has an additional
condition: she's interested only in pairs where one of the
numbers is even.

Write a program using list comprehension to help Wendy filter
out these pairs from the original list. The program should take
the original list of numbers and the target sum as inputs, and
then find and display all pairs that meet Wendy's criteria.

Input format:
The first line of input is a list of integers separated by a
space, which are used for calculation.
The second line of input is an integer value T, representing the
target value.

Output format:
For each unique pair (x, y) where x + y == target and at least
one of the numbers in the pair is even, print the pair in the
format: [x, y]
Each pair should be printed on a new line.
(The output pairs are printed in the order they are first
generated in the list comprehension.)

Code constraints:
1 <= list elements, T <= 100

Sample test cases:
Input 1:
2 5 7 8 6 5 4 7
10
Output 1:
[2, 8]
[8, 2]
[6, 4]
[4, 6]

Input 2:
5 7 11 9 6 4
11
Output 2:
[5, 6]
[7, 4]
[6, 5]
[4, 7]

You are using Python
'''
x = input().split()
T = int(input())

L = []

for i in x:
    L.append(int(i))

for i in range(0, len(x)):
    for j in range(0, len(x)):
        if L[i]+L[j] == T and L[i] != L[j] and (L[i] % 2 ==0 or L[j]%2 ==0):
            r = []
            r.append(L[i])
            r.append(L[j])
            print(r)