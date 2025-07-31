>.<

Title: Inspection For Glassell Coffee Shop
Link: https://platform.stratascratch.com/coding/9689-inspection-for-glassell-coffee-shop?code_type=2
Level: Easy

Find all inspection details made for facilities owned by 'GLASSELL COFFEE SHOP LLC'.

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

los_angeles_restaurant_owner = los_angeles_restaurant[los_angeles_restaurant['owner_name'].str.contains('GLASSELL COFFEE SHOP LLC',na=False)]

los_angeles_restaurant_owner['facility_name']
    
Output:

facility_name
HABITAT COFFEE SHOP
HABITAT COFFEE SHOP
HABITAT COFFEE SHOP
HABITAT COFFEE SHOP
HABITAT COFFEE SHOP
