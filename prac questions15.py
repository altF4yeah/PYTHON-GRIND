'''
Q29. James is managing a list of inventory items in a warehouse. Each
item is recorded as a tuple, where the first element is the item ID and
the second element is a list of quantities available for that item.
James needs to filter out all quantities that are above a certain
threshold to find items that have a stock level above this limit.

Help James by writing a program to process these tuples, filter the
quantities from all the available items, and display the results.

Input format:
The first line of input consists of an integer N, representing the
number of tuples.
The next N lines each contain a tuple in the format (ID, [quantity1,
quantity2, ...]), where ID is an integer and the list contains integers.
The final line consists of an integer threshold, representing the
quantity threshold.

Output format:
The output should be a single line displaying the filtered quantities,
space-separated. Each quantity is strictly greater than the given
threshold.

Code constraints:
2 <= N, ID <= 6
1 <= tuple elements <= 50
1 <= threshold <= 20

Sample Input 1:
2
(1, [1, 2])
(2, [3, 4])
2
Sample Output 1: 3 4

Sample Input 2:
2
(1, [6, 7])
(2, [8])
6
Sample Output 2: 7 8
'''
n = int(input())

r = []
L = []

for i in range(n):
    x = input().replace("(","").replace(")","")
    x = x.replace("[","").replace("]","").replace(" ","")
    y = x.split(",")
    for j in y[1:]:
        if j:
            L.append(int(j))

m = int(input())

for i in L:
    if i>m:
        r.append(i)

print(*(r))


'''
Q30. Sophia, a language enthusiast, is working with a tuple of strings,
each representing a sentence. She wants to determine the sentence with
the highest number of unique words in the tuple.

Input format:
The first line contains an integer n, representing the number of
sentences.
The next n lines each contain a sentence (string). Each sentence
consists of alphabetic characters and spaces.

Output format:
The output prints the sentence that contains the highest number of
unique words. If there is a tie, print the first occurring sentence
among them.

Note: Case-sensitive comparison is not required (treat words as they are)

Sample Input 1:
3
This is a sample sentence
Another sentence with mo...   (rest of line cut off in source screenshot)
This is yet another sent...   (rest of line cut off in source screenshot)
Sample Output 1: This is a sample sentence

Sample Input 2:
2
Happy birthday!
Happy birthday Alex!
Sample Output 2: Happy birthday Alex!
'''
n = int(input())

count = -1
best = ""
for i in range(n):
    sent = input()
    words = sent.split()
    unique = len(set(words))

    if unique > count:
        count = unique
        best = sent
m = max(sent)
print(best)


'''
Q31. Isabella has a tuple of tuples, each containing a student's name
and age. She wants to find the oldest student's name.

Write a program that takes the number of students and their names and
ages as input, and outputs the name of the oldest student.

Input format:
The first line of input consists of an integer n, representing the
number of students.
The next 2n lines contain the student data:
The first line contains the student's name (a string that may include
alphabetic characters and spaces, with a maximum length of 20
characters).
The second line contains the student's age (an integer).

Output format:
The output displays the name of the oldest student in the following
format "The oldest student is [student_name]"
Here, [student_name] is replaced with the name of the student with the
highest age from the input.

Code constraints:
1 <= n <= 100, where n is the number of students
The length of each student's name will be at most 20 characters
Names may contain alphabetic characters and spaces
1 <= age <= 150

Sample Input 1:
2
John
30
Jane
28
Sample Output 1: The oldest student is John

Sample Input 2:
4
Michael
21
Emily
19
James
22
Sophia
20
Sample Output 2: The oldest student is James
'''
n = int(input())
L = []
R = []

for i in range(n):
    x = tuple(input().split())
    y = tuple(input().split())

    L.append(x)
    R.append(y)

m = max(R)
i = R.index(m)

print("The oldest student is", *(L[i]))