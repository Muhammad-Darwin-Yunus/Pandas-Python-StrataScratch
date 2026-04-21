>.<

Title: Users Activity Per Month Day
Link: https://platform.stratascratch.com/coding/2006-users-activity-per-month-day?code_type=2
Level: Easy

Return the total number of posts made on each calendar day of the month, aggregated across all months and years (ignoring user and year).

Data facebook_posts:
post_date: date
post_id: bigint
post_keywords: text
post_text: text
poster: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
facebook_posts = pd.DataFrame(facebook_posts)

facebook_posts['day_of_month'] = facebook_posts['post_date'].dt.day

facebook_posts_group = facebook_posts.groupby('day_of_month').size().reset_index(name='total_post')
    
Output:

day_of_month	total_post
1	3
2	3
