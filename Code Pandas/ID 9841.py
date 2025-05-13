>.<

Title: First Name That Ends With The Letter 'a'
Link: https://platform.stratascratch.com/coding/9841-find-all-workers-whose-first-name-ends-with-the-letter-a?code_type=2
Level: Easy

Find all workers whose first name ends with the letter 'a'.

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

worker_name = worker[worker['first_name'].str.endswith('a')]['first_name']
    
Output:

first_name
Monika
Niharika
Geetika
