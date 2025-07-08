>.<

Title: Find All Inspections Made On Restaurants
Link: https://platform.stratascratch.com/coding/9721-find-all-inspections-made-on-restaurants?code_type=2
Level: Easy

Find all inspections made on restaurants and output the business name and the inspection score.
For this question business is considered as a restaurant if it contains string "restaurant" inside its name.

Data sf_restaurant_health_violations:
business_id: bigint
business_name: text
business_address: text
business_city: text
business_state: text
business_postal_code: double
business_latitude: double
business_longitude: double
business_location: text
business_phone_number: double
inspection_id: text
inspection_date: datetime
inspection_score: double
inspection_type: text
violation_id: text
violation_description: text
risk_category: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sf_restaurant_health = pd.DataFrame(sf_restaurant_health_violations)

sf_restaurant_health_filter = sf_restaurant_health[sf_restaurant_health['business_name'].str.contains('restaurant',case=False,na=False)]

sf_restaurant_health_filter[['business_name','inspection_score']]
    
Output:

business_name                                    |  inspection_score
Sutter Pub and Restaurant                                  88
Washington Bakery & Restaurant                            67
Brothers Restaurant                                        79
Jiang Ling Cuisine Restaurant                              72
Wing Lee BBQ Restaurant                                    78
MANIVANH THAI RESTAURANT                                  85
NEW EMMY'S RESTAURANT	
SAKANA BUNE RESTAURANT                                    83
Jiang Ling Cuisine Restaurant                              74
Chinatown Restaurant                                      76
Hong Kong Clay Pot City Restaurant                        77
Great Eastern Restaurant                                  83
Golden Kim Tar Restaurant                                  68
Tanuki Restaurant                                          94
JIM'S RESTAURANT	
PEKING WOK RESTAURANT                                      85
Soo Fong Restaurant                                        75
Seal Rock Inn Restaurant                                  77
Red Jade Restaurant                                        80
La Quinta Restaurant	
Cecilia's Pizza & Restaurant                               86
MICADO RESTAURANT                                          88
Restaurante Montecristo                                    81
Akira Japanese Restaurant                                  90
Pho Luen Fat Bakery & Restaurant                           79
CHA-AM RESTAURANT                                          83
Castagnola's Restaurant                                    83
Thai Cottage Restaurant	
India Clay Oven Restaurant and Bar	
Old Siam Thai Restaurant                                    84
Ha Nam Ninh Restaurant                                      71
TSING TAO RESTAURANT                                        78
WING HING RESTAURANT                                        70
CLEMENT BBQ RESTAURANT                                      71
MONGKOK DIM SUM & RESTAURANT                                83
Ninki Sushi Bar & Restaurant                                78
Hilton Financial District- Restaurant Seven Fifty            100
Sutter Pub and Restaurant                                    90
