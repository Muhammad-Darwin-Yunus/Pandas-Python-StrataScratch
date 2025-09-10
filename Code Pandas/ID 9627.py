>.<

Title: 3 Bed Minimum
Link: https://platform.stratascratch.com/coding/9627-3-bed-minimum?code_type=2
Level: Easy

Find the average number of beds in each neighborhood that has at least 3 beds in total.
Output results along with the neighborhood name and sort the results based on the number of average beds in descending order.

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

airbnb_search_details_neighbourhood = airbnb_search_details.groupby('neighbourhood')['beds'].mean().reset_index(name='avg_beds')

airbnb_search_details_beds = airbnb_search_details_neighbourhood[airbnb_search_details_neighbourhood['avg_beds']>3]

airbnb_search_details_beds[['avg_beds','neighbourhood']]
    
Output:

avg_beds  |  neighbourhood
3.33        Long Beach
4            Rancho Palos Verdes
4            Temple City
3.33        Astoria
4            The Rockaways
5            Windsor Terrace
4            Manhattan Beach
3.17        Westlake
6            Pacific Palisades
5            Hayes Valley
4            Hell's Kitchen
5            Redondo Beach
