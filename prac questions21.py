# =====================================================================
# QUESTION 1
# =====================================================================
#
# Single File Programming Question
#
# Problem Statement:
#
# Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
#
# Input format:
# The input consists of an integer n, representing the number to which
# the square values must be generated.
#
# Output format:
# The output prints the dictionary containing numbers from 1 to n as
# keys and their squares as values in the format:
# "Result {1: 1, 2: 4, ..., n: n*n}"
#
# Refer to the sample output for the formatting specifications.

# You are using Python
n = int(input())

d = {}

for i in range(1,n+1):
    d[i] = i*i

print("Result", d)