>.<

Title: First Name's Containing the Letter 'a'
Link: https://platform.stratascratch.com/coding/9840-find-all-workers-whose-first-name-contains-the-letter-a?code_type=2
Level: Easy

Find all workers whose first name contains the letter 'a'. Output all columns for such workers.

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

worker_name = worker[worker['first_name'].str.contains('a')]['first_name']
    
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
