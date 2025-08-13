>.<

Title: Flights With No Delay
Link: https://platform.stratascratch.com/coding/9675-flights-with-no-delay?code_type=2
Level: Easy

Find all US flight details which had no delay (use only arr_delay column for filtering).

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

us_flights_arr_delay = us_flights[us_flights['arr_delay']==0]['unique_carrier']
    
Output:

unique_carrier
AA
