>.<

Title: Workers by Department Since April
Link: https://platform.stratascratch.com/coding/9847-find-the-number-of-workers-by-department?code_type=2
Level: Easy

Find the number of workers by department who joined on or after April 1, 2014.
Output the department name along with the corresponding number of workers.
Sort the results based on the number of workers in descending order.

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

worker_date = worker[worker['joining_date']>='2014-04-01']

worker_filter = worker_date.groupby('department').agg(joined_on_or_after=('joining_date','count')).reset_index()

worker_sort = worker_filter.sort_values('joined_on_or_after',ascending=False)
    
Output:

department  |  joined_on_or_after
Admin                4
Account              1
HR                    1
