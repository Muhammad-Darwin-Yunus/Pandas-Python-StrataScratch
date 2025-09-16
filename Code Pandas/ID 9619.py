>.<

Title: Find the search details for villas and houses with wireless internet access
Link: https://platform.stratascratch.com/coding/9619-find-the-search-details-for-villas-and-houses-with-wireless-internet-access?code_type=2
Level: Easy

Find the search details for villas and houses with wireless internet access.

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

airbnb_search_details_filter = airbnb_search_details[((airbnb_search_details['property_type']=='House') | (airbnb_search_details['property_type']=='Villa')) & (airbnb_search_details['amenities'].str.contains('Wireless Internet',na=False))]['property_type']
    
Output:

property_type
House
Villa
Villa
Villa
Villa
Villa
Villa
Villa
Villa
Villa
Villa
Villa
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
Villa
House
House
House
House
House
House
House
Villa
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
House
Villa
House
House
House
House
House
House
House
House
House
