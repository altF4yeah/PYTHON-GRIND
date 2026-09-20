'''
Q39. Vinay works at a currency exchange counter and often bundles a
fixed denomination note repeated a certain number of times into a
stack. He wants a quick way to generate the stack and know how many
notes it contains and their total value.

Write a program that reads a note denomination value and the number
of times it should be repeated, creates a tuple using the repetition
operator, and prints the length of the resulting tuple and the total
value of all notes in it.

Input format:
The first line of input consists of an integer denomination
representing the value of the currency note.
The second line of input consists of an integer count representing
the number of times the note is repeated.

Output format:
The first line of output prints "Notes Count: " followed by the
length of the resulting tuple.
The second line of output prints "Total Value: " followed by the
total value of all notes in the tuple.

Code constraints:
1 <= denomination <= 2000
1 <= count <= 100

Sample Input 1:
200
3
Sample Output 1:
Notes Count: 3
Total Value: 600

Sample Input 2:
1000
7
Sample Output 2:
Notes Count: 7
Total Value: 7000
'''
x = int(input())
y = int(input())

print("Notes Count:", y)
print("Total Value:", y*x)


'''
Q40. Ganesh works for the city traffic department and records the
green light duration (in seconds) for 3 signals along a road. He
wants to check the duration at a given position and the duration of
the last signal using negative indexing.

Write a program that reads the durations of 3 signals and a position
to check, stores the durations in a tuple, and prints the duration at
the given position and the duration of the last signal using tuple
indexing.

Input format:
The first line of input consists of an integer signal1 representing
the duration of signal 1 in seconds.
The second line of input consists of an integer signal2 representing
the duration of signal 2 in seconds.
The third line of input consists of an integer signal3 representing
the duration of signal 3 in seconds.
The fourth line of input consists of an integer position representing
the index position to check.

Output format:
The first line of output prints "Duration At Position: " followed by
the duration at the given position.
The second line of output prints "Last Signal: " followed by the
duration of the last signal.

Code constraints:
10 <= signal1, signal2, signal3 <= 120
0 <= position <= 2

Sample Input 1:
40
50
60
1
Sample Output 1:
Duration At Position: 50
Last Signal: 60

Sample Input 2:
70
80
90
0
Sample Output 2:
Duration At Position: 70
Last Signal: 90
'''
signal1 = int(input())
signal2 = int(input())
signal3 = int(input())
t = (signal1, signal2, signal3)
i = int(input())

print("Duration At Position:", t[i])
print("Last Signal:", t[2])


'''
Q41. Meena runs a coffee shop and records the number of cups ordered
in each of 4 consecutive hours. She wants to see the hourly order
counts in reverse order, from the last hour back to the first, and
also just the counts recorded at every alternate hour starting from
the first hour.

Write a program that reads four integer order counts, one on each
line, stores them in a tuple, and uses tuple slicing to print the
reversed order counts and the alternate hour counts.

Input format:
The first line of input consists of an integer hour1 representing the
number of cups ordered in hour 1.
The second line of input consists of an integer hour2 representing
the number of cups ordered in hour 2.
The third line of input consists of an integer hour3 representing the
number of cups ordered in hour 3.
The fourth line of input consists of an integer hour4 representing
the number of cups ordered in hour 4.

Output format:
The first line of output prints "Reversed Orders: " followed by all
four hourly order counts in reverse order, space-separated.
The second line of output prints "Alternate Orders: " followed by
the order counts of hour 1 and hour 3, space-separated.

Code constraints:
1 <= each hour's order count <= 200

Sample Input 1:
15
25
35
45
Sample Output 1:
Reversed Orders: 45 35 25 15
Alternate Orders: 15 35

Sample Input 2:
70
90
110
130
Sample Output 2:
Reversed Orders: 130 110 90 70
Alternate Orders: 70 110
'''
hour1 = int(input())
hour2 = int(input())
hour3 = int(input())
hour4 = int(input())

print("Reversed Orders:", hour4, hour3, hour2, hour1)
print("Alternate Orders:",hour1, hour3)


'''
Q42. Jacob maintains a vending machine with 4 slots, each holding an
item priced at a fixed amount. When the price of slot 3 needs to be
doubled, he creates a new tuple with the updated price because tuples
cannot be modified directly.

Write a program that reads the prices of 4 slots, stores them in a
tuple, and creates a new tuple with the price of slot 3 doubled.
Print the original tuple and the updated tuple.

Input format:
The first line of input consists of an integer slot1 representing the
price of slot 1.
The second line of input consists of an integer slot2 representing
the price of slot 2.
The third line of input consists of an integer slot3 representing the
price of slot 3.
The fourth line of input consists of an integer slot4 representing
the price of slot 4.

Output format:
The first line of output prints "Original Prices: " followed by the
four original slot prices, space-separated.
The second line of output prints "Updated Prices: " followed by the
four slot prices after slot 3's price has been doubled,
space-separated.

Code constraints:
1 <= each slot price <= 500

Sample Input 1:
15
25
35
45
Sample Output 1:
Original Prices: 15 25 35 45
Updated Prices: 15 25 70 45

Sample Input 2:
80
40
20
60
Sample Output 2:
Original Prices: 80 40 20 60
Updated Prices: 80 40 40 60
'''
slot1 = int(input())
slot2 = int(input())
slot3 = int(input())
slot4 = int(input())

print("Original Prices:", slot1, slot2, slot3, slot4)
print("Updated Prices:", slot1, slot2, 2*slot3, slot4)


'''
Q43. Harish operates two delivery vans and logs the fuel consumed
(in litres) by each van over 2 trips, in order. He wants to compare
the two vans' fuel logs directly using tuple comparison to see which
log is considered "greater" based on Python's element-by-element
tuple comparison rule, or whether both logs are exactly equal.

Write a program that reads the fuel consumed by van A on 2 trips and
van B on 2 trips, stores each van's readings in its own tuple, and
compares the two tuples directly to print which van's tuple is
greater, or if they are equal.

Input format:
The first line of input consists of an integer a1 representing the
fuel consumed by van A on trip 1.
The second line of input consists of an integer a2 representing the
fuel consumed by van A on trip 2.
The third line of input consists of an integer b1 representing the
fuel consumed by van B on trip 1.
The fourth line of input consists of an integer b2 representing the
fuel consumed by van B on trip 2.

Output format:
The first line of output prints "Van A Log: " followed by the fuel
readings of van A, space-separated.
The second line of output prints "Van B Log: " followed by the fuel
readings of van B, space-separated.
The third line of output prints "Result: " followed by "Van A" if
van A's tuple is greater, "Van B" if van B's tuple is greater, or
"Equal" if both tuples are exactly the same.

Code constraints:
1 <= a1, a2, b1, b2 <= 200

Sample Input 1:
30
40
30
50
Sample Output 1:
Van A Log: 30 40
Van B Log: 30 50
Result: Van B

Sample Input 2:
45
45
44
99
Sample Output 2:
Van A Log: 45 45
Van B Log: 44 99
Result: Van A
'''
trip1 = int(input())
trip2 = int(input())
trip3 = int(input())
trip4 = int(input())

print("Van A Log:", trip1, trip2)
print("Van B Log:", trip3, trip4)

a = (trip1, trip2)
b = (trip3, trip4)

if a>b:
    x = "Van A"
elif b>a:
    x = "Van B"
else:
    x = "Equal"

print("Result:", x)