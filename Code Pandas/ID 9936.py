>.<

Title: Find all minors that participated in Olympics games
Link: https://platform.stratascratch.com/coding/9936-find-all-minors-that-participated-in-olympics-games?code_type=2
Level: Easy

Find all minor that participated in Olympics games.
A player is considered as a minor if he or she is 18 or less years old.
Output the name and age of the player along with participated Olympic games (ex: 1992 Summer).

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

olympic_age = olympic[olympic['age']<=18]

olympic_age[['name','age','games']]
    
Output:

name                              |  age  |  games
Maria Rie Vierdag (-Smit)            18      1924 Summer
Richard Louis Pierre Allemane        18      1900 Summer
John C. Hein                         18      1904 Summer
Victor Jacquemin                      16      1908 Summer
Albert Louis Flix Ayat                17      1900 Summer
Gertrude Caroline Trudy Ederle        18      1924 Summer
Willy Falck Hansen                    18      1924 Summer
Maxime Omer Mathieu Max Omer-Dcugis    17      1900 Summer
Tijana Bogdanovi                      18      2016 Summer
Seda Gurgenovna Tutkhalyan            17      2016 Summer
Kyle Chalmers                        18      2016 Summer
