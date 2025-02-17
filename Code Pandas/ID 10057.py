>.<

Title: Find the number of 5-star reviews earned by Lo-Lo's Chicken & Waffles
Link: https://platform.stratascratch.com/coding/10057-find-the-number-of-5-star-reviews-earned-by-lo-los-chicken-waffles?code_type=2
Level: Easy

Find the number of 5-star reviews earned by Lo-Lo's Chicken & Waffles.

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

lolo_five_Star = pd.DataFrame(yelp_reviews)

lolo_five_Star = lolo_five_Star[lolo_five_Star['business_name']=="Lo-Lo's Chicken & Waffles"]

lolo_five_Star = lolo_five_Star.groupby('business_name').agg(stars=('stars','first'),total_reviews=('stars','count'))

Output:

business_name              |  stars  |  total_reviews
Lo-Lo's Chicken & Waffles      5            1
