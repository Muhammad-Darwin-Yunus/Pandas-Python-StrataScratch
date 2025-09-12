>.<

Title: Cheapest Properties
Link: https://platform.stratascratch.com/coding/9625-cheapest-properties?code_type=2
Level: Easy

Find the price of the cheapest property for every city.

Data airbnb_search_details:
id: bigint
price: double
property_type: text
room_type: text
amenities: text
accommodates: bigint
bathrooms: bigint
bed_type: text
cancellation_policy: text
cleaning_fee: tinyint
city: text
host_identity_verified: text
host_response_rate: text
host_since: date
neighbourhood: text
number_of_reviews: bigint
review_scores_rating: double
zipcode: bigint
bedrooms: bigint
beds: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

airbnb_search_details = pd.DataFrame(airbnb_search_details)

airbnb_search_details_city = airbnb_search_details.groupby('city')['price'].min().reset_index(name='cheapest_property')
    
Output:

city    |  cheapest_property
NYC          340.12
LA          270.81
SF          424.85
DC          417.44
Boston      385.01
Chicago     487.52
