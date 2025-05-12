>.<

Title: First Names With Six Letters Ending in 'h'
Link: https://platform.stratascratch.com/coding/9842-find-all-workers-whose-first-name-contains-6-letters-and-also-ends-with-the-letter-h?code_type=2
Level: Easy

Find all workers whose first name contains 6 letters and also ends with the letter 'h'.
Display all information about the workers in output.

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

worker_filter = worker[worker['first_name'].str.match(r'.{5}h$')]

worker_filter['first_name']
    
Output:

first_name
Amitah
Satish
