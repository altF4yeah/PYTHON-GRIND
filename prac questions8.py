'''
============================================================
Question 6: Fibonacci AQI Readings (Air Quality Monitoring)
============================================================

Problem Statement:
An environmental monitoring system collects Air Quality Index
(AQI) readings. The system identifies "natural pattern" readings
that belong to the Fibonacci sequence.

Stations with Fibonacci AQI values are considered "naturally
balanced" and should be prioritized for reporting.

Rearrange the AQI readings so that all Fibonacci numbers appear
first, followed by non-Fibonacci numbers, while maintaining the
original order within each category.

Note: The Fibonacci sequence considered: 0, 1, 1, 2, 3, 5, 8,
13, 21, 34, 55, 89, 144, 233, 377. (Since AQI <= 500)

Input format:
The input contains a single line of space-separated integers
representing AQI readings.

Output format:
The output should be printed as a single line of space-separated
numbers, where all Fibonacci AQI values appear first followed by
all non-Fibonacci AQI values, while preserving the original
order within each group.

Code constraints:
0 <= AQI <= 500

Sample test cases:
Input 1:  0 5 8 13 20 34 50 89
Output 1: 0 5 8 13 34 89 20 50

Input 2:  45 185 95 175 135
Output 2: 45 185 95 175 135

You are using Python
'''
x = input().split()

L = []

for i in x:
    L.append(int(i))

f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

l = []
r = []

for i in L:
    if i in f and L:
        l.append(i)
    else:
        r.append(i)

print(*(l+r))


'''
============================================================
Question 7: Arrange Negatives Before Positives
============================================================

Problem Statement:
Given a list of positive and negative numbers, arrange them such
that all negative integers appear before all the positive
integers in the array. The order of appearance should be
maintained.

Example:
Input:  [12, 11, -13, -5, 6, -7, 5, -3, -6]
Output: List = [-13, -5, -7, -3, -6, 12, 11, 6, 5]

Explanation:
The output is the arranged list where all the negative integers
appear before the positive integers while maintaining the
original order of appearance.

Input format:
The input consists of a single line containing a list of
integers enclosed in square brackets separated by commas.

Output format:
The output displays "List =" followed by an arranged list of
integers as required, separated by commas and enclosed in
square brackets.

Code constraints:
-10^3 <= array elements <= 10^3

Sample test cases:
Input 1:  [12, 11, -13, -5, 6, -7, 5, -3, -6]
Output 1: List = [-13, -5, -7, -3, -6, 12, 11, 6, 5]

Input 2:  [1, 4, -7, 5, 0, -6]
Output 2: List = [-7, -6, 1, 4, 5, 0]

You are using Python
'''
x = input().replace("[", "").replace("]","")

x = x.split(",")

L = []
for i in x:
    L.append(int(i))

l = []
r = []

for i in L:
    if i < 0:
        l.append(i)
    else:
        r.append(i)

print("List = ",l+r)


'''
============================================================
Question 8: Largest Divisor from the List
============================================================

Problem Statement:
Nora is building a simple data-analysis tool that works with
lists of integers. Given a list of N integers, she needs to find
the largest divisor for each element in the list, other than the
number itself.

The divisor should be from the list. If there is no such
divisor, print -1.

Help Nora implement this logic.

Input format:
The first line contains an integer n, representing the number of
elements in the list.
The second line contains n integers separated by a comma and a
space, representing the elements of the list.

Output format:
The output should print a list of n integers, where the ith
integer represents the largest divisor of the ith element in the
input list (excluding the element itself) separated by comma as
a list.

Code constraints:
1 <= n <= 15
1 <= elements of the list <= 50

Sample test cases:
Input 1:
6
5, 16, 4, 8, 9, 10
Output 1: [-1, 8, -1, 4, -1, 5]

Input 2:
7
15, 17, 10, 5, 30, 6, 18
Output 2: [5, -1, 5, -1, 15, -1, 6]

You are using Python
'''
n = int(input())

x = input().replace(",", "").split()

L = []

for i in x:
    L.append(int(i))

l = []

for i in range(n):
    e = -1
    for j in range(n):
        if L[i] % L[j] == 0 and i!=j:
            if L[j] > e:
                e = L[j]
    l.append(e)

print(l)