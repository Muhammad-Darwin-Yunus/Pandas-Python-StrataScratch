>.<

Title: Patrons Who Renewed Books
Link: https://platform.stratascratch.com/coding/9931-patrons-who-renewed-books?code_type=2
Level: Easy

Find the number of patrons who renewed books at least once but less than 10 times in April 2015.
Each row is an unique patron.

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

library_filter = library[(library['total_renewals']>=1) & (library['total_renewals']<=10) & (library['circulation_active_month']=='April') & (library['circulation_active_year']==2015)]

library_filter['patron_type_definition'].drop_duplicates()
    
Output:

patron_type_definition
ADULT
SENIOR
