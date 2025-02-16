>.<

Title: Even-numbered IDs Hired in June
Link: https://platform.stratascratch.com/coding/10137-find-workers-with-an-even-number-for-worker-id?code_type=2
Level: Easy

Find employees who started in June and have even-numbered employee IDs.

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

hired_june = pd.DataFrame(worker)

hired_june = hired_june[(hired_june['joining_date'].dt.month==6) & (hired_june['worker_id']% 2 == 0)]

hired_june['fullname'] = hired_june['first_name'] + ' ' + hired_june['last_name']

hired_june['fullname']

Output:

fullname
Niharika Verma
Vipul Diwan
