>.<

Title: Three Lowest Distinct Salaries
Link: https://platform.stratascratch.com/coding/9867-find-the-three-lowest-salaries?code_type=2
Level: Easy

You have been asked to find the three lowest distinct salaries.
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

worker_sort = worker['salary'].drop_duplicates().sort_values().head(3)
    
Output:

salary
65000
75000
80000
