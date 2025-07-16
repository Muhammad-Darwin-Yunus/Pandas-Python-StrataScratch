>.<

Title: Find all businesses which have a phone number listed
Link: https://platform.stratascratch.com/coding/9718-find-all-businesses-which-have-a-phone-number-listed?code_type=2
Level: Easy

Find all businesses which have a phone number.

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

sf_notnull = sf_restaurant_health[sf_restaurant_health['business_phone_number'].notnull()]

sf_distinct = sf_notnull.drop_duplicates(subset='business_name')

sf_distinct['business_name']
    
Output:

business_name
Antonelli Brothers Meat, Fish, and Poultry Inc.
The Castro Republic
SAFEWAY STORE #964
Dolores Park Outpost
L & G Vietnamese Sandwich
Allstars Cafe Inc
Peet's Coffee & Tea
Sharetea
Boss Supermarket
NEW EMMY'S RESTAURANT
Live Oak School
Castro Street Chevron
Golden Wok
Expressions Snack Bar
Taqueria Dos Charros
SUBWAY #31419
TAQUERIA EL BUEN SABOR
Clay Oven Indian Cuisine
HAMANO SUSHI
MV Taurus
Samiramis Imports
MARTHA & BROS. COFFEE CO
LA VICTORIA BAKERY
JIM'S RESTAURANT
Glaze Teriyaki
EL POLLO SUPREMO
Buckhorn Grill
Hook a Cook
SH Dream Inc
Jersey
Cecilia's Pizza & Restaurant
Crepe and Brioche, Inc.
Mi Yucatan
Fresca Gardens, Inc
AT&T - COMMISARY KITCHEN [145184]
Subway #36339
Champa Garden
Starbucks
Pectopah LLC
The Salvation Army
Harvest Urban Market
Del Popolo LLC
Bubble Cafe
Rock Japanese Cuisine
LOS PANCHOS
Juice Craze
Gateway High/Kip Schools
Urban Putt
Bebebar Juice & Sandwich
Cream
CHA-AM RESTAURANT
AK SUBS
BALBOA HIGH SCHOOL
Park Gyros Castro
SF BAGEL CO. (KATZ BAGELS)
Thai Cottage Restaurant
GOLDEN PRODUCE
NORTH BEACH PIZZA
Project Juice
India Clay Oven Restaurant and Bar
Brendas Meat & Three
LA ALTENA
BLOWFISH SUSHI
Lollipot
Westfield Food Court Scullery
JAVA ON OCEAN
Chez Julien
Burger King 4525
Mixt Greens
DENMAN MIDDLE SCHOOL
Quickly
California Pizza Kitchen, Inc.
Tai Hing Inc.
Pollo Campero
