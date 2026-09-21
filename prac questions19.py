# =====================================================================
# QUESTION 1
# =====================================================================
#
# Single File Programming Question
#
# Problem Statement
#
# Mahi has participated in several sports events, and for each event,
# she receives medals represented by integers (e.g., 1 for Gold,
# 2 for Silver, 3 for Bronze). Mahi wants to keep track of how many
# medals she has won for each type.
#
# Write a program that takes a list of medal types as input and returns
# a dictionary that counts the number of each type of medal Mahi has won.
#
# Input format:
# The first line of input consists of an integer n, representing the
# number of medals Mahi has won.
# The next n lines consist of n integers, each representing a medal
# type Mahi has won.
#
# Output format:
# The output prints "Medal Count {medal_type: count, ...}" - a
# dictionary where:
# Each key is a medal type (represented as an integer, e.g., 1 for Gold,
# 2 for Silver, 3 for Bronze).
# Each value is the number of times that medal was awarded (an integer).
# The dictionary includes only those medals that were awarded at least
# once, and their counts are shown in the order they first appeared in
# the input.
#
# Refer to the sample output for the formatting specifications.
#
# Code constraints:
# 5 <= n <= 10

# You are using Python
n = int(input())

d = {}

for i in range(n):
    ind = int(input())

    if ind in d:
        d[ind] += 1
    else:
        d[ind] = 1

print("Medal Count", d)


# =====================================================================
# QUESTION 2
# =====================================================================
#
# Single File Programming Question
#
# Problem Statement
#
# Jack and Rose are managing the inventory for their respective stores.
# Each store has a list of items and the quantity they have in stock,
# represented as dictionaries. They need to merge these inventories.
# If an item is in both inventories, multiply their quantities.
# If an item is only in one inventory, include it with its quantity in
# the merged inventory.
#
# Help Jack and Rose to implement the above task using a dictionary.
#
# Input format:
# The first line of input consists of an integer n, representing the
# number of items in the first dictionary, dict1.
# The next 2×n lines represent the items of dict1, where each item is
# given on two consecutive lines:
# - One line containing an integer representing the item key.
# - The next line contains an integer representing the quantity value.
# The following line consists of an integer m, representing the number
# of items in the second dictionary dict2.
# The next 2×m lines represent the items of dict2 in the same
# two-line-per-item format.
#
# Output format:
# The output displays a dictionary where if a key is present in both
# dictionaries, the values are multiplied; otherwise, the key and its
# corresponding value are displayed.
#
# Refer to the sample output for formatting specifications.

# You are using Python

dict1 = {}
dict2 = {}

n = int(input())

for i in range(n):
    key = int(input())
    value = int(input())
    dict1[key] = value

m = int(input())

for i in range(m):
    key = int(input())
    value = int(input())
    dict2[key] = value

x = dict1.copy()

for key, value in dict2.items():
    if key in x:
        x[key] *= value
    else:
        x[key] = value

print(x)