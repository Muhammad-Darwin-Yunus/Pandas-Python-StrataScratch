>.<

Title: Find all businesses which have low-risk safety violations
Link: https://platform.stratascratch.com/coding/9717-find-all-businesses-which-have-low-risk-safety-violations?code_type=2
Level: Easy

Find all businesses which have low-risk safety violations.

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

sf_restaurant = pd.DataFrame(sf_restaurant_health_violations)

sf_restaurant_category = sf_restaurant[sf_restaurant['risk_category']=='Low Risk']

sf_restaurant_distinct = sf_restaurant_category.drop_duplicates(subset='business_name')['business_name']
    
Output:

business_name
John Chin Elementary School
SRI THAI CUISINE
Antonelli Brothers Meat, Fish, and Poultry Inc.
STARBUCKS COFFEE CO. #603
Wing Lee BBQ Restaurant
The Castro Republic
Rico Pan
Crepe Cafe
L & G Vietnamese Sandwich
Tacolicious
MANIVANH THAI RESTAURANT
Extreme Pizza
NEW EMMY'S RESTAURANT
Straw
General Nutrition #302
Expressions Snack Bar
In-N-Out Burger
Cafe Broadway
Starbucks Coffee
SAFEWAY STORE #964
Jiang Ling Cuisine Restaurant
Subway 30303
TAQUERIA EL BUEN SABOR
Clay Oven Indian Cuisine
Hong Kong Clay Pot City Restaurant
Great Eastern Restaurant
Golden Kim Tar Restaurant
City Super
Cafe Bean
LA VICTORIA BAKERY
Francisco Middle School
Tanuki Restaurant
ABSINTHE PASTRY
Howard & 6th Street Food Market Inc.
The Good Life Grocery
New Luen Sing Fish Market
Coffee Cultures SOMA
Glaze Teriyaki
Escape From New York Pizza
Wines of California Wine Bar
T & L Liquor Store Inc.
Events Management @ Legion of Honor
Elephant Sushi
SH Dream Inc
MICADO RESTAURANT
Ramzi's Cafe
Cadillac Market
PRESIDIO THEATRE
Restaurante Montecristo
AT&T - COMMISARY KITCHEN [145184]
Old Blue
Akira Japanese Restaurant
Minna SF Group LLC
Subway #36339
Champa Garden
Starbucks
CALIFORNIA PACIFIC MEDICAL CENTER
S & T Hong Kong Seafood
Annie's Hot Dogs & Pretzels
Rock Japanese Cuisine
Juice Craze
Peet's Coffee & Tea
Pho Luen Fat Bakery & Restaurant
Earthbar
Miller's East Coast Deli
Rusty's Southern LLC
Belly Burger
Panuchos
Batter Bakery
Angel Cafe and Deli
Surisan
Starbucks Coffee Co
Chowders
PIZZA HUT #758280
BALBOA HIGH SCHOOL
New Regent Cafe
NORTH BEACH PIZZA
Old Siam Thai Restaurant
Ha Nam Ninh Restaurant
TSING TAO RESTAURANT
LA ALTENA
House of Xian Dumpling
The Lord George
Lollipot
Westfield Food Court Scullery
JAVA ON OCEAN
Burger King 4525
Golden Natural Foods
Hong Kee & Kim
DENMAN MIDDLE SCHOOL
J.B.'S PLACE
David's Deli & Bistro
Cafe Insalata
Fresca Gardens, Inc
24 Hour Fitness Club, #273
California Pizza Kitchen, Inc.
Dip, LLC
Marina Meats Inc.
The Willows
Sutter Pub and Restaurant
Tai Hing Inc.
Pollo Campero
Roxanne Cafe
