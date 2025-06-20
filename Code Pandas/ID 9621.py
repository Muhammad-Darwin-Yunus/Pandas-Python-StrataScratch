>.<

Title: Find all searches for San Francisco with a flexible cancellation policy and a review score rating
Link: https://platform.stratascratch.com/coding/9621-find-all-searches-for-san-francisco-with-a-flexible-cancellation-policy-and-a-review-score-rating?code_type=2
Level: Easy

Find all searches for San Francisco with a flexible cancellation policy and a review score rating.
Sort the results by the review score in the descending order.

Data airbnb_search_details:
accommodates: bigint
amenities: text
bathrooms: bigint
bed_type: text
bedrooms: bigint
beds: bigint
cancellation_policy: text
city: text
cleaning_fee: tinyint
host_identity_verified: text
host_response_rate: text
host_since: date
id: bigint
neighbourhood: text
number_of_reviews: bigint
price: double
property_type: text
review_scores_rating: double
room_type: text
zipcode: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

airbnb = pd.DataFrame(airbnb_search_details)

airbnb_filter = airbnb[(airbnb['cancellation_policy']=='flexible') & (airbnb['city']=='SF')].sort_values(by='review_scores_rating',ascending=False)

airbnb_filter['review_scores_rating']
    
Output:

review_scores_rating
100
