>.<

Title: Find the total number of interactions on days 0 and 2
Link: https://platform.stratascratch.com/coding/9788-find-the-total-number-of-interactions-on-days-0-and-2?code_type=2
Level: Easy

Find the total number of interactions on days 0 and 2.
Output the result alongside the day.

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

facebook_day = facebook[facebook['day'].isin([0,2])]

facebook_filter = facebook_day.groupby('day').size().reset_index(name='total_interactions')
    
Output:

day  |  total_interactions
0              4
2              3
