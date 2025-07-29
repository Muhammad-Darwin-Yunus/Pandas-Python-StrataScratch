>.<

Title: Facility Zip Codes
Link: https://platform.stratascratch.com/coding/9691-facility-zip-codes?code_type=2
Level: Easy

Find all facilities with the zip code 90049, 90034, or 90045.

Data los_angeles_restaurant_health_inspections:
serial_number: text
activity_date: datetime
facility_name: text
score: bigint
grade: text
service_code: bigint
service_description: text
employee_id: text
facility_address: text
facility_city: text
facility_id: text
facility_state: text
facility_zip: text
owner_id: text
owner_name: text
pe_description: text
program_element_pe: bigint
program_name: text
program_status: text
record_id: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code 

los_angeles_restaurant = pd.DataFrame(los_angeles_restaurant_health_inspections)

los_angeles_restaurant_zip = los_angeles_restaurant[los_angeles_restaurant['facility_zip'].isin(['90049','90034','90045'])]['facility_name']
    
Output:

facility_name
VINCENTE FOODS-MARKET
ADMIRALS CLUB
RENAISSANCE 96TH STREET BISTRO
SWEETGREEN
CUSTOM HOTEL
CINEMARK
FLAME BROILER TRBK #80
SOUPLANTATION
99 CENTS ONLY STORE #0375
TAVERN
PHORAGE
STARBUCKS COFFEE
PICK-UP STIX
FOOD AND BOUNTY
UMAMI BURGER
LEMONADE
STARBUCKS EVENING
UMAMI BURGER
ROLLING STONE SPACE 7C
VANILLA BAKESHOP
THE KITCHEN COUNTER
PANDA EXPRESS
CHAYA SUSHI
STARBUCKS COFFEE
CHAYA SUSHI
KLATCH COFFEE
