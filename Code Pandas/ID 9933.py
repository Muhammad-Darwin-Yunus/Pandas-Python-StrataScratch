>.<

Title: Find all Danish athletes who won a medal
Link: https://platform.stratascratch.com/coding/9933-find-all-danish-athletes-who-won-a-medal?code_type=2
Level: Easy

Find all Danish athletes who won a medal.
Output unique names only.

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

olympic_filter = olympic[(olympic['team']=='Denmark') & (olympic['medal'].notnull())]

olympic_filter['name']
    
Output:

name
Lasse Norman Hansen
