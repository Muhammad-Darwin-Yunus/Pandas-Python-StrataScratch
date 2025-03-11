>.<

Title: QBs With Most Interceptions
Link: https://platform.stratascratch.com/coding/9969-qbs-with-most-interceptions?code_type=2
Level: Easy

Use the sorting to recognize quarterbacks with the most interceptions in 2016.
Output the quarterbacks along with the corresponding number of interceptions.
Sort records by the interceptions in descending order.

Data qbstats_2015_2016:
att: bigint
cmp: bigint
game_points: bigint
home_away: text
int: bigint
lg: text
loss: bigint
qb: text
rate: double
sack: bigint
td: bigint
yds: bigint
year: bigint
ypa: double

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

qbs = pd.DataFrame(qbstats_2015_2016)

qbs_year = qbs[qbs['year']==2016]

qbs_sort = qbs_year.sort_values(by='int',ascending=False).head(2)

qbs_sort[['qb','int']]

qbs_final = pd.DataFrame({'qb':qbs_sort['qb'],'most_interceptions':qbs_sort['int']})
    
Output:

qb                        |  most_interceptions
Philip RiversP. Rivers            4
Carson PalmerC. Palmer            4
