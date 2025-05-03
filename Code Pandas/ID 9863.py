>.<

Title: First Record Without LIMIT or ORDER BY
Link: https://platform.stratascratch.com/coding/9863-find-the-first-record-of-the-dataset-without-using-limit-or-order-by?code_type=2
Level: Easy

Find the first record of the dataset without using LIMIT or ORDER BY.
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

worker_min = worker['joining_date'].min()

worker_fix = worker[worker['joining_date'] == worker_min][['worker_id','joining_date']]
    
Output:

worker_id  |  joining_date
7             2014-01-20 00:00:00
