>.<

Title: BAKERY' Owned Facilities
Link: https://platform.stratascratch.com/coding/9697-bakery-owned-facilities?code_type=2
Level: Easy

Find the owner_name and the pe_description of facilities owned by 'BAKERY' where low-risk cases have been reported.

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

los_angeles = pd.DataFrame(los_angeles_restaurant_health_inspections)

los_angeles_owner = los_angeles.drop_duplicates('owner_name')

los_angeles_likes = los_angeles_owner[los_angeles_owner['pe_description'].str.contains('LOW RISK',case=False,na=False) & los_angeles_owner['facility_name'].str.endswith('BAKERY',na=False)]

los_angeles_likes[['owner_name','pe_description']]
    
Output:

owner_name                |  pe_description
DANNY'S BAKERY INC            FOOD MKT RETAIL (25-1,999 SF) LOW RISK
GALDAZA FOOD CORPORATION      FOOD MKT RETAIL (25-1,999 SF) LOW RISK
