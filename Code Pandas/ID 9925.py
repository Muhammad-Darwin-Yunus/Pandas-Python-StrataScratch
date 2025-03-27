>.<

Title: Find how many people registered in libraries in the year 2016
Link: https://platform.stratascratch.com/coding/9925-find-how-many-people-registered-in-libraries-in-the-year-2016?code_type=2
Level: Easy

Find how many people registered in libraries in the year 2016.
Output the total patrons. Keep in mind that each row represents different patron.

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

library_year = library[library['year_patron_registered']==2016].shape[0]

library_year_fix = pd.DataFrame({'total_patrons':[library_year]})

Output:

total_patrons
10
