>.<

Title: Find the number of entries per star
Link: https://platform.stratascratch.com/coding/10054-find-the-number-of-entries-per-star?code_type=2
Level: Easy

Find the number of entries per star.
Output each number of stars along with the corresponding number of entries.
Order records by stars in ascending order.

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

entries_star = pd.DataFrame(yelp_reviews)

entries_per_star = entries_star.groupby('stars').agg(total_stars=('stars','count')).reset_index()

entries_per_star_sort = entries_per_star.sort_values(by='stars')

Output:

stars  |  total_stars
?            5
1            7
2            11
3            16
4            33
5            34
