>.<

Title: Find the number of views each post has
Link: https://platform.stratascratch.com/coding/9770-find-the-number-of-views-each-post-has?code_type=2
Level: Easy

Find the number of views each post has.
Output the post id along with the number of views.
Order records by post id in ascending order.

Data facebook_post_views:
post_id: bigint
viewer_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_post_views)

facebook_post = facebook.groupby('post_id')['viewer_id'].sum().reset_index(name='total_views')

facebook_sort = facebook_post.sort_values(by='post_id',ascending=True)
    
Output:

post_id  |  total_views
3              6
4              3
5              3
