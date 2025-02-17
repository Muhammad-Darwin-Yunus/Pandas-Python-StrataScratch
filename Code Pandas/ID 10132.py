>.<

Title: Highest Crime Rate
Link: https://platform.stratascratch.com/coding/10132-highest-crime-rate?code_type=2
Level: Easy

Find the number of crime occurrences for each day of the week.
Output the day alongside the corresponding crime count.

Data sf_crime_incidents_2014_01:
incidnt_num: float
category: varchar
descript: varchar
day_of_week: varchar
date: datetime
time: datetime
pd_district: varchar
resolution: varchar
address: varchar
lon: float
lat: float
location: varchar
id: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

highest_crime = pd.DataFrame(sf_crime_incidents_2014_01)

highest_crime = highest_crime.groupby('day_of_week')['date'].count().reset_index()

highest_crime = pd.DataFrame({'day_of_week':highest_crime['day_of_week'],'total_crime':highest_crime['date']})

Output:

day_of_week  |  total_crime
Monday              14
Thursday            16
Saturday            18
Tuesday              12
Wednesday            19
Friday                12
Sunday                9
