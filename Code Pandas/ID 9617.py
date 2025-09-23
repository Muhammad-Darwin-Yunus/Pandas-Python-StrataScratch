>.<

Title: Find all searches for accommodations with an equal number of bedrooms bathrooms
Link: https://platform.stratascratch.com/coding/9617-find-all-searches-for-accommodations-with-an-equal-number-of-bedrooms-bathrooms?code_type=2
Level: Easy

Find all searches for accommodations where the number of bedrooms is equal to the number of bathrooms.

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

airbnb_search_details_bedrooms = airbnb_search_details[airbnb_search_details['bedrooms']==airbnb_search_details['bathrooms']]['accommodates']
    
Output:

accommodates
2
2
8
2
6
10
4
8
2
2
4
1
4
2
2
2
3
4
5
1
2
2
4
2
4
12
2
4
2
1
2
2
2
2
3
4
4
2
2
6
2
5
6
6
4
2
2
4
2
3
2
2
2
2
2
4
2
4
2
4
2
2
2
2
2
1
2
1
3
2
4
4
4
2
2
1
4
2
4
3
1
8
4
2
10
4
1
4
2
2
2
2
1
2
1
2
2
2
4
2
2
2
2
