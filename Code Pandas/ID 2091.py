>.<

Title: Latest Login Date
Link: https://platform.stratascratch.com/coding/2091-latest-login-date?code_type=2
Level: Easy

For each video game player, find the latest date when they logged in.

Data players_logins:
login_date: date
player_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
players_logins = pd.DataFrame(players_logins)

players_logins_group = players_logins.groupby('player_id')['login_date'].max().reset_index(name='latest_date')
    
Output:

player_id  |  latest_date
101            2021-12-19
102            2022-01-15
103            2021-12-23
104            2022-01-14
105            2022-01-10
106            2022-01-26
