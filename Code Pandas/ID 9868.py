>.<

Title: Five Highest Distinct Salaries
Link: https://platform.stratascratch.com/coding/9868-find-the-five-highest-salaries?code_type=2
Level: Easy

You have been asked to find the five highest distinct salaries.
For example, if two people earn the same amount of money, they are counted as one.

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

worker_filter = worker.groupby('first_name').agg(highest_salaries=('salary','first')).drop_duplicates()

worker_sort = worker_filter.sort_values(by='highest_salaries',ascending=False).head(5)
    
Output:

highest_salaries
500000
300000
200000
100000
90000
