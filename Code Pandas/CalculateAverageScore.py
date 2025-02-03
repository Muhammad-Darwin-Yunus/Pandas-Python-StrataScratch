>.<

Title: Calculate Average Score
Link: https://platform.stratascratch.com/coding/10540-calculate-average-score?code_type=2
Level: Easy

Calculate the average score for each project, but only include projects where more than one team member has provided a score.
Your output should include the project ID and the calculated average score for each qualifying project.

Data project_data:
project_id: int
team_member_id: int
score: int
date: datetime

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

group_data = project_data.groupby('project_id').agg(team_count=('team_member_id','nunique'),average_score=('score','mean'))

filter_data = group_data[group_data['team_count']>1]
filter_data = filter_data.reset_index()

filter_data[['project_id', 'average_score']]

Output:

project_id | average_score
101            5.33
102            3
103            56.82
104            5.46
105            14.25
