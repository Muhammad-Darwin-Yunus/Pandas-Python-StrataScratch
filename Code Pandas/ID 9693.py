>.<

Title: Find the average score for grades A, B, and C
Link: https://platform.stratascratch.com/coding/9693-find-the-average-score-for-grades-a-b-and-c?code_type=2
Level: Easy

Find the average score for grades A, B, and C.
Output the results along with the corresponding grade (ex: 'A', avg(score)).

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

los_angeles_grade = los_angeles.groupby('grade')['score'].mean().reset_index(name='average_score')
    
Output:

grade	average_score
A	94.44
B	83.38
C	73.64
