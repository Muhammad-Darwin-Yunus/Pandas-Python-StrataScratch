>.<

Title: Cast stars column values to integer and return with all other column values
Link: https://platform.stratascratch.com/coding/10056-cast-stars-column-values-to-integer-and-return-with-all-other-column-values?code_type=2
Level: Easy

Cast stars column values to integer and return with all other column values.
Be aware that certain rows contain non integer values.
You need to remove such rows. You are allowed to examine and explore the dataset before making a solution.

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

cast_stars = pd.DataFrame(yelp_reviews)

cast_stars_column = cast_stars[cast_stars['stars'].str.contains(r'[0-9]',regex=True,na=False)]

cast_stars_column['stars_int'] = pd.to_numeric(cast_stars_column['stars'],errors='coerce',downcast='unsigned')

cast_stars_column['stars_int']

Output:

stars_int
5
4
5
3
3
1
5
4
4
5
5
4
3
4
4
4
5
2
2
3
1
4
4
4
5
5
5
5
2
5
5
5
5
4
5
5
4
5
5
3
1
3
2
4
4
4
2
3
3
5
1
3
3
5
4
5
3
4
2
4
5
2
3
4
5
3
4
3
4
5
4
4
5
2
2
4
4
5
5
3
4
4
1
5
3
5
5
2
1
5
4
5
4
4
4
1
5
2
4
4
5
