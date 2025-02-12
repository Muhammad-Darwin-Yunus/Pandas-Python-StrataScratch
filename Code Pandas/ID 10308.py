>.<

Title: Salaries Differences 
Link: https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=2
Level: Easy

Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments.
Output just the absolute difference in salaries.

Data db_employee:
id: int
first_name: varchar
last_name: varchar
salary: int
department_id: int

Data db_dept:
id: int
department: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

salaries = pd.merge(db_employee,db_dept,how='left',left_on=['department_id'],right_on=['id'])

marketing = salaries[salaries['department']=='marketing']
salary_marketing = (marketing.groupby('department')['salary'].max()).reset_index(name='salary_mkt')

engineering = salaries[salaries['department']=='engineering']
salary_engineering = (engineering.groupby('department')['salary'].max()).reset_index(name='salary_eng')

result = abs(pd.DataFrame(salary_marketing['salary_mkt'] - salary_engineering['salary_eng']))

result.columns = ['salary_difference']
result

Output:

salary_different
2400
