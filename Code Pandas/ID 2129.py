>.<

Title: Post Likes
Link: https://platform.stratascratch.com/coding/2129-post-likes?code_type=2
Level: Easy

You are given a list of posts of a Facebook user. Find the average number of likes.

Data fb_posts:
post_id: text
post_date: date
no_of_likes: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
fb_posts = pd.DataFrame(fb_posts)

fb_posts_avg = fb_posts['no_of_likes'].mean()

fb_posts_fix = pd.DataFrame({'average_number_of_likes':[fb_posts_avg]})
    
Output:

average_number_of_likes
41.15
