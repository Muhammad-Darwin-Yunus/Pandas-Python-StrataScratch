>.<

Title: Find neighborhoods that have properties with a parking space and no cleaning fees
Link: https://platform.stratascratch.com/coding/9631-find-neighborhoods-that-have-properties-with-a-parking-space-and-no-cleaning-fees?code_type=2
Level: Easy

Find all neighborhoods that have properties with a parking space and don't charge for cleaning fees.

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

airbnb_search_details_filter = airbnb_search_details[(airbnb_search_details['cleaning_fee']==0) & (airbnb_search_details['amenities'].str.contains('Parking',case=False,na=False)) & (airbnb_search_details['neighbourhood'].notnull())]

airbnb_search_details_drop_dupli = airbnb_search_details_filter['neighbourhood'].drop_duplicates()
    
Output:

neighbourhood
Santa Monica
Studio City
Long Beach
Harlem
Mount Washington
Westlake
Williamsburg
Reseda
Culver City
