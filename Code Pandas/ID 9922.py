>.<

Title: Highest Checkouts
Link: https://platform.stratascratch.com/coding/9922-highest-checkouts?code_type=2
Level: Easy

Find the number of patrons that have made the highest checkouts up to 10 (excluding 10).
Output the number of patrons along with the corresponding total checkouts.
Sort records based on the total checkouts in descending order.

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

library_group = library.groupby('home_library_definition')['total_checkouts'].sum().reset_index()

library_filter = library_group[library_group['total_checkouts']>10]

library_sort = library_filter.sort_values(by='total_checkouts',ascending=False)
    
Output:

home_library_definition              |  total_checkouts
Eureka Valley/Harvey Milk Memorial            7635
Ortega                                        4255
Portola                                       2902
Main Library                                  2618
Chinatown                                      1475
Parkside                                      1089
Bernal Heights                                980
North Beach                                    885
Glen Park                                      576
Ingleside                                      440
Mission                                        350
Sunset                                        245
Anza                                          184
Richmond                                      177
Excelsior                                      119
Mission Bay                                    100
Merced                                        100
Park                                          98
Visitacion Valley                              54
Western Addition                              25
Marina                                        24
Golden Gate Valley                            20
Noe Valley/Sally Brunn                        19
Potrero                                        11
