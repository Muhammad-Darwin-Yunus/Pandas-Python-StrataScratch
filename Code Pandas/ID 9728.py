>.<

Title: Number of violations
Link: https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?code_type=2
Level: Easy

You are given a dataset of health inspections that includes details about violations.
Each row represents an inspection, and if an inspection resulted in a violation, the violation_id column will contain a value.
Count the total number of violations that occurred at 'Roxanne Cafe' for each year, based on the inspection date.
Output the year and the corresponding number of violations in ascending order of the year.

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

sf_restaurant_filter = sf_restaurant[(sf_restaurant['business_name']=='Roxanne Cafe') & (sf_restaurant['violation_id'].notnull())]

sf_restaurant_filter['year'] = sf_restaurant_filter['inspection_date'].dt.year

sf_restaurant_year = sf_restaurant_filter.groupby('year')['violation_id'].size().reset_index(name='total_violation').sort_values('year',ascending=True)
    
Output:

year  |  total_violation
2015          5
2016	        2
2018	        3
