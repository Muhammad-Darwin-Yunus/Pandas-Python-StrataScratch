>.<

Title: Women In The Olympics Before World War 2
Link: https://platform.stratascratch.com/coding/9932-women-in-the-olympics-before-world-war-2?code_type=2
Level: Easy

Find unique names women who participated in an Olympics before World War 2.
Let's consider the year 1939 as the start of WW2.

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

olympic_filter = olympic[(olympic['year']<1939) & (olympic['sex']=='F')].drop_duplicates()

olympic_filter['name']
    
Output:

name
Dora Honnywill (Neve-)
Emma C. Cooke
Sybil Fenton Newall
Maria Rie Vierdag (-Smit)
Rene Brasseur
Marion Hall Jessup (Zinderstein- -MacLure)
Giulia Perelli
Gladys Mary Davis
Hlne de Pourtals (Barbey-)
Gertrude Caroline Trudy Ederle
Hazel Virginia Wightman (Hotchkiss-)
Jeanne Marie Henriette Filleaul-Brohy (Hantjens-)
Leonora Josephine Leonie Taylor
Emily Woodruff (Smiley-)
Inger Nordb (Kragh-)
Catharina Maria Toos van der Klaauw (-Steensma)
Dorothy Brown Locke
Anne Marie Carl-Nielsen (Brodersen-)
