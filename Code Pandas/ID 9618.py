>.<

Title: Find searches for Los Angeles neighborhoods
Link: https://platform.stratascratch.com/coding/9618-find-distinct-searches-for-los-angeles-neighborhoods?code_type=2
Level: Easy

Find distinct searches for Los Angeles neighborhoods.
Output neighborhoods and remove duplicates.

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

airbnb_search_details_filter = airbnb_search_details[(airbnb_search_details['city'] == 'LA') & (airbnb_search_details['neighbourhood'].notnull())]['neighbourhood']
    
Output:

neighbourhood
Valley Glen
Topanga
Hollywood Hills
Long Beach
Rancho Palos Verdes
Malibu
Harbor Gateway
Topanga
Temple City
Hollywood
Westchester/Playa Del Rey
Mid-Wilshire
Mar Vista
Studio City
Santa Monica
Studio City
Topanga
Long Beach
Long Beach
Mid-Wilshire
Echo Park
Westwood
Marina Del Rey
Malibu
Hermosa Beach
Manhattan Beach
Westlake
Westlake
Westlake
Westlake
Westside
Hawthorne
Gardena
Pacific Palisades
West Hollywood
Echo Park
Mount Washington
Canoga Park
Redondo Beach
Westlake
Burbank
Woodland Hills/Warner Center
Reseda
Westlake
West Los Angeles
Venice
Culver City
Mid-Wilshire
