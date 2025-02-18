>.<

Title: Find the total number of searches for houses Westlake neighborhood with a TV
Link: https://platform.stratascratch.com/coding/10122-find-the-total-number-of-searches-for-houses-westlake-neighborhood-with-a-tv?code_type=2
Level: Easy

Find the total number of searches for houses in Westlake neighborhood with a TV among the amenities.

Data airbnb_search_details:
id: int
price: float
property_type: varchar
room_type: varchar
amenities: varchar
accommodates: int
bathrooms: int
bed_type: varchar
cancellation_policy: varchar
cleaning_fee: bool
city: varchar
host_identity_verified: varchar
host_response_rate: varchar
host_since: datetime
neighbourhood: varchar
number_of_reviews: int
review_scores_rating: float
zipcode: int
bedrooms: int
beds: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

westlake_neighborhood = pd.DataFrame(airbnb_search_details)

westlake_neighborhood = westlake_neighborhood[(westlake_neighborhood['property_type']=='House') & (westlake_neighborhood['neighbourhood']=='Westlake') & (westlake_neighborhood['amenities'].str.contains('tv',case=False))]

westlake_neighborhood_count = westlake_neighborhood.shape[0]

westlake_neighborhood_new = pd.DataFrame({
    'total_number_of_searches_for_houses': [westlake_neighborhood_count]
})

Output:

total_number_of_searches_for_houses
6
