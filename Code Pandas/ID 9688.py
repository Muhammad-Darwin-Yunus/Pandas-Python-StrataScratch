>.<

Title: Churro Activity Date
Link: https://platform.stratascratch.com/coding/9688-churro-activity-date?code_type=2
Level: Easy

Find the inspection date and risk category (pe_description) of facilities named 'STREET CHURROS' that received a score below 95.

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

los_angeles_restaurant = los_angeles_restaurant[(los_angeles_restaurant['facility_name']=='STREET CHURROS') & (los_angeles_restaurant['score']<95)]

los_angeles_restaurant[['activity_date','pe_description']]
    
Output:

activity_date        |  pe_description
2017-12-29 00:00:00    RESTAURANT (0-30) SEATS LOW RISK
2016-12-01 00:00:00    RESTAURANT (0-30) SEATS LOW RISK
2016-06-16 00:00:00    RESTAURANT (0-30) SEATS LOW RISK
