'''
Q32. Tom has a tuple of colors, and he needs a program to check if a
specific color exists in the tuple. Write a Python program that takes
a tuple of colors as input, and then determines if the entered color
is present in the tuple.

Input format:
The first line of input consists of a comma-separated string
representing a tuple of colors.
The second line of input consists of a single string representing the
color to be checked.

Output format:
The output consists of any one of the following:
If the entered color is found in the tuple, then print "The color
'<color>' is in the tuple."
If the entered color is not found in the tuple, then print "The color
'<color>' is not in the tuple."

Code constraints:
1 <= number of colors in the tuple <= 10
The input color to be checked is case-sensitive
Each color is a non-empty string consisting of alphabetic characters
only

Sample Input 1:
red,green,blue,yellow
blue
Sample Output 1: The color 'blue' is in the tuple.

Sample Input 2:
red,green,blue,yellow
orange
Sample Output 2: The color 'orange' is not in the tuple.
'''
x = tuple(input().split(","))
y = input()

if y in x:
    print(f"The color '{y}' is in the tuple.")
else:
    print(f"The color '{y}' is not in the tuple.")


'''
Q33. Charlie needs to analyze rainfall data for multiple years to
determine the average monthly rainfall for a specific year. He has a
tuple where each element is another tuple representing the monthly
rainfall data for a year.

Help Charlie by writing a program that extracts the rainfall data for
a given year and calculates the average monthly rainfall for that
year.

Input format:
The first line of input consists of an integer n, representing the
number of years.
The next n lines each contain 12 space-separated integers,
representing the monthly rainfall data for each year (one year per
line).
The last line consists of an integer year, representing the year
number (1-based index) for which the average monthly rainfall should
be calculated.

Output format:
The output displays a float value representing the average monthly
rainfall for the specified year, rounded to two decimal points.

Code constraints:
1 <= n <= 15
1 <= rainfall <= 100
1 <= year <= n

Sample Input 1:
5
90 89 1 29 87 68 11 79 ...   
73 28 75 14 54 28 9 63 ...   
11 6 66 36 70 52 15 20 ...   
64 22 29 28 15 34 40 79 ...  
69 17 11 83 30 45 25 92 ...  
4
Sample Output 1: 39.50

Sample Input 2:
4
87 27 68 66 46 71 43 34 ...  
57 58 69 83 78 79 47 98 ...  
46 29 68 35 53 36 25 11 ...  
76 4 33 73 97 98 7 78 ...    
4
Sample Output 2: 48.83
'''
n = int(input())
L = []

for _ in range(n):
    x = input().split()
    L.append([int(i) for i in x])

z = int(input())
t = L[z-1]

avg = sum(t)/12

print(f"{avg:.2f}")