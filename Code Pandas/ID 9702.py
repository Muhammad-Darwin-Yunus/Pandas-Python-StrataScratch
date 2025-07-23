>.<

Title: Number Of Unique Facilities And Inspections Per Municipality
Link: https://platform.stratascratch.com/coding/9702-number-of-unique-facilities-and-inspections-per-municipality?code_type=2
Level: Easy

Count the number of unique facilities per municipality zip code along with the number of inspections.
Output the result along with the number of inspections per each municipality zip code.
Sort the result based on the number of inspections in descending order.

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

los_angeles_facility = los_angeles.groupby('facility_zip')['facility_zip'].count().reset_index(name='total_zip')

los_angeles_sort = los_angeles_facility.sort_values('total_zip',ascending=False)
    
Output:

facility_zip  |  total_zip
90045              21
90028              15
90012              14
90027              14
90064              13
90026              10
90046              9
90004              9
90025              8
90024              8
90011              7
90063              7
90065              7
90020              6
90017              6
90042              6
90019              5
90005              5
90015              5
90001              5
90043              5
90007              5
90044              5
90006              5
90022              5
90049              4
90036              4
90066              4
90071              4
90057              4
90038              4
90062              4
90002              3
90048              3
90058              3
90003              3
90023              3
90039              3
90035              3
90018              3
90033              3
90032              3
90016              2
90067              2
90089              2
90031              2
90014              2
90029              2
90013              2
90008-1821          1
90063-3144          1
90037              1
90061              1
90003-1844          1
90034              1
90022-4032          1
90044-3425          1
90015-3315          1
90041              1
90011-1432          1
90291              1
90028-7160          1
90069              1
90025-6229          1
90033-3006          1
90012-4296          1
90048-3402          1
90058-2008          1
90061-2521          1
90033-3412          1
90040                1
