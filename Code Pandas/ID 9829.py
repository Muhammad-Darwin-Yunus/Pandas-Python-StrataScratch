>.<

Title: Positions Of Letter 'a'
Link: https://platform.stratascratch.com/coding/9829-positions-of-letter-a?code_type=2
Level: Easy

Find the position of the lower case letter 'a' in the first name of the worker 'Amitah'.

Data worker:
worker_id: bigint
first_name: text
last_name: text
salary: bigint
joining_date: datetime
department: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

worker = pd.DataFrame(worker)

worker_Sort = worker[worker['first_name'].str.contains('a',case=False,na=False)][['first_name']]
    
Output:

first_name
Monika
Niharika
Vishal
Amitah
Satish
Geetika
Agepi
Nayah
Jai
Agepi
