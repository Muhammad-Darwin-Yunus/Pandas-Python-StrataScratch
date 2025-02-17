>.<

Title: Abigail Breslin Nominations
Link: https://platform.stratascratch.com/coding/10128-count-the-number-of-movies-that-abigail-breslin-nominated-for-oscar?code_type=2
Level: Easy

Count the number of movies that Abigail Breslin was nominated for an oscar.

Data oscar_nominees:
year: int
category: varchar
nominee: varchar
movie: varchar
winner: bool
id: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

abigail_breslin = pd.DataFrame(oscar_nominees)

abigail_breslin = abigail_breslin[abigail_breslin['nominee']=='Abigail Breslin']

abigail_breslin_nominee = abigail_breslin.groupby('nominee').agg(nominated_oscar=('nominee','count')).reset_index()

abigail_breslin_nominee

Output:

nominee          |  nominated_oscar
Abigail Breslin        1
