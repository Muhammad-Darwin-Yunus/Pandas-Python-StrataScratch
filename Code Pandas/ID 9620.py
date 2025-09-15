>.<

Title: Find searches with no data for the host_response_rate column
Link: https://platform.stratascratch.com/coding/9620-find-searches-with-no-data-for-the-host_response_rate-column?code_type=2
Level: Easy

Find all search details where data is missing from the host_response_rate column.

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

airbnb_search_details_host = airbnb_search_details[airbnb_search_details['host_response_rate'].isnull()]['id']
    
Output:

id
12497464
19161964
8889145
17840858
13276443
19583726
6390069
21005590
4698479
5059214
10165064
7359527
4902799
18211034
1077375
13041230
20049857
18157879
17666136
2135314
5321584
13121821
19245819
6689195
11157369
533884
3585452
3380585
16073836
20257960
4559312
18385413
