>.<

Title: Workers With The Highest Salaries
Link: https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2
Level: Easy

Find the job titles of the employees with the highest salary.
If multiple employees have the same highest salary, include the job titles for all such employees.

Data worker:
department: text
first_name: text
joining_date: date
last_name: text
salary: bigint
worker_id: bigint

Data title:
affected_from: date
worker_ref_id: bigint
worker_title: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

worker_salaries = pd.merge(worker,title,how='inner',left_on='worker_id',right_on='worker_ref_id')

max_worker_salaries = worker_salaries['salary'].max()

best_worker_salaries = worker_salaries[worker_salaries['salary']== max_worker_salaries]

best_worker_salaries[['worker_title']].rename(columns={'worker_title':'best_paid_title'})
    
Output:

best_paid_title
Asst. Manager
Manager
