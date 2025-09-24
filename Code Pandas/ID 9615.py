>.<

Title: Solo Apartment Search
Link: https://platform.stratascratch.com/coding/9615-find-out-search-details-for-apartments-designed-for-a-sole-person-stay?code_type=2
Level: Easy

Find the search details for apartments where the property type is Apartment and the accommodation is suitable for one person.

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

airbnb_search_details_filter = airbnb_search_details[(airbnb_search_details['property_type']=='Apartment') & (airbnb_search_details['accommodates']==1)]['id']
    
Output:

id
5059214
10923708
1077375
13121821
19245819
11157369
12386097
