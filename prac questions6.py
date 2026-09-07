"""
Question:
You are working as a software developer at a math education company, and your team
is working on a program to help students understand odd and even numbers better.

Your task is to create a program that demonstrates the concept of using the
continue statement to skip even numbers while printing a list of odd numbers.

Input format:
The input consists of an integer n, representing the upper limit of the range.

Output format:
The output prints the odd numbers from 1 to n (inclusive), each on its own line, in
ascending order.

Refer to the sample output for the formatting specifications.

Code constraints:
1 <= n <= 100

Sample test cases:
Input 1: 10
Output 1: 1
          3
          5
          7
          9

Input 2: 5
Output 2: 1
          3
          5
"""

# Answer
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i)
'''
============================================================
Question 1: Transaction Rearrangement (Bank Analyst)
============================================================

Problem Statement:
Ravi is a bank analyst who is reviewing a sequence of daily
transactions. The transactions include both deposits (positive
values) and withdrawals (negative values).

He wants to rearrange the transaction list such that all
withdrawals are processed first, followed by deposits, while
maintaining the original order within each category.

Help Ravi implement a program to perform this rearrangement.

Input format:
The input consists of a single line containing space-separated
integers representing the transactions.

Output format:
The output prints the rearranged transactions such that all
negative values appear first, followed by positive values,
maintaining their original order. The values should be
separated by a single space.

Code constraints:
-100 <= transaction value <= 100

Sample test cases:
Input 1:  12 11 -13 -5 6 -7 5
Output 1: -13 -5 -7 12 11 6 5

Input 2:  -1 -2 -3 -4
Output 2: -1 -2 -3 -4
'''
 
x = input().split()
 
L = []
l = []
r = []
 
for i in x:
    L.append(int(i))
 
for i in L:
    if i < 0:
        l.append(i)
    else:
        r.append(i)
print(*(l+r))
 
'''
============================================================
Question 2: Harmful Comment Rearrangement (Content Moderator)
============================================================

Problem Statement:
Maya is a content moderator at a social media platform that
assigns sentiment scores to user comments. Instead of using a
fixed rule, the moderation system calculates the average
sentiment score of all comments.

Any comment with a score less than the average is considered
harmful and should be reviewed first.

Rearrange the list so that harmful comments appear first,
followed by safe comments, while maintaining their original
order.

Input format:
The input consists of a single line containing space-separated
integers representing sentiment scores.

Output format:
The output prints the rearranged sentiment scores such that
values less than the average appear first, followed by the
rest. The values should be separated by a single space.

Code constraints:
-100 <= sentiment score <= 100

Sample test cases:
Input 1:  5 -3 2 -8 0 7
Output 1: -3 -8 0 5 2 7

Input 2:  1 2 3 4 5
Output 2: 1 2 3 4 5
'''
# You are using Python
x = input().split()
 
L = []
 
for i in x:
    L.append(int(i))
 
avg = sum(L) / len(L)
 
l = []
r = []
 
for i in L:
    if i < avg:
        l.append(i)
    else:
        r.append(i)
 
print(*(l+r))
 