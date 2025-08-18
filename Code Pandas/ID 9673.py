>.<

Title: Find unique IATA codes
Link: https://platform.stratascratch.com/coding/9673-find-unique-iata-codes?code_type=2
Level: Easy

What are the unique airport codes for all origin airports in the dataset? (e.g., LAX, JFK, SFO)

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

us_flights_origin = us_flights['origin'].drop_duplicates()
    
Output:

origin
ORD
CLE
LGA
ATL
PBI
MSP
JFK
FLL
SFO
DEN
BDL
STL
BOS
OGG
RSW
DFW
AUS
CVG
LAS
HOU
PSP
MDW
LGB
ABQ
BWI
SAN
DCA
MKE
DAL
CID
PLN
GPT
SDF
CAK
SAT
LAN
BNA
OAK
SJU
SYR
BHM
PHX
LAX
BTR
ASE
SNA
CHA
JAX
KOA
FSD
PHL
TUS
RDU
BUR
RNO
