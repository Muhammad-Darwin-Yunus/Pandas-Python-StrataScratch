>.<

Title: Find players who participated in the Olympics representing more than one team
Link: https://platform.stratascratch.com/coding/10143-find-players-who-participated-in-the-olympics-representing-more-than-one-team?code_type=2
Level: Easy

Find players who participated in the Olympics representing more than one team. 
To detect multiple teams please inspect team column and how are multiple teams structured.
Output the player name, team, games, sport, and the medal.

Data olympics_athletes_events:
id: int
name: varchar
sex: varchar
age: float
height: float
weight: float
team varchar
noc: varchar
games: varchar
year: int
season: varchar
city: varchar
sport: varchar
event: varchar
medal: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

team_more_one = pd.DataFrame(olympics_athletes_events)

team_more_one_olympic = team_more_one.fillna(' ')

one_team = team_more_one_olympic.groupby('name').agg(
    teams=('team', lambda x: ','.join(sorted(x))),
    games=('games', lambda x: ','.join(sorted(x))),
    sport=('sport', lambda x: ','.join(sorted(x))),
    medal=('medal', lambda x: ','.join(sorted(x))),
).reset_index()

one_team_len = one_team[one_team['teams'].str.split(',').apply(len)>1]

Output:

name                      |    teams                                                                |        games                                                                |        sport                                                                          |        medal
Albertson Van Zo Post        United States,United States                                                1904 Summer,1904 Summer                                                      Fencing,Fencing                                                                              Gold,Silver
Christine Jacoba Aaftink    Netherlands,Netherlands,Netherlands,Netherlands,Netherlands,Netherlands      1988 Winter,1988 Winter,1992 Winter,1992 Winter,1994 Winter,1994 Winter      Speed Skating,Speed Skating,Speed Skating,Speed Skating,Speed Skating,Speed Skating	
Edward Martin Dahl          Sweden,Sweden                                                                1908 Summer,1908 Summer                                                      Athletics,Athletics	
Leslie George Rich          United States,United States                                                  1908 Summer,1908 Summer                                                      Swimming,Swimming	
Marianne Kjrstad            Norway,Norway                                                                1994 Winter,1994 Winter                                                      Alpine Skiing,Alpine Skiing	
Mario Lertora                Italy,Italy                                                                  1924 Summer,1924 Summer                                                      Gymnastics,Gymnastics	
Ole Kristian Furuseth        Norway,Norway                                                                1992 Winter,1992 Winter                                                      Alpine Skiing,Alpine Skiing	
Pierre Tolar                Luxembourg,Luxembourg                                                        1924 Summer,1924 Summer                                                        Gymnastics,Gymnastics	
Samuel Sam Blatherwick      Great Britain,Great Britain,Great Britain                                    1908 Summer,1908 Summer,1908 Summer                                            Swimming,Swimming,Swimming	
Stane Hlastan                Yugoslavia,Yugoslavia                                                        1924 Summer,1924 Summer                                                      Gymnastics,Gymnastics	
Thomas Hopkins              Great Britain,Great Britain                                                  1924 Summer,1924 Summer                                                      Gymnastics,Gymnastics
