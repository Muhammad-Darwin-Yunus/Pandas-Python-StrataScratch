>.<

Title: London Olympic Swimmers
Link: https://platform.stratascratch.com/coding/9934-london-olympic-swimmers?code_type=2
Level: Easy

Find the athletes who competed in swimming events at the London Olympics.

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

olympic_city = olympic[(olympic['city']=='London') & (olympic['sport']=='Swimming')]

olympic_city['name']
    
Output:

name
Leslie George Rich
Samuel Sam Blatherwick
Jeong Won-Yong
Theodora Drakou
Samuel Sam Blatherwick
Leslie George Rich
Samuel Sam Blatherwick
