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

facility_name                      |  program_status
LAS MOLENDERAS                            INACTIVE
INTI PERUVIAN RESTAURANT                  INACTIVE
MICHELLE'S DONUT HOUSE                    INACTIVE
LA PRINCESITA MARKET                      INACTIVE
LA PETITE BOULANGERIE                    INACTIVE
CARNITAS URUAPAN - MARKET & BAKERY        INACTIVE
ANTOJITOS LISETH                          INACTIVE
MIKE'S DELI #2                            INACTIVE
NISSI BAKERY                              INACTIVE
GUI IL BUNJI                              INACTIVE
STK/BAGATELLE                              INACTIVE
HOLLYWOOD ROCK CAFE                        INACTIVE
MR BOBA                                    INACTIVE
FIX COFFEE                                INACTIVE
POPEYE DUMPLING AND NOODLES                INACTIVE
LOUIS JUNIOR                              INACTIVE
EL RINCON DE LAS DELICIAS                  INACTIVE
HARRIS MARKET                              INACTIVE
STARBUCKS COFFEE                          INACTIVE
BIBIGO-REMOTE STORAGE                      INACTIVE
BROOKLYN PIZZA AND PASTA                    INACTIVE
KAJU UDON                                  INACTIVE
KAJU UDON                                  INACTIVE
STARBUCKS COFFEE                           INACTIVE
SLAUSON FISH MARKET                        INACTIVE
SILVER LAKE JUICE BAR                      INACTIVE
