>.<

Title: Email Preference Missing
Link: https://platform.stratascratch.com/coding/9924-find-libraries-who-havent-provided-the-email-address-in-2016-but-their-notice-preference-definition-is-set-to-email?code_type=2
Level: Easy

Find libraries from the 2016 circulation year that have no email address provided but have their notice preference set to email.
In your solution, output their home library code.

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

library_filter = library[(library['circulation_active_year']==2016) & (library['provided_email_address']==0) & (library['notice_preference_definition']=='email')]

library_filter['home_library_code'].drop_duplicates()
    
Output:

home_library_code
X
R3
P7
E9
