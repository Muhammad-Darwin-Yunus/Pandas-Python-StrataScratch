>.<

Title: Employees Who Joined in February 2014
Link: https://platform.stratascratch.com/coding/9844-find-all-workers-who-joined-on-february-2014?code_type=2
Level: Easy

Find all workers who joined on February 2014.

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

worker_date = worker[(worker['joining_date'].dt.month == 2) & (worker['joining_date'].dt.year == 2014)]

worker_date['fullname'] = worker_date['first_name'] + ' ' + worker_date['last_name']

worker_date['fullname']
    
Output:

fullname
Monika Arora
Vishal Singhal
Amitah Singh
