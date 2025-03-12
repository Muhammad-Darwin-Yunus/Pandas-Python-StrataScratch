>.<

Title: Top 10 QBs
Link: https://platform.stratascratch.com/coding/9963-top-10-qbs?code_type=2
Level: Easy

Find the top quarterbacks with the most points in a single game in 2016.
Rank them in such a way where ties in game points are assigned the same rank.
Ensure the output includes all quarterbacks ranked in the top 10, even if ties result in more than 10 records.
Display the quarterback and their game points, ordered by rank.

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

qb_year = qb[qb['year']==2016]

qb_year['top_rank'] = qb_year['game_points'].rank(method='max',ascending=False)

top_qb = qb_year[qb_year['top_rank']<=10]

top_qb_rank = top_qb[['qb','game_points','top_rank']].sort_values(by='top_rank')
    
Output:

qb                      |  game_points  |  top_rank
Drew BreesD. Brees            49              1
Matt RyanM. Ryan              48              3
Drew BreesD. Brees            48              3
Marcus MariotaM. Mariota      47              4
Cam NewtonC. Newton            46              5
Matt RyanM. Ryan              45              7
Tyrod TaylorT. Taylor          45              7
Carson PalmerC. Palmer        44              8
