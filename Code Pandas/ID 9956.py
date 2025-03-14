>.<

Title: Find Olympics games that the youngest and the oldest athletes participated in the history of Olympics
Link: https://platform.stratascratch.com/coding/9956-find-olympics-games-that-the-youngest-and-the-oldest-athletes-participated-in-the-history-of-olympics?code_type=2
Level: Easy

Find Olympics games that the youngest and the oldest athletes participated in the history of Olympics.
Output all the details corresponding to each record.

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

young_olympic = olympic[olympic['age'].notnull()]['age'].min()
oldest_olympic = olympic[olympic['age'].notnull()]['age'].max()

oldest_olympic_fix = olympic[(olympic['age']== young_olympic) | (olympic['age']==oldest_olympic)][['event','age']]
    
Output:

event                                            |  age
Athletics Men's 100 metres                          16
Art Competitions Mixed Sculpturing Unknown Event    73
