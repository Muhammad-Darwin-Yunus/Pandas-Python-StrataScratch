>.<

Title: Popularity of Hack
Link: https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=2
Level: Easy

Meta/Facebook has developed a new programing language called Hack.To measure the popularity of Hack they ran a survey with their employees.
The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack.
Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. 
Luckily the user IDs of employees completing the surveys were stored.
Based on the above, find the average popularity of the Hack per office location.
Output the location along with the average popularity.

Data facebook_employees:
id: int
location: varchar
age: int
gender: varchar
is_senior: bool

Data facebook_hack_survey:
employee_id: int
age: int
gender: varchar
popularity: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

popularity_hack = pd.merge(facebook_employees,facebook_hack_survey,left_on='id',right_on='employee_id',how='inner')

popularity_hack_of = popularity_hack.groupby('location')['popularity'].mean().reset_index()

Output:

location  |  popularity
USA              4.6
India            7.5
UK                4.33
Switzerland        1
