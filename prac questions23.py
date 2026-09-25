# =====================================================================
# QUESTION 5
# =====================================================================
#
# Maya wants to create a dictionary that maps each integer from 1 to a
# given number n to its square. She will use this dictionary to quickly
# reference the square of any number up to n.
#
# Help Maya generate this dictionary based on the input she provides.
#
# Input format:
# The input consists of an integer n, representing the highest number
# for which Maya wants to calculate the square.
#
# Output format:
# The output displays the generated dictionary where each key is an
# integer from 1 to n, and the corresponding value is its square.
#
# Refer to the sample output for formatting specifications.
#
# Code constraints:
# 1 <= n <= 20

# You are using Python
n = int(input())

d = {}

for i in range(1,n+1):
    d[i]=i*i

print(d)


# =====================================================================
# QUESTION 6
# =====================================================================
#
# Noah, a global analyst at a demographic research firm, has been
# tasked with identifying which country experienced the largest
# population growth over a two-year period. He has a dataset where each
# entry consists of a country code and its population figures for two
# consecutive years. Noah needs to determine which country had the
# highest increase in population and present the result in a specific
# format.
#
# Help Noah by writing a program that outputs the country code with the
# largest population increase, along with the increase itself.
#
# Input format:
# The first line of input consists of an integer N, representing the
# number of countries.
# Each of the following N blocks contains three lines:
# The first line is a country code.
# The second line is an integer representing the population of the
# country in the first year.
# The third line is an integer representing the population of the
# country in the second year.
#
# Output format:
# The output displays the country code and the population increase in
# the format {code:difference}, where code is the country code and
# difference is the increase in population.
#
# Refer to the sample output for formatting specifications.
#
# Code constraints:
# 1 <= N <= 15
# 01 <= country code <= 09
# 1 <= population <= 10000

# You are using Python
n = int(input())
L = []
R = []
for i in range(1,n+1):
    cc = input().strip()
    x = int(input())
    y = int(input())

    L.append(y-x)
    R.append(cc)
m = max(L)
i = L.index(m)

d = {i+1:m}
a = [f"{k:02d}:{v}" for k, v in d.items()]
b = "{" + ", ".join(a) + "}"

print(b)