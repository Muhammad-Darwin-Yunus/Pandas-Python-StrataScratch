>.<

Title: Quarterback Top Ratings
Link: https://platform.stratascratch.com/coding/9962-top-10-qbs?code_type=2
Level: Easy

Identify the top 10 ratings received by quarterbacks.
Your output should include the quarterback's name and their corresponding rating.

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

qb = pd.DataFrame(qbstats_2015_2016)

qb_sort = qb.sort_values(by='rate',ascending=False).head(10)

qb_sort[['qb','rate']]
    
Output:

qb                                    |  rate
Ben RoethlisbergerB. Roethlisberger      155.8
Cam NewtonC. Newton                      153.3
Ben RoethlisbergerB. Roethlisberger      152.5
Aaron RodgersA. Rodgers                  150.8
Marcus MariotaM. Mariota                  149.8
Dak PrescottD. Prescott                  148.3
Marcus MariotaM. Mariota                  148.1
Ben RoethlisbergerB. Roethlisberger        146
Matt RyanM. Ryan                          144.7
Matt RyanM. Ryan                          144.5
