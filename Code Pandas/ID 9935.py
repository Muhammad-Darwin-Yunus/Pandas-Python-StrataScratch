>.<

Title: Find all events participated by Christine Jacoba Aaftink
Link: https://platform.stratascratch.com/coding/9935-find-all-events-participated-by-christine-jacoba-aaftink?code_type=2
Level: Easy

Find all events participated by Christine Jacoba Aaftink.
Output unique values only.

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

olympic_Aaftink = olympic[olympic['name']=='Christine Jacoba Aaftink']

olympic_Aaftink['event'].drop_duplicates()
    
Output:

event
Speed Skating Women's 500 metres
Speed Skating Women's 1000 metres
