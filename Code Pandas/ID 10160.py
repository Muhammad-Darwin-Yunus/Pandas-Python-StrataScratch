>.<

Title: Rank guests based on their ages
Link: https://platform.stratascratch.com/coding/10160-rank-guests-based-on-their-ages?code_type=2
Level: Easy

Rank guests based on their ages.
Output the guest id along with the corresponding rank.
Order records by the age in descending order.

Data airbnb_guests:
guest_id: int
nationality: varchar
gender: varchar
age: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

rank_guest = pd.DataFrame(airbnb_guests)

rank_guest['rank'] = rank_guest['age'].rank(ascending=False,method='min')

rank_guest_sort = rank_guest.sort_values(by='age',ascending=False)

rank_guest_sort[['guest_id','rank']]

Output:

guest_id  |  rank
8              1
5              2
6              3
9              4
10              5
2              6
7              6
3              8
11              8
1              10
0              11
4              12
