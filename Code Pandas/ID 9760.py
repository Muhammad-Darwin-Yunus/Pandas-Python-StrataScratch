>.<

Title: Find the number of people on Airbnb
Link: https://platform.stratascratch.com/coding/9760-find-the-number-of-searches-on-airbnb?code_type=2
Level: Easy

Find the number of people that made a search on Airbnb.

Data airbnb_searches:
ds: datetime
id_user: text
ds_checkin: datetime
ds_checkout: datetime
n_searches: bigint
n_nights: double
n_guests_min: bigint
n_guests_max: bigint
origin_country: text
filter_price_min: double
filter_price_max: double
filter_room_types:text
filter_neighborhoods: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

airbnb = pd.DataFrame(airbnb_searches)

airbnb_searches = airbnb['n_searches'].sum()

airbnb_name = pd.DataFrame({'total_search_airbnb':[airbnb_searches]})
    
Output:

total_search_airbnb
2893
