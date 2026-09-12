'''
============================================================
Question 15: Longest Word in a List
============================================================

Problem Statement:
Raj wants to write a program that takes a list of strings as
input and returns the longest word in the list. If there are
multiple words with the same length, the program should return
the first one encountered.

Help Raj in his task.

Input format:
The input consists of a single line of space-separated strings.

Output format:
The output prints a string representing the longest word in the
given list.

Code constraints:
The input string consists of printable ASCII characters.
1 <= Length of the string <= 100

Sample test cases:
Input 1:  cat dog elephant lion tiger giraf
Output 1: elephant

Input 2:  apple banana orange peach grape
Output 2: banana

Input 3:  ABC abc
Output 3: ABC

You are using Python
'''
x = input().split()
L = []
for i in x:
    L.append(len(i))

m = max(L)

a = L.index(m)

print(x[a])


'''
============================================================
Question 16: Total and Average Marks per Student
============================================================

Problem Statement:
Alice is a school admin collecting marks of students from 5
subjects. She wants to find the total and average marks for
each student.

You are asked to build a system that computes this for each
student.

Input format:
The First line of input consists of an Integer n representing
the number of students.
The Next n lines consist of 5 space-separated integers
representing the marks in 5 subjects.

Output format:
The output consists of, for each student, print Total: <total>
Average: <average> (average as float).

Code constraints:
1 <= Number of students <= 100
0 <= Marks <= 100

Sample test cases:
Input 1:
1
70 75 80 85 90
Output 1: Total: 400 Average: 80.0

Input 2:
2
55 60 65 70 75
40 45 50 55 60
Output 2:
Total: 325 Average: 65.0
Total: 250 Average: 50.0

Input 3:
3
99 98 97 96 95
50 51 52 53 54
0 0 100 0 100
Output 3:
Total: 485 Average: 97.0
Total: 260 Average: 52.0
Total: 200 Average: 40.0

You are using Python
'''
n = int(input())

for i in range(0, n):
    x = input().split()

    L  = []

    for i in x:
        L.append(int(i))

    total=sum(L)
    avg = total / 5

    print(f"Total: {total:.0f} Average: {avg:.1f}")


'''
============================================================
Question 17: Rotate Workers 2 Positions to the Right
============================================================

Problem Statement:
A factory has a team of workers arranged in a fixed order for
daily tasks. To improve efficiency and reduce monotony, the
supervisor decides to rotate the arrangement by 2 positions to
the right. This means the last two workers will be moved to the
front, and all others will shift two positions to the right.

You are tasked with implementing a system that takes the list of
workers and rotates it accordingly.

Input format:
The first line consists an integer n, representing the number of
workers.
The second line consists of an n space-separated strings, each
representing a worker's name.

Output format:
The output consists of a single line of space-separated worker
names after rotating them 2 positions to the right.

Code constraints:
3 <= n <= 15

Sample test cases:
Input 1:
3
Alice Bob Charlie
Output 1: Bob Charlie Alice

Input 2:
6
John Paul Ringo George Mick Keith
Output 2: Mick Keith John Paul Ringo George

Input 3:
9
A1 B2 C3 D4 E5 F6 G7 H8 I9
Output 3: H8 I9 A1 B2 C3 D4 E5 F6 G7

You are using Python
'''
n = int(input())

x = input().split()

y = x[-2:]

x.pop(-1)
x.pop(-1)

print(*(y+x))