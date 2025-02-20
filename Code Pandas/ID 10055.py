>.<

Title: Records With '?'
Link: https://platform.stratascratch.com/coding/10055-records-with?code_type=2
Level: Easy

Find records with the value '?' in the stars column.

Data yelp_reviews:
business_name: varchar
review_id: varchar
user_id: varchar
stars: varchar
review_date: datetime
review_text: varchar
funny: int
useful: int
cool: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

question_mark = pd.DataFrame(yelp_reviews)

question_mark_stars = question_mark[question_mark['stars']=='?']

question_mark_stars[['business_name','stars']]

Output:

business_name          |  stars
Residence Inn Tempe        ?
Maloney's on Shea          ?
China King                  ?
Arriba Mexican Grill        ?
Stacy's Pit Stop BBQ        ?
