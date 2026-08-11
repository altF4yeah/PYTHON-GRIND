"""
================================================================================
Problem Statement: Single File Programming Question
================================================================================
A kid has a hobby of collecting coins and rupee notes in his piggy bank. The 
denominations of coins are one rupee, two rupees, five rupees, and ten rupees. 
Each year, he calculates the total amount of money saved and uses it to buy his 
favorite comic book. After purchasing the comic book, any remaining amount is 
returned to the piggy bank.

You need to automate this process. The program should calculate the total 
amount collected based on the number of coins and notes of each denomination, 
then compute the extra amount to be returned to the piggy bank.

Formula:
total_amount = (one_rupee * 1) + (two_rupee * 2) + (five_rupee * 5) + (ten_rupee * 10)
extra_amount = total_amount - comic_price

--------------------------------------------------------------------------------
Input Format:
The first line of input consists of an integer one_rupee representing the number of one rupee coins.
The second line consists of an integer two_rupee representing the number of two rupee coins.
The third line consists of an integer five_rupee representing the number of five rupee coins.
The fourth line consists of an integer ten_rupee representing the number of ten rupee coins.
The fifth line consists of an integer comic_price representing the price of the comic book.

--------------------------------------------------------------------------------
Output Format:
The output prints two integers on a single line, separated by a single space: 
the total amount collected followed by the extra amount to be returned to 
the piggy bank (e.g., 18 8).

--------------------------------------------------------------------------------
Code Constraints:
0 <= one_rupee, two_rupee, five_rupee, ten_rupee, comic_price <= 1000

--------------------------------------------------------------------------------
Sample Test Cases:

Sample 1:
Input:
1
1
1
1
10
Output:
18 8

Sample 2:
Input:
3
0
2
5
25
Output:
63 38
================================================================================
"""

# Solution Code

one_rupee = int(input())
two_rupee = int(input())
five_rupee = int(input())
ten_rupee = int(input())
comic_price = int(input())

total_amount = (one_rupee*1)+(two_rupee*2)+(five_rupee*5)+(ten_rupee*10)
extra_amount = total_amount - comic_price

print(total_amount, extra_amount)

"""
================================================================================
Problem Statement: Single File Programming Question
================================================================================
Bob, the owner of a popular bakery, wants to create a special offer code for 
his customers. To generate the code, he plans to combine the day of the month 
with the number of items left in stock.

Help Bob to encode these two values into a unique offer code.

Note: Use the bitwise operator (XOR) to calculate the offer code.

Example:
Input:
15
9

Output:
Offer code: 6

Explanation:
Given the day of the month 15th day (binary 1111) and there are 9 items 
left (binary 1001), the offer code is calculated as 0110 which is 6.

--------------------------------------------------------------------------------
Input format:
The first line of input consists of an integer D, representing the day of the month.
The second line consists of an integer S, representing the number of items left in stock.

--------------------------------------------------------------------------------
Output format:
The output displays "Offer code:" followed by an integer representing the 
encoded offer code.

Refer to the sample output for formatting specifications.

--------------------------------------------------------------------------------
Code constraints:
1 <= D <= 30
1 <= S <= 500

--------------------------------------------------------------------------------
Sample test cases:

Sample 1:
Input:
15
9
Output:
Offer code: 6

Sample 2:
Input:
20
15
Output:
Offer code: 27
================================================================================
"""

D = int(input())
S = int(input())

offer_code = D ^ S

print("Offer code:", offer_code)

"""
================================================================================
Problem Summary: Delivery Cost Calculator
================================================================================
Tinu works as a delivery person and needs to calculate the total cost of delivery 
for a given distance. The delivery company charges a base rate of Rs. 400 for up 
to 3 kilometers and an additional Rs. 80 for each kilometer beyond the first 3 
kilometers. Tinu wants to automate this calculation to save time.

Write a program that takes the distance in kilometers as input and outputs the 
number of full miles (1 mile = 1 kilometer beyond the initial 3 kilometers) and 
the total cost of delivery.

--------------------------------------------------------------------------------
Input format:
The input consists of an integer, representing the distance in kilometers.

--------------------------------------------------------------------------------
Output format:
The first line displays "Number of full miles: " followed by an integer, 
representing the number of full miles beyond the initial 3 kilometers.
The second line displays "Total cost of delivery: " followed by an integer, 
representing the total cost of delivery in Rupees.

--------------------------------------------------------------------------------
Code constraints:
1 <= distance <= 2000

--------------------------------------------------------------------------------
Sample test cases:

Input 1:
4

Output 1:
Number of full miles: 1
Total cost of delivery: Rs. 480

Input 2:
25

Output 2:
Number of full miles: 22
Total cost of delivery: Rs. 2160
================================================================================
"""

n = int(input())

nofm = (n - 3) // 1
tc = 400 + (nofm * 80)

print(f"Number of full miles: {nofm}")
print(f"Total cost of delivery: Rs.{tc}")

"""
================================================================================
Problem Summary: Movie Download Time Calculator
================================================================================
Oliver is planning a movie night with his friends and wants to download a 
high-definition movie. He knows the file size of the movie in megabytes (MB) 
and his internet speed in megabits per second (Mbps). To ensure the movie is 
ready in time, Oliver needs to calculate the download time.

Your task is to write a program that calculates the download time and displays 
it in hours, minutes, and seconds.

Explanation:
1. Convert the file size to bits (800 MB * 8 bits/byte = 6400 megabits) and 
   divide it by the download speed (6400 Mbps / 40 Mbps = 160 seconds).
2. Now, convert the download time in seconds to hours, minutes, and seconds: 
   160 seconds is equal to 2 minutes and 40 seconds.
So, the download time is 0 hours, 2 minutes, and 40 seconds.

--------------------------------------------------------------------------------
Input format:
The first line of input consists of an integer N, representing the file size 
in megabytes (MB).
The second line consists of an integer S, representing the network speed in 
megabits per second (Mbps).

--------------------------------------------------------------------------------
Output format:
The output prints "Download Time: X hours, Y minutes, and Z seconds", where 
X, Y,```python

Example:
Input:
MB = 800
mbps = 40

Output:
Download Time: 0 hours, 2 minutes, and 40 seconds


"""

N = int(input())
S = int(input())

bits = (N*8)
ds = bits/S

X=(ds // 3600)
Y=(ds % 3600) // 60
Z=(ds % 60)

print (f"Download Time: {X:.0f}hours, {Y:.0f}Minutes, and {Z:.Of} seconds")