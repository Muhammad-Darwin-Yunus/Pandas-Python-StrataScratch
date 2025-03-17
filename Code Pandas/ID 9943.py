>.<

Title: Olympics Events List By Age
Link: https://platform.stratascratch.com/coding/9943-winter-olympics-events-list-by-height?code_type=2
Level: Easy

Find the lowest, average, and the highest ages of athletes across all Olympics.
HINT: If athlete participated in more than one discipline at one Olympic games, consider it as a separate athlete, no need to remove such edge cases.

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

olympic_not_null = olympic[olympic['age'].notnull()]

min_age = olympic_not_null['age'].min()
avg_age = round(olympic_not_null['age'].mean())
max_age = olympic_not_null['age'].max()

filtered_olimpic = olympic_not_null[
    (olympic_not_null['age'] == min_age) |
    (olympic_not_null['age'] == avg_age) |
    (olympic_not_null['age'] == max_age)]
    
sort_olympic = filtered_olimpic.sort_values(by='age',ascending=True)

sort_olympic[['name','age']]
    
Output:

name                                      |  age
Victor Jacquemin                              16
Georg Frederik Ahrensborg Clausen              28
Edward D'Arcy McCrea                          28
Charles Umbs                                  28
Jzef Ignacy Kaua                              28
Julius Lenhart                                28
Alfred Edward Flaxman                          28
Franois Jacques Florentin Lafortune            28
Viljo Eino Ville Ritola (Koukkari-)            28
Jan Janssen                                    28
Victoria Thornley                              28
Mohamed Karim Moe Sbihi                        28
Isabel Kerschowski                            28
Anne Marie Carl-Nielsen (Brodersen-)          73
