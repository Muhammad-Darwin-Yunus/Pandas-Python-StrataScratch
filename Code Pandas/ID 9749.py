>.<

Title: Find the most dangerous places in SF
Link: https://platform.stratascratch.com/coding/9749-find-the-most-dangerous-place-in-sf?code_type=2
Level: Easy

Find the most dangerous places in SF based on the crime count per address and district combination.
Output the number of incidents alongside the corresponding address and the district.
Order records based on the number of occurrences in descending order.

Data sf_crime_incidents_2014_01:
incidnt_num: double
category: text
descript: text
day_of_week: text
date: datetime
time: timestamp
pd_district: text
resolution: text
address: text
lon: double
lat: double
location: text
id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sf = pd.DataFrame(sf_crime_incidents_2014_01)

sf_crimes = sf.groupby(['address','pd_district']).size().reset_index(name='total_crimes').sort_values('total_crimes',ascending=False)
    
Output:

address  |                                  |  pd_district    |  total_crimes
800 Block of BRYANT ST                          SOUTHERN              4
800 Block of MARKET ST                          SOUTHERN              2
TURK ST / TAYLOR ST                            TENDERLOIN            2
0 Block of 6TH ST                               SOUTHERN              1
200 Block of WHITNEY ST                        INGLESIDE              1
7TH ST / HOWARD ST                              SOUTHERN              1
RITCH ST / TOWNSEND ST                          SOUTHERN                1
700 Block of VANNESS AV                        NORTHERN                1
2300 Block of 3RD ST                            BAYVIEW                1
3RD ST / BRANNAN ST                            SOUTHERN                 1
600 Block of EDDY ST                            NORTHERN	              1
100 Block of TIFFANY AV                        INGLESIDE                1
900 Block of BAY SHORE BL                      BAYVIEW                  1
100 Block of 3RD ST                            SOUTHERN                  1
800 Block of PACHECO ST                        TARAVAL	                1
1900 Block of BEACH ST                          NORTHERN	                1
2000 Block of MARKET ST                        MISSION	                  1
1100 Block of GOUGH ST                        NORTHERN	                  1
23RD ST / VERMONT ST                          MISSION                    	1
TAYLOR ST / OFARRELL ST                        TENDERLOIN                	1
MARTIN LUTHER KING JR DR / 7TH AV              RICHMOND	                  1
1000 Block of GEARY ST                        NORTHERN	                  1
1000 Block of POLK ST                          NORTHERN	                  1
500 Block of GREEN ST                          CENTRAL	                  1
1100 Block of VANNESS AV                      NORTHERN	                  1
0 Block of SHRADER ST                          PARK	                      1
200 Block of VANNESS AV                        NORTHERN	                  1
1800 Block of VICENTE ST                        TARAVAL	                  1
HYDE ST / GROVE ST                              TENDERLOIN	              1
1700 Block of VALLEJO ST                        NORTHERN	                1
18TH ST / CASTRO ST                            MISSION	                  1
FELL ST / OCTAVIA ST                          NORTHERN	                  1
HYDE ST / LOMBARD ST                          CENTRAL	                    1
1400 Block of THOMAS AV                      BAYVIEW	                    1
4000 Block of 19TH ST                        MISSION	                    1
100 Block of BLUXOME ST                    SOUTHERN	                      1
18TH ST / OAKWOOD ST                        MISSION                        1
MINNA ST / 11TH ST                          SOUTHERN	                    1
500 Block of PORTOLA DR                      INGLESIDE	                  1
700 Block of POLK ST                        NORTHERN	                    1
4600 Block of 3RD ST                        BAYVIEW	                      1  
VICENTE ST / 37TH AV                        TARAVAL	                      1
100 Block of OFARRELL ST                    TENDERLOIN	                  1
HYDE ST / TURK ST                            TENDERLOIN	                  1
0 Block of JONES ST                          TENDERLOIN	                  1
TURK ST / FRANKLIN ST                        NORTHERN	                    1
1200 Block of FITZGERALD AV                  BAYVIEW	                    1
0 Block of MADISON ST                        INGLESIDE	                  1
2200 Block of BAY SHORE BL                    INGLESIDE	                  1
500 Block of JOHNFKENNEDY DR                  RICHMOND	                  1
800 Block of EDDY ST                          NORTHERN	                  1
0 Block of CHUMASERO DR                        TARAVAL	                  1
35TH AV / IRVING ST                            TARAVAL	                  1
1300 Block of MARKET ST                        SOUTHERN	                  1
SAN JOSE AV / RANDALL ST                      INGLESIDE	                  1
0 Block of FREDERICK ST                          PARK	                    1
1000 Block of BUSH ST                          CENTRAL	                  1
700 Block of NATOMA ST                        SOUTHERN	                  1
100 Block of POWELL ST                        TENDERLOIN	                1
0 Block of PERRY ST                            SOUTHERN	                  1
1100 Block of PALOU AV                        BAYVIEW	                    1
100 Block of ROOSEVELT WY                      PARK	                      1
2700 Block of 24TH ST                          MISSION	                  1
700 Block of GOUGH ST                          NORTHERN	                  1
1600 Block of THE EMBARCADERONORTH ST          CENTRAL	                  1
2300 Block of BAKER ST                          RICHMOND	                1
BOSWORTH ST / DIAMOND ST                        INGLESIDE	                1
500 Block of 9TH ST                              SOUTHERN	                1
FOLSOM ST / THE EMBARCADEROSOUTH ST              SOUTHERN	                1
300 Block of GREENWICH ST                        CENTRAL	                1
0 Block of ONONDAGA AV                          INGLESIDE	                1
1700 Block of MARKET ST                        SOUTHERN	                  1
4400 Block of MISSION ST                        INGLESIDE	                1
0 Block of 1ST ST                              SOUTHERN	                  1
SACRAMENTO ST / VANNESS AV                      NORTHERN	                1
4TH ST / TOWNSEND ST                            SOUTHERN	                1
CALIFORNIA ST / PIERCE ST                        RICHMOND	                1
OAKDALE AV / NEWHALL ST                          BAYVIEW	                1
400 Block of TREAT AV                            MISSION	                1
0 Block of STOCKTON ST                          TENDERLOIN	              1
LINCOLN WY / 24TH AV                              TARAVAL	                1
0 Block of BLUXOME ST                            SOUTHERN	                1
GOLDEN GATE AV / LEAVENWORTH ST                  TENDERLOIN	              1
100 Block of JONES ST                            TENDERLOIN              	1
1900 Block of GEARY BL                              PARK	                1
800 Block of MOSCOW ST                            INGLESIDE	              1
1000 Block of SUTTER ST                            CENTRAL	              1
2800 Block of MISSION ST                          MISSION	                1
300 Block of SUTTER ST                            CENTRAL	                1
4TH ST / HOWARD ST                                SOUTHERN	              1
SUNNYDALE AV / RUTLAND ST                          INGLESIDE	            1
1500 Block of EDDY ST                              NORTHERN              	1
WASHINGTON ST / POLK ST                            NORTHERN	               1
POST ST / AVERY ST                                  NORTHERN	            1
1900 Block of HARRISON ST                            MISSION	              1
