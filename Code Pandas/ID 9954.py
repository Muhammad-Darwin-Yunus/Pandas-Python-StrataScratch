>.<

Title: Find the history of each sport by finding the first year, last year and total times that sport was played in the Olympics
Link: https://platform.stratascratch.com/coding/9954-find-the-history-of-each-sport-by-finding-the-first-year-last-year-and-total-years-that-sport-played-in-the-olympics?code_type=2
Level: Easy

Find the history of each sport by finding the first year, last year, and the total number of occasions that was sport played in the Olympics.
Output the sport name along with the first year, last year, and the total number of occasions.
Order records by the first year in descending order.

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

olympic_group = olympic.groupby('sport').agg(first_year=('year','min'),last_year=('year','max'),total_games=('sport','count')).reset_index()

olympic_sort = olympic_group.sort_values(by='first_year',ascending=False)
    
Output:

sport                    |  first_year  |  last_year  |  total_games
Volleyball                    2016            2016            1
Synchronized Swimming          2016            2016            1
Basketball                      2016            2016            2
Taekwondo                      2016            2016            1
Canoeing                      2016              2016            5
Rugby Sevens                  2016              2016            3
Alpine Skiing                1992              1994            10
Speed Skating                1988              1994              6
Judo                          1984              2008            5
Modern Pentathlon              1924            1924              2
Art Competitions              1924            1936              7
Boxing                        1908            2016              4
Diving                        1908            2016              9
Motorboating                  1908            1908              2
Hockey                        1908            2016              5
Lacrosse                      1904            1908              2
Weightlifting                  1904            2016              3
Wrestling                      1904            1924              12
Swimming                        1900            2016            20
Gymnastics                      1900            2016            40
Cycling                        1900            2016              17
Football                        1900            2016              11
Golf                            1900            2016              7
Fencing                        1900              1936              28
Shooting                        1900            2016              34
Archery                        1900              2016              7
Croquet                        1900              1900              1
Basque Pelota                  1900              1900              1
Equestrianism                  1900              2016              4
Tug-Of-War                      1900              1908              4
Water Polo                      1900              2016              7
Tennis                          1900              1924              14
Athletics                      1900              2016                47
Rugby                          1900              1924                9
Sailing                        1900              2016                10
Rowing                          1900              2016                13
