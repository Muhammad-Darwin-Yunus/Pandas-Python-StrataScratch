>.<

Title: Last Five Records of Dataset
Link: https://platform.stratascratch.com/coding/9864-find-the-last-five-records-of-the-dataset?code_type=2
Level: Easy

Find the last five records of the dataset.

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

worker_join = worker.sort_values('joining_date',ascending=False).head(5)

worker_join['joining_date']
    
Output:

joining_date
2015-04-11 00:00:00
2015-04-10 00:00:00
2014-06-11 00:00:00
2014-06-11 00:00:00
2014-06-11 00:00:00
