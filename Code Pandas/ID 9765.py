>.<

Title: List all interactions of user wth id 4 on either day 0 or 2
Link: https://platform.stratascratch.com/coding/9765-list-all-interactions-of-user-wth-id-4-on-either-day-0-or-2?code_type=2
Level: Easy

List all interactions of user with id 4 on either day 0 or 2.

Data facebook_user_interactions:
day: bigint
user1: bigint
user2: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
facebook = pd.DataFrame(facebook_user_interactions)

facebook_filter = facebook[((facebook['user1']== 4) | (facebook['user2']== 4)) & ((facebook['day']== 0) | (facebook['day']== 2))]
    
Output:

day  |  user1  |  user2
2        4          1
2        4          2
2        4          0
