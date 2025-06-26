>.<

Title: Find all users who liked a post
Link: https://platform.stratascratch.com/coding/9769-find-all-friends-who-liked-a-post?code_type=2
Level: Easy

Find all users who liked one or more posts

Data facebook_reactions:
poster: bigint
friend: bigint
reaction: text
date_day: int
post_id: bigint
date_day: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_reactions)

facebook_like = facebook[facebook['reaction']=='like']['friend'].drop_duplicates()
    
Output:

friend
1
6
2
4
3
5
