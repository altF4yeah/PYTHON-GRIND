'''
============================================================
Question 3: Donations Above Median (Charity Event)
============================================================

Problem Statement:
Charlie is organizing a charity event and has recorded donation
amounts from attendees. He wants to calculate the percentage of
donations that are greater than the median donation amount.
Implement a solution to find the median after sorting the
recorded donations, count how many donations exceed this
median, and compute the percentage of such donations relative
to the total number of donations.

The median is the middle value in a sorted list if the number
of elements is odd, or the average of the two middle values if
the number of elements is even.

Help Charlie by implementing a solution using list comprehension
to solve this problem.

Input format:
The first line of input consists of an integer n, representing
the number of donations.
The second line contains n space-separated integers, each
representing a donation amount.

Output format:
The output displays a float rounded to two decimal places,
representing the percentage of donations that exceed the
median donation amount.

Code constraints:
5 <= n <= 20
25 <= list elements <= 100

Sample test cases:
Input 1:
5
32 42 45 95 67
Output 1: 40.00

Input 2:
8
76 87 82 72 71 98 75 81
Output 2: 50.00

You are using Python
'''
n = int(input())
x = input().split()
L = []
for i in x:
    L.append(int(i))

L.sort()
mid = len(L) // 2
if n % 2 != 0:
    m = L[mid]
else:
    m = (L[mid]+L[mid-1]) / 2

l = []
r = []
for i in L:
    if i > m:
        r.append(int(i))
    else:
        l.append(int(i))

p = (len(r)/len(L)) * 100
print(f"{p:.2f}")


'''
============================================================
Question 4: Check for Duplicate Elements (List Manipulation)
============================================================

Problem Statement:
Meenu is a diligent programmer who loves to work on tasks
related to list manipulation. Today, she's tasked with a
problem that involves determining whether a given list contains
unique elements or if there are duplicates present.

Meenu needs to develop a program that checks whether all
elements in a given list are unique or if there are duplicates
present.

Input format:
The input consists of a single line containing space-separated
integers, representing the elements of the list.

Output format:
The first line prints "List: " followed by the input list in
square brackets, separated by commas.
The second line contains the result message:
If all elements in the input list are unique, the message is
"All elements are unique".
If the input list contains duplicate elements, the message is
"List contains duplicate elements".

Code constraints:
1 <= number of elements in the list <= 100
1 <= each integer in the list <= 1000

Sample test cases:
Input 1:  1 2 3 4
Output 1:
List: [1, 2, 3, 4]
All elements are unique

Input 2:  6 7 8 5 3 2 1 6
Output 2:
List: [6, 7, 8, 5, 3, 2, 1, 6]
List contains duplicate elements

You are using Python
'''
x = input().split()

L = []

for i in x:
    L.append(int(i))

print("List:", L)

d = False
for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[i] == L[j]:
            d = True

if d:
    print("List contains duplicate elements")
else:
    print("All elements are unique")


'''
============================================================
Question 5: Inventory Tracker (Remove and Add Item IDs)
============================================================

Problem Statement:
Karan is building a basic inventory tracker. He first records a
list of item IDs as integers, then removes a specific item if it
exists in the list. After this, he adds more item IDs to the
list. The final list should reflect the removal and addition
accurately.

Help Karan complete this task using a Python program.

Note: If the item to be removed appears multiple times in the
list, only the first occurrence is removed.

Input format:
The first line of input contains a string of space-separated
integers representing the initial list of item IDs.
The second line contains an integer representing the item ID to
be removed from the list.
The third line contains another string of space-separated
integers representing item IDs to be added to the list.

Output format:
The first line of output prints "List1: " followed by the
original list of item IDs.
If the item was found and removed, the second line prints
"List after removal: " followed by the updated list.
If the item was not found, print "Element not found in the
list".
The last line prints "Final list: " followed by the final list
after the additions.

Sample test cases:
Input 1:
1 2 3 4 5
3
6 7 8
Output 1:
List1: [1, 2, 3, 4, 5]
List after removal: [1, 2, 4, 5, 6, 7, 8]
Final list: [1, 2, 4, 5, 6, 7, 8]

Input 2:
3 4 5 7 8 9 10
2
1 6
Output 2:
List1: [3, 4, 5, 7, 8, 9, 10]
Element not found in the list
Final list: [3, 4, 5, 7, 8, 9, 10, 1, 6]

You are using Python
'''
x1 = input().split()
n = int(input())
x2 = input().split()

L1 = []
L2 = []

for i in x1:
    L1.append(int(i))

for i in x2:
    L2.append(int(i))

print("List1:", L1)

if n in L1:
    L1.remove(n)
    print("List after removal:", L1)
else:
    print("Element not found in the list")

print("Final list:", L1+L2)