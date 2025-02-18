>.<

Title: User Exile
Link: https://platform.stratascratch.com/coding/10091-user-exile?code_type=2
Level: Easy

Find the number of relationships that user  with id == 1 is not part of.

Data facebook_friends:
user1: int
user2: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

user_exile = pd.DataFrame(facebook_friends)

user_exile = user_exile[(user_exile['user1']!=1) & (user_exile['user2']!=1)]

Output:

user1  |  user2
2          6
7          2
8          3
3          9
