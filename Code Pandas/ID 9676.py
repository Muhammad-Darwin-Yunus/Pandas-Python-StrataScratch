>.<

Title: Find the average distance traveled from each origin airport.
Link: https://platform.stratascratch.com/coding/9676-find-the-average-distance-traveled-from-each-origin-airport?code_type=2
Level: Easy

Find the average distance an airplane travels from each origin airport.
Output the result along with the corresponding origin.

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

us_flights_origin = us_flights.groupby('origin')['distance'].mean().reset_index(name='avg_distance')
    
Output:

origin  |  avg_distance
ORD          1227.2
CLE            404
LGA          426.25
ATL          443.67
PBI          1197
MSP          828.5
JFK          2521
FLL          450
SFO          1526.5
DEN          646.67
BDL          1173
STL            825.2
BOS          1237
OGG          2338
RSW          618.5
DFW          542.12
AUS          876.5
CVG          335
LAS          902.89
HOU          696
PSP          261
MDW          895
LGB          387
ABQ          569
BWI          365
SAN          933
DCA          547
MKE          896
DAL          436
CID          430
PLN          243
GPT          500
SDF          788
CAK          274
SAT          1042.5
LAN          455
BNA          646.5
OAK          517
SJU          1576
SYR          794
BHM          587
PHX          304
LAX          1166.5
BTR          448
ASE          737
SNA          338
CHA          501
JAX          270
KOA          1333.5
FSD          196
PHL          1127
TUS          601
RDU          427
BUR          325
RNO          1671
