'''
============================================================
Question 21: RGB Color Mixing (Debugging with Tuples)
============================================================

Problem Statement:
Sita is working on a graphics application where she needs to mix
two RGB colors. The colors are represented as tuples, and she
wants to calculate the average color by blending the two RGB
values. The blending is done by averaging the corresponding red,
green, and blue values. However, there is a bug in the code that
prevents the correct result from being printed.

Your task is to debug the code that calculates the mixed color
from the two provided RGB tuples. Make sure to use tuples and
ensure the calculation of the mixed color is correct.

Formulas:
Mixed Red = (color1[0] + color2[0]) // 2
Mixed Green = (color1[1] + color2[1]) // 2
Mixed Blue = (color1[2] + color2[2]) // 2

Input format:
The first three lines of input represent the red, green, and
blue components of the first color, respectively.
The next three lines represent the red, green, and blue
components of the second color.

Output format:
The output prints: "Mixed RGB: " followed by the mixed color
tuple.

Code constraints:
Each RGB component is an integer between 0 and 255.

Sample test cases:
Input 1:
255
0
0
0
255
255
Output 1: Mixed RGB: (127, 127, 127)

Input 2:
100
150
200
50
100
150
Output 2: Mixed RGB: (75, 125, 175)

You are using Python
'''
color1 = (
    int(input()),
    int(input()),
    int(input())
)
color2 = (
    int(input()),
    int(input()),
    int(input())
)

mixed_color = (
    (color1[0] + color2[0]) // 2,
    (color1[1] + color2[1]) // 2,
    (color1[2] + color2[2]) // 2
)

print("Mixed RGB:", mixed_color)


'''
============================================================
Question 22: Student Performance Report (Tuple Traversal)
============================================================

Problem Statement:
Sophia is a class teacher who maintains student records in a
school database. For a particular assessment, the system
provides her with two fixed collections in the form of tuples:
- one tuple containing student names
- another tuple containing their corresponding scores

Each student's name should match with the score at the same
position in the tuple. Sophia needs to generate a performance
report by pairing each student with their score.

However, due to system issues, sometimes the number of names
and scores may not match, and in such cases, the report should
not be generated. Also, if any score is outside the valid range
(0 to 100), it should be reported as invalid for that student.

She must generate the final report without using built-in
functions like zip() or list conversion, and must rely only on
tuple traversal.

Input format:
The first line contains a tuple of student names.
The second line contains a tuple of corresponding student
scores.

Output format:
If the number of names and scores are equal and all scores are
valid (0 to 100), the output prints:
Name: <student_name>
Score: <score>

If the number of names and scores are not equal, the output
prints "The number of names and scores must be the same."

If any score is invalid (not in range 0 to 100), the output
prints "Error: Invalid score for <student_name>." (Continue
printing for remaining valid entries)

Code constraints:
1 <= number of students <= 100
Score range: 0 to 1000

Sample test cases:
Input 1:
Alice Bob Charlie
85 92 78
Output 1:
Name: Alice
Score: 85
Name: Bob
Score: 92
Name: Charlie
Score: 78

Input 2:
Alice Bob
85 92 78
Output 2: The number of names and scores must be the same.

Input 3:
Alice Bob
105 92
Output 3:
Error: Invalid score for Alice.
Name: Bob
Score: 92

You are using Python
'''
name = tuple(input().split())
score = input().split()

L = []
for i in score:
    L.append(int(i))

score = (L)

for i in range(0, len(name)):
    if len(name)==len(score):
        if score[i] > 100:
            print(f"Error: Invalid score for {name[i]}.")
            i += 1
        else:
            print("Name:", name[i])
            print("Score:", score[i])
    else:
        print("The number of names and scores must be the same.")
        break


'''
============================================================
Question 23: Cumulative Product of Treasure Hunt Clues
============================================================

Problem Statement:
Daniel is organizing a treasure hunt where each participant's
clues are represented as a tuple of integers. Each integer
represents the points earned for solving a clue.

To determine who performed best, Daniel needs to calculate the
cumulative product of the points for each participant. Since
tuples are immutable, he will use a list to compute and store
the intermediate results before converting it back to a tuple.

Input format:
The first line of input contains an integer n, representing the
size of the tuple.
The second line contains n space-separated integers,
representing the points gained from solving each clue.

Output format:
The output format is: (element1, element2, element3, ...)
Each cumulative product is printed in a tuple format, with the
values separated by commas.

Code constraints:
3 <= n <= 12
1 <= tuple elements <= 15

Sample test cases:
Input 1:
3
6 1 8
Output 1: (6, 6, 48)

Input 2:
4
1 9 12 12
Output 2: (1, 9, 108, 1296)

You are using Python
'''
n = int(input())

x = input().split()

L = []

for i in x:
    L.append(int(i))

a = []
k = 1

for i in range(0, n):
    k = L[i]*k
    a.append(k)

t = tuple(a)
print(t)