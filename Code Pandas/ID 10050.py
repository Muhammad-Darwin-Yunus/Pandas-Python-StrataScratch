>.<

Title: Find the review count for one-star businesses from yelp
Link: https://platform.stratascratch.com/coding/10050-find-the-review-count-for-one-star-businesses-from-yelp?code_type=2
Level: Easy

Find the review count for one-star businesses from yelp.
Output the name along with the corresponding review count.

Data yelp_business:
address: text
business_id: text
categories: text
city: text
is_open: bigint
latitude: double
longitude: double
name: text
neighborhood: text
postal_code: text
review_count: bigint
stars: double
state: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

one_star = pd.DataFrame(yelp_business)

one_star_yelp = one_star[one_star['stars']==1]

one_star_count = one_star_yelp.groupby('name')['review_count'].sum().reset_index()

Output:

name                              |  review_count
All Colors Mobile Bumper Repair            4
Dry Clean Vegas                            4
The Cuyahoga Room                          3
