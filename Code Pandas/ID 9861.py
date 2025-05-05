>.<

Title: Total Employees in Each Department
Link: https://platform.stratascratch.com/coding/9861-find-the-number-of-employees-in-each-department?code_type=2
Level: Easy

Find the number of employees in each department.
Output the department name along with the corresponding number of employees.

Data worker:
department: text
first_name: text
joining_date: datetime
last_name: text
salary: bigint
worker_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

worker = pd.DataFrame(worker)

worker_filter = worker.groupby('department').agg(total_employees=('worker_id','sum')).reset_index()

worker_filter[['department','total_employees']]
    
Output:

department  |  total_employees
HR                  26
Admin              28
Account            24
