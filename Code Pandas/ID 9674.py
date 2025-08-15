>.<

Title: Find the top 5 longest US flights by distance
Link: https://platform.stratascratch.com/coding/9674-find-the-top-5-longest-us-flights-by-distance?code_type=2
Level: Easy

Find the top 5 longest US flights by distance.
Output the result along with the corresponding origin, destination, and distance.
Sort the flights from longest to shortest.

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

us_flights_sort = us_flights.sort_values('distance',ascending=False)

us_flights_origin = us_flights_sort.drop_duplicates(subset='origin',keep='first').head(5)

us_flights_origin[['origin','dest','distance']]
    
Output:

origin  |  dest  |  distance
SFO        MIA        2585
JFK        SMF        2521
KOA        LAX        2504
OGG        SFO        2338
ORD        LAX        1744
