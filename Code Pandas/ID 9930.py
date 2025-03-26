>.<

Title: Find libraries with the highest number of total renewals
Link: https://platform.stratascratch.com/coding/9930-find-libraries-with-the-highest-number-of-total-renewals?code_type=2
Level: Easy

Find libraries with the highest number of total renewals.
Output all home library definitions along with the corresponding total renewals.
Order records by total renewals in descending order.

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

library_filter = library.groupby('home_library_definition')['total_renewals'].sum().reset_index(name='highest_total_renewals')

library_sort = library_filter.sort_values(by='highest_total_renewals',ascending=False).head(2)
    
Output:

home_library_definition            |  highest_total_renewals
Ortega                                        2421
Eureka Valley/Harvey Milk Memorial            2421
