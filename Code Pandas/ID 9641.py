>.<

Title: Find the number of users that have done a search
Link: https://platform.stratascratch.com/coding/9641-find-the-number-of-users-that-have-done-a-search?code_type=2
Level: Easy

How many unique users have performed a search?

Data airbnb_searches:
ds: date
id_user: text
ds_checkin: date
ds_checkout: date
n_searches: bigint
n_nights: double
n_guests_min: bigint
n_guests_max: bigint
origin_country: text
filter_price_min: double
filter_price_max: double
filter_room_types: text
filter_neighborhoods: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

airbnb_searches = pd.DataFrame(airbnb_searches)

airbnb_searches_searches = airbnb_searches[airbnb_searches['n_searches']>0]

airbnb_searches_id_user = airbnb_searches_searches['id_user'].nunique()

airbnb_searches_fix = pd.DataFrame({'number_of_users':[airbnb_searches_id_user]})
    
Output:

number_of_users
66
