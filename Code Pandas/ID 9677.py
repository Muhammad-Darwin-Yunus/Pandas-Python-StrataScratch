>.<

Title: Count the number of cancelled flights by American Airlines (AA).
Link: https://platform.stratascratch.com/coding/9677-count-the-number-of-cancelled-flights-by-american-airlines-aa?code_type=2
Level: Easy

Count the number of cancelled flights by American Airlines (AA).

Data us_flights:
flight_date: datetime
unique_carrier: text
flight_num: bigint
origin: text
dest: text
arr_delay: double
cancelled: bigint
distance: double
carier_delay: double
weather_delay: double
late_aircraft_delay: double
nas_delay: double
security_delay: double
actual_elapsed_time: double

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

us_flights = pd.DataFrame(us_flights)

us_flights_carrier = us_flights[us_flights['unique_carrier']=='AA']

us_flights_carrier = us_flights_carrier.groupby('unique_carrier')['cancelled'].count().reset_index()

us_flights_carrier.rename(columns={'cancelled':'number_of_cancelled_flights'})
    
Output:

unique_carrier  |  number_of_cancelled_flights
AA                          12
