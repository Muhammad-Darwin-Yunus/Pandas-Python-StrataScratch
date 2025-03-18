>.<

Title: Find Olympic Events Based On Height
Link: https://platform.stratascratch.com/coding/9938-find-olympic-events-based-on-height?code_type=2
Level: Easy

Find events of any Winter Olympics in which there were athletes of height between 180 to 210 centimeters.
Output unique events only.

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

olympic_season = olympic[olympic['season']=='Winter']

olympic_height = olympic_season[(olympic_season['height']>180) & (olympic_season['height']<210)].drop_duplicates()

olympic_height['event']
    
Output:

event
Speed Skating Women's 500 metres
Speed Skating Women's 1000 metres
Alpine Skiing Men's Combined
Alpine Skiing Men's Downhill
Alpine Skiing Men's Super G
