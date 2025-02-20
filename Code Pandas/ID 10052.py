>.<

Title: Find the average number of stars for each state
Link: https://platform.stratascratch.com/coding/10052-find-the-average-number-of-stars-for-each-state?code_type=2
Level: Easy

Find the average number of stars for each state.
Output the state name along with the corresponding average number of stars.

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

stars_state = pd.DataFrame(yelp_business)

avg_stars_state = stars_state.groupby('state')['stars'].mean().reset_index()

avg_stars_state_fix = pd.DataFrame({'state':avg_stars_state['state'],'avg_stars':avg_stars_state['stars']})

Output:

state  |  avg_stars
AZ          3.8
NV          3.25
OH          3.75
ON          3.78
NC          3.29
WI          4.75
IL          5
PA          3.7
BW          4.17
EDH          5
QC          4.33
