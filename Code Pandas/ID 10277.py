>.<

Title: Find all inspections which are part of an inactive program
Link: https://platform.stratascratch.com/coding/10277-find-all-inspections-which-are-part-of-an-inactive-program?code_type=2
Level: Easy

Find all inspections which are part of an inactive program.

Data los_angeles_restaurant_health_inspections:
serial_number: varchar
activity_date: datetime
facility_name: varchar
score: int
grade: varchar
service_code: int
service_description: varchar
employee_id: varchar
facility_address: varchar
facility_city: varchar
facility_id: varchar
facility_state: varchar
facility_zip: varchar
owner_id: varchar
owner_name: varchar
pe_description: varchar
program_element_pe: int
program_name: varchar
program_status: varchar
record_id: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

los_angeles_restaurant_health_inspections = pd.DataFrame(los_angeles_restaurant_health_inspections)

los_angeles_restaurant_health_inspections = los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['program_status']=='INACTIVE']

los_angeles_restaurant_health_inspections[['program_name','program_status']]

Output:

serial_number | activity_date | facility_name                  | score | program_status
DA2GQRJOS        2017-03-07    LAS MOLENDERAS                      97        INACTIVE
DAQZAULOI        2017-10-11    INTI PERUVIAN RESTAURANT            94        INACTIVE
DA0N7AWN0        2016-09-21    MICHELLE'S DONUT HOUSE              96        INACTIVE
DA2M0ZPRD        2017-01-24    LA PRINCESITA MARKET                95        INACTIVE
DAKIPC9UB        2016-06-16    LA PETITE BOULANGERIE                86        INACTIVE
DAH08SUQB        2016-01-13    CARNITAS URUAPAN - MARKET & BAKERY    92	      INACTIVE
DA0KUBBF6        2015-08-13    ANTOJITOS LISETH                      90        INACTIVE
DAKYQHFDV        2016-08-09    MIKE'S DELI #2                        94        INACTIVE
DAH9FUPBP        2017-01-31    NISSI BAKERY                          90        INACTIVE
DAERHLUYY        2015-07-28    GUI IL BUNJI                          75        INACTIVE
DATERW8EJ        2015-12-11    STK/BAGATELLE                          90        INACTIVE
DA43D5RLO        2017-01-09    HOLLYWOOD ROCK CAFE                    80        INACTIVE
DATKE9ZEY        2016-01-19    MR BOBA                                95        INACTIVE
DAAZEJORN        2015-11-06    FIX COFFEE                            98          INACTIVE
DAL9QKQYF        2016-08-10    POPEYE DUMPLING AND NOODLES            90        INACTIVE
DA6TFCWEK        2017-03-15    LOUIS JUNIOR                            87        INACTIVE
DAHZWAM9W        2015-12-01    EL RINCON DE LAS DELICIAS                95        INACTIVE
DANYAXWN1        2016-02-12    HARRIS MARKET                            97        INACTIVE
DAA0AJ0WC        2016-07-12    STARBUCKS COFFEE                          90        INACTIVE
DAQOADCKZ        2016-01-06    BIBIGO-REMOTE STORAGE                    100        INACTIVE
DA0NJNGFD        2017-08-04    BROOKLYN PIZZA AND PASTA                  72        INACTIVE
DA3YKNNH7        2016-06-20    KAJU UDON                                  86        INACTIVE
DAH0MH5XB        2015-08-31    KAJU UDON                                  73        INACTIVE
DAUH8FDSV        2015-08-06    STARBUCKS COFFEE                            95        INACTIVE
DAIA7KS01        2017-02-28    SLAUSON FISH MARKET                        74          INACTIVE
DAJ6DGZIM        2015-09-10    SILVER LAKE JUICE BAR                      90        INACTIVE
