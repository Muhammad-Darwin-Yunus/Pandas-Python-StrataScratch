>.<

Title: 100 Total Checkouts Libraries
Link: https://platform.stratascratch.com/coding/9923-100-total-checkouts-libraries?code_type=2
Level: Easy

Find the number of libraries that had 100 or more of total checkouts in February 2015.
Be aware that there could be more than one row for certain library on monthly basis.

Data library_usage:
age_range: text
circulation_active_month: text
circulation_active_year: double
home_library_code: text
home_library_definition: text
notice_preference_code: text
notice_preference_definition: text
outside_of_county: tinyint
patron_type_code: bigint
patron_type_definition: text
provided_email_address: tinyint
supervisor_district: double
total_checkouts: bigint
total_renewals: bigint
year_patron_registered: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

library = pd.DataFrame(library_usage)

library_filter = library[(library['circulation_active_year']==2015) & (library['circulation_active_month']=='February')]

library_sum = library_filter.groupby('home_library_definition')['total_checkouts'].sum().reset_index()

library_sum[['home_library_definition','total_checkouts']]
    
Output:

home_library_definition  |  total_checkouts
Mission Bay                      100
Glen Park                        200
Merced                            100
Main Library                      100
