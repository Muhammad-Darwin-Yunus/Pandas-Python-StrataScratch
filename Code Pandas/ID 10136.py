>.<

Title: Odd-numbered ID's Hired in February
Link: https://platform.stratascratch.com/coding/10136-find-workers-with-an-odd-number-for-worker-id?code_type=2
Level: Easy

Find employees who started in February and have odd-numbered employee IDs.

Data worker:
worker_id: int
first_name: varchar
last_name: varchar
salary: int
joining_date: datetime
department: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

hired_february = pd.DataFrame(worker)

hired_february = hired_february[(hired_february['joining_date'].dt.month == 2) & (hired_february['worker_id']% 2 != 0)]

hired_february['fullname'] = hired_february['first_name'] + ' ' + hired_february['last_name']

hired_february['fullname']

Output:

fullname
Monika Arora
Vishal Singhal
