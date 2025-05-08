>.<

Title: April Admin Employees
Link: https://platform.stratascratch.com/coding/9845-find-the-number-of-employees-working-in-the-admin-department?code_type=2
Level: Easy

Find the number of employees working in the Admin department that joined in April or later.

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

worker['joining_date'] = pd.to_datetime(worker['joining_date'])

worker_filter = worker[(worker['department']=='Admin') & (worker['joining_date'].dt.month >=4)]

worker_count = worker_filter['worker_id'].count()

worker_fix = pd.DataFrame({'total_employees':[worker_count]})
    
Output:

total_employees
4
