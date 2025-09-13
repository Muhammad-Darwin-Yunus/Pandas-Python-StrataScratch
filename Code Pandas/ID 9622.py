>.<

Title: Number Of Bathrooms And Bedrooms
Link: https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=2
Level: Easy

Find the average number of bathrooms and bedrooms for each city’s property types.
Output the result along with the city name and the property type.

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

airbnb_search_details_property_type_city = airbnb_search_details.groupby(['property_type','city'])[['bathrooms','bedrooms']].mean().reset_index().rename(index=str,columns={'bathrooms':'n_bathrooms_avg','bedrooms':'n_bedrooms_avg'})

airbnb_search_details_property_type_city[['city','property_type','n_bathrooms_avg','n_bedrooms_avg']]
    
Output:

city  |  property_type  |  n_bathrooms_avg  |  n_bedrooms_avg
NYC      Apartment            1.12                1.25
LA        Cabin                3                    1
SF        House                1.4                1.8
LA        Villa                2.07                2.53
LA        House                1.5                1.56
NYC       House                1.4                1.8
LA        Apartment            1.14                1.14
LA        Condominium          1.5                1.5
DC        House                  1                  1
Boston    House                  1                  1
LA        Other                  1                  1
Boston    Condominium            2                  2
Boston    Apartment              1                  1
Chicago    Condominium          2                  2
NYC        Condominium          1                  1.33
NYC        Townhouse            1                  0
LA        Loft                  1                  0
Chicago    Apartment            2                  2
Chicago    House                2                  3
NYC        Loft                  1                  0.5
SF        Apartment              1                  2
LA        Townhouse              2                  3
LA        Bungalow              1                    0
