>.<

Title: Count the unique origin airports
Link: https://platform.stratascratch.com/coding/9672-count-the-unique-origin-airports?code_type=2
Level: Easy

Find how many different origin airports exist?

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

us_flights_origin = us_flights['origin'].nunique()

us_flights_fix = pd.DataFrame({'total_unique_origin':[us_flights_origin]})
    
Output:

total_unique_origin
55
