>.<

Title: Questions in Second Quarter
Link: https://platform.stratascratch.com/coding/2062-questions-in-second-quarter?code_type=2
Level: Easy

How many searches were there in the second quarter of 2021?

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
fb_searches = pd.DataFrame(fb_searches)

fb_searches_date = fb_searches[(fb_searches['date'].dt.year==2021) & (fb_searches['date'].dt.month.between(4,6))]['search_id'].count()

fb_searches_fix = pd.DataFrame({'searches':[fb_searches_date]})
    
Output:

searches
38
