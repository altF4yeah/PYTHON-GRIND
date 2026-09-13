'''
============================================================
Question 18: Find Peaks in a List of Measurements
============================================================

Problem Statement:
Kyara is analyzing a series of measurements taken over time. She
needs to identify all the "peaks" in this list of integers.

A peak is defined as an element that is greater than its
immediate neighbors. Boundary elements are considered peaks if
they are greater than their single neighbor.

Your task is to find and list all such peaks using list
comprehension.

Example:
Input:  1 3 2 4 1 5 7 6 10 2 8
Output: Peaks: [3, 4, 7, 10, 8]

Explanation:
3 is a peak because it's greater than 1 and 2.
4 is a peak because it's greater than 2 and 1.
7 is a peak because it's greater than 5 and 6.
10 is a peak because it's greater than 6 and 2.
8 is a peak because it is a boundary element and it is greater
than 2.

Input format:
The input consists of several integers separated by spaces,
representing the measurements.

Output format:
The output displays "Peaks: " followed by a list of integers,
representing the peak elements in the list.

Code constraints:
1 <= list elements <= 25

Sample test cases:
Input 1:  1 3 2 4 1 5 7 6 10 2 8
Output 1: Peaks: [3, 4, 7, 10, 8]

Input 2:  1 2 1
Output 2: Peaks: [2]

You are using Python
'''
x=input().split()

L = []
for i in x:
    L.append(int(i))

r = []

for i in range(0, len(L)-2):
    j = i+1
    k = i+2
    if L[j] > L[i] and L[j] > L[k]:
        r.append(L[j])

if L[-1] > L[-2]:
    r.append(L[-1])

print("Peaks:", r)


'''
============================================================
Question 19: Pet Adoption Center (Debugging with Tuples)
============================================================

Problem Statement:
Yamine manages a pet adoption center and keeps track of the pets
available for adoption using tuples. Each pet has a name and
age, and he wants to find out the pet at a specific index and
count how many pets are younger than 3 years old. The data for
each pet is stored as a tuple. The code provided has some
issues.

Your task is to debug the code and correct it to ensure that it
works as expected.

Input format:
The first line of input consists of an integer pet_count (the
number of pets in the adoption center).
The next pet_count pairs of lines:
The first line of each pair contains the name (a string) of the
pet.
The second line of each pair contains the age (an integer) of
the pet.
The last line contains an integer search_index, which is used to
find the pet at the given index.

Output format:
The first line of output prints: "Pet found: " followed by the
name of the pet at the given index.
The second line of output prints: "Young pets: " followed by the
number of pets that are younger than 3 years old.

Code constraints:
1 <= pet_count <= 100

Sample test cases:
Input 1:
4
Rocky
2
Charlie
4
Bella
1
Cody
3
2
Output 1:
Pet found: Bella
Young pets: 2

You are using Python
'''
pet_count = int(input())
pet_list = []

for i in range(pet_count):
    name = input()
    age = int(input())
    pet_info = (name, age)
    pet_list.append(pet_info)

search_index = int(input())
selected_pet = pet_list[search_index]
print("Pet found:", selected_pet[0])

young_pets = []
for pet in pet_list:
    if pet[1] < 3:
        young_pets.append(pet)
print("Young pets:", len(young_pets))


'''
============================================================
Question 20: Sports Team Performance (Debugging with Tuples)
============================================================

Problem Statement:
Kalia is tracking the performance of a sports team across
multiple games. He records the team's name and their scores for
four games. Kalia wants to calculate the total points scored by
the team and determine the best performance (highest score in a
single game). The data for each game score is stored as a tuple.
The code provided has some issues.

Your task is to debug the code and correct it to ensure that it
works as expected.

Input format:
The first line of input consists of the team's name (a string).
The second line of input consists of the score for the first
game (an integer).
The third line of input consists of the score for the second
game (an integer).
The fourth line of input consists of the score for the third
game (an integer).
The fifth line of input consists of the score for the fourth
game (an integer).

Output format:
The first line of output prints: "Team: " followed by the
team's name.
The second line of output prints: "Total points: " followed by
the sum of the game scores.
The third line of output prints: "Best game: " followed by the
highest score in a single game.

Code constraints:
The game scores are integers between 0 and 1000.
1 <= team name length <= 100

Sample test cases:
Input 1:
Warriors
100
120
110
130
Output 1:
Team: Warriors
Total points: 460
Best game: 130

You are using Python
'''
team_name = input()
game1_score = int(input())
game2_score = int(input())
game3_score = int(input())
game4_score = int(input())

team_performance = (team_name, (game1_score, game2_score, game3_score, game4_score))
match_scores = team_performance[1]
total_points = sum(match_scores)
best_performance = max(match_scores)

print("Team:", team_performance[0])
print("Total points:", total_points)
print("Best game:", best_performance)