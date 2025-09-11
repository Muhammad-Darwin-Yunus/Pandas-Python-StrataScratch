>.<

Title: Find all neighborhoods present in this dataset
Link: https://platform.stratascratch.com/coding/9626-find-all-neighborhoods-present-in-this-dataset?code_type=2
Level: Easy

Find all neighbourhoods present in this dataset.

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

airbnb_search_details_neighbourhood = airbnb_search_details['neighbourhood'].drop_duplicates()
    
Output:

neighbourhood
East Harlem
Valley Glen
Richmond District
Williamsburg
Topanga
Hollywood Hills
Long Beach
Rancho Palos Verdes
Malibu
Harbor Gateway
Crown Heights
Temple City
Bedford-Stuyvesant
Harlem
Hollywood
Richmond Hill
Astoria
Westchester/Playa Del Rey
Mid-Wilshire
Mar Vista
Hunts Point
Carroll Gardens
Studio City
Santa Monica
Flushing
Logan Circle
Dorchester
The Rockaways
Windsor Terrace
Bernal Heights
Echo Park
Russian Hill
Westwood
South Boston
Marina Del Rey
Hermosa Beach
East New York
Manhattan Beach
Westlake
Lakeview
Westside
Hawthorne
Gardena
Alphabet City
Pacific Palisades
Sunset Park
Loop
West Hollywood
Lincoln Park
East Village
Hayes Valley
Park Slope
Hell's Kitchen
Mount Washington
Mission District
Canoga Park
Redondo Beach
Burbank
Upper East Side
Woodland Hills/Warner Center
Cow Hollow
Reseda
West Los Angeles
Venice
Culver City
