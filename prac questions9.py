'''
============================================================
Question 9: To-Do List Tracker (Add and Pop Tasks)
============================================================

Problem Statement:
Dhoni is organizing his tasks for the day and wants to create a
simple to-do list using Python. He plans to input his tasks one
by one and then remove them as he completes them.

He wants to create a program that allows him to add tasks, mark
them as completed by removing first and last elements from the
list, and visualize his progress.

Input format:
The first line of input consists of the number of elements in
the list N.
The next N lines of input consist of integers representing the
elements in the list.

Output format:
The first line displays "List after appending elements: "
followed by the list after appending elements to it.
The second line displays "List after popping last element: "
followed by the list after popping the last element.
The third line displays "Popped element: " followed by the
popped last element.
The fourth line displays "List after popping first element: "
followed by the list after popping the first element.
The fifth line displays "Popped element: " followed by the
popped first element.

Code constraints:
3 <= N <= 100

Sample test cases:
Input 1:
5
10
20
30
40
50
Output 1:
List after appending elements: [10, 20, 30, 40, 50]
List after popping last element: [10, 20, 30, 40]
Popped element: 50
List after popping first element: [20, 30, 40]
Popped element: 10

You are using Python
'''
n = int(input())

L = []

for i in range(0,n):
    x = int(input())
    L.append(x)

print("List after appending elements:", L)
print("List after popping last element:", L[:-1])
print("Popped element:", L[-1])
print("List after popping first element:", L[1:-1])
print("Popped element:", L[0])


'''
============================================================
Question 10: Index-Based List Transformation
============================================================

Problem Statement:
Ravi is learning Python and got an assignment to practice list
operations. He is required to take N integers as input, store
them in a list, and then transform the list based on specific
index-based rules.

1. Sort the list in ascending order.
2. Replace the element at index 0 with 0.
3. For elements at even indices (excluding index 0), replace
   them with their cube.
4. For elements at odd indices, replace them with their square.
5. Finally, display both the original sorted list and the
   transformed list.

Help Ravi write a program to accomplish this task.

Input format:
The first line of input contains an integer N, representing the
size of the list.
The next N lines contain one integer each, representing the
elements of the list.

Output format:
The first line of output prints "Original List: " followed by
the sorted list.
The second line of output prints "Replaced List: " followed by
the transformed list.

Code constraints:
1 <= N <= 100
The program follows 0-based indexing.

Sample test cases:
Input 1:
5
5
1
2
3
4
Output 1:
Original List: [1, 2, 3, 4, 5]
Replaced List: [0, 4, 27, 16, 125]

You are using Python
'''
n = int(input())
L = []
for i in range(0,n):
    x = int(input())
    L.append(x)

L.sort()

print("Original List:", L)

l = []
r = []

for i in range(0, len(L)):
    if i % 2 == 0:
        L[i] = L[i]**3
    else:
        L[i] = L[i]**2

L[0] = 0

print("Replaced List:", L)


'''
============================================================
Question 11: Abnormal Sensor Readings (IoT Monitoring)
============================================================

Problem Statement:
An IoT system monitors sensor readings. It first calculates the
average reading. Any reading whose absolute difference from the
average is greater than 10 is considered abnormal.

Rearrange the readings so that abnormal values appear first,
followed by normal readings, while maintaining order.

Note: If the absolute difference is exactly 10, the reading is
considered normal (not abnormal).

Input format:
A single line of space-separated integers representing sensor
readings.

Output format:
The output prints the rearranged readings such that abnormal
values appear first.

Code constraints:
0 <= reading <= 100

Sample test cases:
Input 1:  40 60 55 90 30
Output 1: 40 90 30 60 55

Input 2:  100 0 50
Output 2: 100 0 50

You are using Python
'''
x = input().split()

L = []
for i in x:
    L.append(int(i))

m = sum(L)/len(L)

l = []
r = []

for i in L:
    if i-m > 10 or m-i > 10:
        l.append(i)
    else:
        r.append(i)

print(*(l+r))