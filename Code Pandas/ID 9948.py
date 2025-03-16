>.<

Title: Find the Olympic game which had the highest number of participants that didn't earn a medal
Link: https://platform.stratascratch.com/coding/9948-find-the-olympic-game-which-had-the-highest-number-of-participants-that-didnt-earn-a-medal?code_type=2
Level: Easy

Find the Olympic game which had the highest number of participants that didn't earn a medal.
Output the Olympic game name along with the corresponding number of athletes.
Olympic game name consists of the year and the season.

Data olympics_athletes_events:
age: double
city: text
event: text
games: text
height: double
id: bigint
medal: text
name: text
noc: text
season: text
sex: text
sport: text
team: text
weight: double
year: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

olympic = pd.DataFrame(olympics_athletes_events)

olympic_not_null = olympic[olympic['medal'].isnull()]

olympic_group = olympic_not_null.groupby('games').agg(year=('year','first'),season=('season','first'),total_games_no_medal=('games','count')).reset_index()

olympic_sort = olympic_group.sort_values(by='total_games_no_medal',ascending=False).head(1)
    
Output:

games            |  year  |  season  |  total_games_no_medal
1924 Summer        1924      Summer              97
