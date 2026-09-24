# =====================================================================
# QUESTION 3
# =====================================================================
#
# Problem Statement
#
# Lucas is working on a project where he needs to analyze movie ratings
# by genre. He has a dataset where each movie's genre and rating are
# recorded. To make sense of the data, Lucas wants to calculate the
# average rating for each genre. He needs a program to process this
# data, compute the average ratings, and print them in ascending order
# of genre numbers.
#
# Help Lucas by writing a program that performs this analysis and
# provides the average ratings in the required format.
#
# Input format:
# The first line of input consists of an integer n, representing the
# number of entries in the dataset.
# The next 2n lines contain the data for n entries, where for each
# entry:
# The first line contains an integer representing the genre ID of the
# movie.
# The second line contains an integer representing the rating of that
# movie.
#
# Output format:
# The output prints a dictionary in the following format
# "{genre_id: 'average_rating', ...}" where:
# Each key is a genre ID (integer).
# Each value is the average rating for that genre, rounded to two
# decimal places and represented as a string (e.g., '6.67').
# The dictionary is sorted in ascending order of genre ID.
#
# Refer to the sample output for formatting specifications.

n = int(input())
d = {}

for i in range(n):
    d_id = int(input())
    rating = float(input())

    if d_id not in d:
        d[d_id] = []

    d[d_id].append(rating)

od = {}

for d_id in sorted(d.keys()):
    avg = sum(d[d_id]) / len(d[d_id])

    od[d_id] = f"{avg:.2f}"

print(od)


# =====================================================================
# QUESTION 4
# =====================================================================
#
# Tom wants to create a dictionary that lists the first n prime
# numbers, where each key represents the position of the prime number,
# and the value is the prime number itself.
#
# Help Tom generate this dictionary based on the input he provides.
#
# Input format:
# The input consists of an integer n, representing the number of prime
# numbers Tom wants to generate.
#
# Output format:
# The output displays the generated dictionary where each key is an
# integer from 1 to n, and the corresponding value is the prime number.
#
# Refer to the sample output for formatting specifications.

# You are using Python

p = int(input())

def check_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n <1:
        return False
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

c = 1
d = {}
i = 2
while c<=p:
    if check_prime(i):
        d[c] = i
        c += 1
    i += 1

print(d)