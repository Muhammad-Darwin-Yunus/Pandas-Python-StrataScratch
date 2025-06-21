>.<

Title: Users with Many Searches
Link: https://platform.stratascratch.com/coding/2061-users-with-many-searches?code_type=2
Level: Easy

Count the number of users who made more than 5 searches in August 2021.

Data fb_searches:
age_group: text
date: date
search_id: bigint
search_query: text
user_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

fb = pd.DataFrame(fb_searches)

fb_date = fb[(fb['date'].dt.month == 8) & (fb['date'].dt.year == 2021)]

fb_user = fb_date.groupby('user_id').size()

fb_filter = fb_user[fb_user > 5]

fb_count = fb_filter.count

fb_name = pd.DataFrame({'users_more_5_search': [fb_filter.count()]})
    
Output:

users_more_5_search
2
