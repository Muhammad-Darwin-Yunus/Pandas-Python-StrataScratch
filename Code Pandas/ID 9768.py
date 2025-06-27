>.<

Title: Posts with 'nba' substring in keyword
Link: https://platform.stratascratch.com/coding/9768-find-all-posts-with-the-keyword-nba?code_type=2
Level: Easy

Find all posts with a keyword that contains 'nba' substring. For such rows output all columns.

Data facebook_posts:
post_id: bigint
poster: bigint
post_text: text
post_keywords: text
post_date: datetime

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_posts)

facebook_keyword = facebook[facebook['post_keywords'].str.contains('nba',case=False,na=False)]
    
Output:

post_id  |  poster  |  post_text                                |  post_keywords              |  post_date
0            2        The Lakers game from last night was great.	[basketball,lakers,nba]	        2019-01-01 00:00:00
1            1        Lebron James is top class.                  [basketball,lebron_james,nba]	  2019-01-02 00:00:00
