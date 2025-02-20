>.<

Title: Gender With Generous Reviews
Link: https://platform.stratascratch.com/coding/10149-gender-with-generous-reviews?code_type=2
Level: Easy

Write a query to find which gender gives a higher average review score when writing reviews as guests.
Use the from_type column to identify guest reviews.
Output the gender and their average review score.

Data airbnb_reviews:
from_user: bigint
to_user: bigint
from_type: text
to_type: text
review_score: bigint

Data airbnb_guests:
guest_id: bigint
nationality: text
gender: text
age: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

gender_reviews = pd.merge(airbnb_reviews,airbnb_guests,left_on='from_user',right_on='guest_id',how='left')

gender_reviews_type = gender_reviews[gender_reviews['to_type']=='guest']

gender_reviews_user = gender_reviews_type.groupby('gender')['from_user'].mean().reset_index()

gender_reviews_fix = pd.DataFrame({'gender':gender_reviews_user['gender'],'average_review_score':gender_reviews_user['from_user']})
    
Output:

gender  |  average_review_score
F                5.25
M                5.92
