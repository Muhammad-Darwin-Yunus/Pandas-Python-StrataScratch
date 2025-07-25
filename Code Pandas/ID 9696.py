>.<

Title: Check if record_id is unique for every row
Link: https://platform.stratascratch.com/coding/9696-check-if-record_id-is-unique-for-every-row?code_type=2
Level: Easy

Check if record_id is unique for every row.
Output the total record ids and total unique record ids for comparison.

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

los_angeles_count = los_angeles['record_id'].count()

total_unique_record = los_angeles['record_id'].nunique()

los_angeles_fix = ([{'total_record' : los_angeles_count,'total_unique_record' : total_unique_record}])
    
Output:

total_record  |  total_unique_record
299                    233
