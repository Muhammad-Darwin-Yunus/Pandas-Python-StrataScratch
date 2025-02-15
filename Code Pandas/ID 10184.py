>.<

Title: Order all countries by the year they first participated in the Olympics
Link: https://platform.stratascratch.com/coding/10184-order-all-countries-by-the-year-they-first-participated-in-the-olympics?code_type=2
Level: Easy

Order all countries by the year they first participated in the Olympics.
Output the National Olympics Committee (NOC) name along with the desired year.
Sort records by the year and the NOC in ascending order.

Data olympics_athletes_events:
id: int
name: varchar
sex: varchar
age: float
height: float
weight: float
team: varchar
noc: varchar
games: varchar
year: int
season: varchar
city: varchar
sport: varchar
event: varchar
medal: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

olympics_athletes_events = pd.DataFrame(olympics_athletes_events)

olympics_athletes_events = olympics_athletes_events.groupby('noc').agg(first_participated=('year','min')).reset_index()

olympics_athletes_events_sort = olympics_athletes_events.sort_values(by='noc',ascending=True)

olympics_athletes_events_sort

Output:

noc | first_participated
ARG	1924
AUS	1924
AUT	1904
BEL	1900
BOH	1908
BRA	1924
CAN	1904
CHN	2016
CZE	2016
DEN	1900
ESP	1900
EST	1924
FIJ	2016
FIN	1908
FRA	1900
GBR	1900
GEO	1996
GER	1900
GRE	1900
HAI	1924
HUN	1908
IRL	1924
ISL	1908
ITA	1900
JAM	2016
JPN	1924
KEN	2016
KOR	2012
LAT	1924
LTU	1924
LUX	1924
MEX	1924
NED	1908
NOR	1900
NZL	2016
POL	1924
POR	1924
ROU	1924
RSA	1924
RUS	2016
SRB	2016
SUI	1900
SWE	1900
TCH	1924
URU	1924
USA	1900
YUG	1924
