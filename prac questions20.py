# =====================================================================
# QUESTION 3
# =====================================================================
#
# Single File Programming Question
#
# Problem Statement
#
# Riya owns a store and keeps track of item prices from two different
# suppliers using two separate dictionaries. He wants to compare these
# prices to identify any differences. Your task is to write a program
# that calculates the absolute difference in prices for items that are
# present in both dictionaries. For items that are unique to one
# dictionary (i.e., not present in the other), include them in the
# output dictionary with their original prices.
#
# Help Riya implement the above task using a dictionary.
#
# Input format:
# The first line of the input consists of an integer n1, representing
# the number of items in the first dictionary.
# The next n1x2 lines contain two integers:
# The first line contains the item (key), and
# The second line contains the price (value).
# The following line consists of an integer n2, representing the number
# of items in the second dictionary.
# The next n2x2 lines contain two integers:
# The first line contains the item (key), and
# The second line contains the price (value).
#
# Output format:
# The output prints "{key: value, ...}" followed by a dictionary where:
# If a key exists in both dictionaries, the corresponding value is the
# absolute difference between the values from dict1 and dict2.
# If a key exists only in one dictionary, its original value is retained
# in the order it appears.
# The final result is represented as a dictionary of integers mapped to
# integers.

# You are using Python

d1 = {}
d2 = {}

n = int(input())

for i in range(n):
    key = int(input())
    value = int(input())
    d1[key] = value

m = int(input())

for i in range(m):
    key = int(input())
    value = int(input())
    d2[key] = value

x = d1.copy()

for key, value in d2.items():
    if key in x:
        x[key] -= value
        if x[key] < 0:
            x[key] = x[key] * -1
    else:
        x[key] = value

print(x)


# =====================================================================
# QUESTION 4
# =====================================================================
#
# Single File Programming Question
#
# Problem Statement
#
# Bobby is managing employee performance records across two
# departments. Each department has a separate list of employees with
# their scores from different evaluations. Bobby needs to combine these
# records, calculate the average score for each employee who appears in
# both departments, and round the result to two decimal places.
#
# Your task is to help Bobby by writing a program to compute the
# average score for each employee who appears in both departments.
#
# Input format:
# The first line of input consists of an integer n1, representing the
# number of employees in the first department.
# The next n1 lines each contain an integer followed by a list of
# integers, representing the employee ID and their scores in the first
# department.
# The next line consists of an integer n2, representing the number of
# employees in the second department.
# The following n2 lines each contain an integer followed by a list of
# integers, representing the employee ID and their scores in the second
# department.
#
# Output format:
# The output prints "{emp_id: 'average_score', ...}" followed by a
# dictionary where each key is an employee ID and the value is the
# average of all scores (from both sources) for that employee, rounded
# to two decimal places, represented as a dictionary of integers mapped
# to strings.
#
# Refer to the sample output for formatting specifications.

L = []
R = []
d = {}
e = {}

n = int(input())

for i in range(n):
    x = input().split()

    L = [int(i) for i in x]

    key = L[0]
    value = L[1:]
    d[key] = value

m = int(input())

for i in range(m):
    x = input().split()

    R = [int(i) for i in x]

    key = R[0]
    value = R[1:]
    e[key] = value

ans = {}
for key in d:
    if key in e:
        values = d[key] + e[key]
        avg = sum(values)/len(values)
        ans[key] = f"{avg:.2f}"

print(ans)