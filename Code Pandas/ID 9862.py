>.<

Title: Last Record Without LIMIT or ORDER BY
Link: https://platform.stratascratch.com/coding/9862-find-the-last-record-of-the-dataset-without-using-limit-or-order-by?code_type=2
Level: Easy

Find the last record of the dataset without using LIMIT or ORDER BY.
Note: The earliest records correspond to the earliest employee ID's.

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

worker_max = worker['joining_date'].max()

worker_fix = worker[worker['joining_date']==worker_max][['worker_id','joining_date']]
    
Output:

worker_id  |  joining_date
10            2015-04-11 00:00:00
