>.<

Title: Salary by Education
Link: https://platform.stratascratch.com/coding/2100-salary-by-education?code_type=2
Level: Easy

Given the education levels and salaries of a group of individuals, find what is the average salary for each level of education.

Data google_salaries:
id: bigint
first_name: text
last_name: text
department: text
education: text
salary: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
google_salaries = pd.DataFrame(google_salaries)

google_salaries_group = google_salaries.groupby('education')['salary'].mean().reset_index(name='avg_salary')
    
Output:

education  |  avg_salary
Master        57207.2
Doctorate      74045.6
Primary        26206.2
Secondary      35593.8
Bachelor       49888.4
