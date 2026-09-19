'''
Q34. Neha is building a small music app and wants to store the
duration (in minutes) of 4 songs in a playlist. She wants to quickly
know the total playtime of the playlist and the duration of the
longest song.

Write a program that reads the durations of 4 songs, one on each
line, creates a tuple from them, and uses sum() and max() to print
the total playtime and the longest song's duration.

Input format:
The first line of input consists of an integer song1 representing the
duration of song 1 in minutes.
The second line of input consists of an integer song2 representing
the duration of song 2 in minutes.
The third line of input consists of an integer song3 representing the
duration of song 3 in minutes.
The fourth line of input consists of an integer song4 representing
the duration of song 4 in minutes.

Output format:
The first line of output prints "Total Playtime: " followed by the
sum of all song durations.
The second line of output prints "Longest Song: " followed by the
duration of the longest song.

Code constraints:
1 <= each song duration <= 20

Sample Input 1:
4
6
3
5
Sample Output 1:
Total Playtime: 18
Longest Song: 6

Sample Input 2:
9
2
11
7
Sample Output 2:
Total Playtime: 29
Longest Song: 11
'''
song1 = int(input())
song2 = int(input())
song3 = int(input())
song4 = int(input())

L = [song1, song2, song3, song4]

a = sum(L)
b = max(L)

print("Total Playtime:", a)
print("Longest Song:", b)


'''
Q35. Tara is a school administrator who records the scores of a
student in 4 subject tests. She wants to view the scores of the first
two tests and the last two tests separately to compare performance
across the term.

Write a program that reads four integer scores, one on each line,
stores them in a tuple, and uses tuple slicing to print the first two
scores and the last two scores.

Input format:
The first line of input consists of an integer test1 representing the
score of test 1.
The second line of input consists of an integer test2 representing
the score of test 2.
The third line of input consists of an integer test3 representing the
score of test 3.
The fourth line of input consists of an integer test4 representing
the score of test 4.

Output format:
The first line of output prints "First Half: " followed by the
scores of test 1 and test 2, space-separated.
The second line of output prints "Second Half: " followed by the
scores of test 3 and test 4, space-separated.

Code constraints:
0 <= each test score <= 100

Sample Input 1:
75
82
91
68
Sample Output 1:
First Half: 75 82
Second Half: 91 68

Sample Input 2:
60
40
30
55
Sample Output 2:
First Half: 60 40
Second Half: 30 55
'''
test1 = int(input())
test2 = int(input())
test3 = int(input())
test4 = int(input())

print("First Half:", test1, test2)
print("Second Half:", test3, test4)


'''
Q36. Suresh manages a small parking lot with 3 slots and records
whether each slot is occupied (1) or free (0). He wants to check the
occupancy status at a given slot position entered by the security
guard.

Write a program that reads the occupancy status of 3 slots and a
position to check, stores the statuses in a tuple, and prints the
status at slot 1 and at the requested position using tuple indexing.

Input format:
The first line of input consists of an integer slot1 representing the
occupancy status of slot 1.
The second line of input consists of an integer slot2 representing
the occupancy status of slot 2.
The third line of input consists of an integer slot3 representing the
occupancy status of slot 3.
The fourth line of input consists of an integer position representing
the index position to check.

Output format:
The first line of output prints "Slot 1 Status: " followed by the
occupancy status of slot 1.
The second line of output prints "Status At Position: " followed by
the occupancy status at the given position.

Code constraints:
0 <= slot1, slot2, slot3 <= 1
0 <= position <= 2

Sample Input 1:
1
1
1
0
Sample Output 1:
Slot 1 Status: 1
Status At Position: 1

Sample Input 2:
0
0
1
2
Sample Output 2:
Slot 1 Status: 0
Status At Position: 1
'''
slot1 = int(input())
slot2 = int(input())
slot3 = int(input())
i = int(input())
t = (slot1, slot2, slot3)

print("Slot 1 status:",slot1)
print("Status At position:",t[i])


'''
Q37. Rohan runs a courier service and delivers 2 packages in the
morning shift and 2 packages in the evening shift, each with a
recorded weight in kilograms. At the end of the day, he wants to
combine both shifts into a single record and know the total weight
delivered.

Write a program that reads the weights of 2 morning packages and 2
evening packages, stores each shift's weights in its own tuple,
concatenates them into a single combined tuple, and prints the
combined tuple and the total weight.

Input format:
The first line of input consists of an integer m1 representing the
weight of morning package 1.
The second line of input consists of an integer m2 representing the
weight of morning package 2.
The third line of input consists of an integer e1 representing the
weight of evening package 1.
The fourth line of input consists of an integer e2 representing the
weight of evening package 2.

Output format:
The first line of output prints "Combined: " followed by all four
package weights, space-separated, in the order morning then evening.
The second line of output prints "Total Weight: " followed by the sum
of all package weights.

Code constraints:
1 <= m1, m2, e1, e2 <= 100

Sample Input 1:
8
12
20
10
Sample Output 1:
Combined: 8 12 20 10
Total Weight: 50

Sample Input 2:
30
40
10
20
Sample Output 2:
Combined: 30 40 10 20
Total Weight: 100
'''
m1 = int(input())
m2 = int(input())
e1 = int(input())
e2 = int(input())

print("Combined:", m1, m2, e1, e2)
print("Total Weight:", m1+m2+e1+e2)


'''
Q38. Deepak works at a weather station and records the temperature
readings (in Celsius) taken at 3 different times during the day. He
wants to check how many times a specific target temperature was
recorded and whether it appeared at all.

Write a program that reads three integer temperature readings and a
target temperature, stores the readings in a tuple, and uses the
count() method and the in operator to print the required details.

Input format:
The first line of input consists of an integer temp1 representing the
temperature reading at time 1.
The second line of input consists of an integer temp2 representing
the temperature reading at time 2.
The third line of input consists of an integer temp3 representing the
temperature reading at time 3.
The fourth line of input consists of an integer target representing
the temperature to search for.

Output format:
The first line of output prints "Occurrences: " followed by the
number of times the target temperature was recorded.
The second line of output prints "Present: " followed by "True" if
the target temperature is in the tuple, or "False" otherwise.

Sample Input 1:
15
18
15
15
Sample Output 1:
Occurrences: 2
Present: True

Sample Input 2:
22
24
26
30
Sample Output 2:
Occurrences: 0
Present: False
'''
temp1 = int(input())
temp2 = int(input())
temp3 = int(input())
i = int(input())
t =(temp1, temp2, temp3)
x = t.count(i)
if i in t:
    y = True
else:
    y = False

print("Occurrences:", x)
print("Present:", y)