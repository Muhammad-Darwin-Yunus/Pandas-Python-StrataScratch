>.<

Title: Find all athletes who were older than 40 years when they won either Bronze or Silver medals
Link: https://platform.stratascratch.com/coding/9937-find-all-athletes-who-were-older-than-40-years-when-they-won-either-bronze-or-silver-medals?code_type=2
Level: Easy

Find all athletes who were older than 40 years when they won either Bronze or Silver medals.

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

olympic_not_null = olympic[olympic['medal'].notnull()]

olympic_age = olympic_not_null[olympic_not_null['age']>40]

olympic_medal = olympic_age[(olympic_age['medal']=='Bronze') | (olympic_age['medal']=='Silver')]

olympic_medal[['name','medal']]
    
Output:

name                      |  medal
Gustaf Vilhelm Carlberg      Silver
Emma C. Cooke                Silver
Claude-Lon Mascaux            Bronze
Walter Riggs                  Silver
Matthew John Matt McGrath    Silver
Auguste Serrurier            Silver
