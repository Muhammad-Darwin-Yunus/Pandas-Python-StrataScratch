>.<

Title: Find the number of reviews received by Lo-Lo's Chicken & Waffles for each star
Link: https://platform.stratascratch.com/coding/10058-find-the-number-of-reviews-received-by-lo-los-chicken-waffles-for-each-star?code_type=2
Level: Easy

Find the number of reviews received by Lo-Lo's Chicken & Waffles for each star.
Output the number of stars along with the corresponding number of reviews.
Sort records by stars in ascending order.

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

lolo_chicken = pd.DataFrame(yelp_reviews)

lolo_chicken_star = lolo_chicken[lolo_chicken['business_name']=="Lo-Lo's Chicken & Waffles"]

lolo_chicken_fix = lolo_chicken_star.groupby('business_name').agg(stars=('stars','sum'),total_review_id=('review_id','count')).reset_index()

Output:

business_name            |  stars  |  total_review_id
Lo-Lo's Chicken & Waffles      5            1
