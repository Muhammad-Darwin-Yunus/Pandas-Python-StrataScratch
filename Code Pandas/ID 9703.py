>.<

Title: Find the most common grade earned by bakeries
Link: https://platform.stratascratch.com/coding/9703-find-the-most-common-grade-earned-by-bakeries?code_type=2
Level: Easy

Find the most common grade earned by bakeries.

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

los_angeles_bakery = los_angeles[los_angeles['program_name'].str.contains('bakery',case=False,na=False)]

los_angeles_grade = los_angeles_bakery.groupby('grade')['grade'].count().reset_index(name='total_grade')
    
Output:

grade  |  total_grade
A              9
C              1
B              1
