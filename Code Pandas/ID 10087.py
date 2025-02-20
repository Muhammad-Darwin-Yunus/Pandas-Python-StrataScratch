>.<

Title: Find all posts which were reacted to with a heart
Link: https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=2
Level: Easy

Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

Data facebook_reactions:
poster: int
friend: int
reaction: varchar
date_day: int
post_id: int

Data facebook_posts:
post_id: int
poster: int
post_text: varchar
post_keywords: varchar
post_date: datetime

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

post_heart = pd.merge(facebook_reactions,facebook_posts,how='inner',on='post_id')

post_heart_react = post_heart[post_heart['reaction']=='heart']

post_heart.distinct = post_heart_react[['post_id','poster_y','post_text','post_keywords','post_date']].drop_duplicates()

Output:

post_id  |  poster_y  |  post_text                 |                  post_keywords              |        post_date
0            2        The Lakers game from last night was great.    [basketball,lakers,nba]        2019-01-01 00:00:00
