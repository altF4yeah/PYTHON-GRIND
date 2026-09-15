'''
Q26. Chris, an enthusiastic programmer, has a tuple containing integers.
He wants to create a new tuple that contains the even numbers from the
original tuple exclusively, without using any built-in functions or
libraries to filter them.

Input format:
The first line of input consists of space-separated integers, representing
the elements to be stored in a tuple. The line may contain any number of
elements, and each element is a non-negative integer.

Output format:
The first line of output prints "New Tuple with Even Integers:" in the
first line. The second line of output prints the resulting tuple
containing only even numbers in the next line.

Code constraints:
1 <= number of elements in the tuple <= 100
0 <= each integer <= 100000

Sample Input 1: 1 2 3 4 5 6 7 8
Sample Output 1:
New Tuple with Even Integers:
(2, 4, 6, 8)

Sample Input 2: 0 1 2 3 4 5
Sample Output 2:
New Tuple with Even Integers:
(0, 2, 4)
'''
x = input().split()

L = []
for i in x:
    L.append(int(i))

l = []
for i in L:
    if i % 2 == 0:
        l.append(i)

t = tuple(l)
print("New Tuple with Even Integers:")
print(t)


'''
Q27. Riley is analyzing DNA sequences and needs to determine which bases
match at the same positions in two given DNA sequences. Each DNA sequence
is represented as a tuple of integers, where each integer corresponds to
a DNA base.

Write a program that compares these two sequences and identifies the
bases that match at the same positions and prints it.

Input format:
The first line of input consists of an integer n, representing the size
of the first tuple.
The second line contains n space-separated integers, representing the
elements of the first DNA sequence tuple.
The third line of input consists of an integer m, representing the size
of the second tuple.
The fourth line contains m space-separated integers, representing the
elements of the second DNA sequence tuple.

Output format:
The output prints the matching bases as space-separated integers,
representing the values that match at the same positions in both
sequences.

Code constraints:
4 <= n <= 20
0 <= tuple element <= 255

Sample Input 1:
4
5 1 8 4
4
4 1 8 2
Sample Output 1: 1 8

Sample Input 2:
18
10 2 2 10 8 9 7 9 6 3 4
18
8 7 10 2 7 4 9 6 5 8 1 ...   (rest of line cut off in source screenshot)
Sample Output 2: 7
'''
n = int(input())
x = input().split()
m = int(input())
y = input().split()

a = []
b = []

for i in x:
    a.append(int(i))
for i in y:
    b.append(int(i))

z = []
for i in range(0, n):
    for j in range(0, m):
        if i == j and a[i] == b[j]:
            z.append(a[i])

t = tuple(z)
print(*(t))


'''
Q28. Emerson is managing a list of task IDs for a project. To streamline
task management, he needs to remove every nth task from the list. Help
Emerson by creating a program that reads a tuple of task IDs and an
integer n, then removes every nth task from the tuple and returns the
updated tuple.

If there are no n values in the tuple then display the original tuple
values without any change. The position of the task ID starts from 1.

Input format:
The first line of input consists of an integer size, representing the
number of elements in the tuple.
The second line contains size space-separated integers, representing
the task IDs in the tuple.
The third line contains an integer n, which specifies the position of
tasks to be removed.

Output format:
The output is a tuple of integers, where every nth task has been
removed from the original tuple.

Code constraints:
3 <= size <= 15
1 <= tuple elements <= 100
2 <= n <= 5

Sample Input 1:
6
1 2 3 4 5 6
3
Sample Output 1: (1, 2, 4, 5)

Sample Input 2:
4
5 10 15 20
5
Sample Output 2: (5, 10, 15, 20)
'''
n = int(input())
x = input().split()
m = int(input())

L = []
for i in x:
    L.append(int(i))

R = []
for i in range(len(L)):
    if (i+1)%m != 0:
        R.append(L[i])

print(tuple(R))