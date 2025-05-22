>.<

Title: First Name with Right Whitespace Removed
Link: https://platform.stratascratch.com/coding/9830-print-the-first-name-after-removing-white-spaces-from-the-right-side?code_type=2
Level: Easy

Print the first name after removing white spaces from the right side.

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

worker = pd.DataFrame(worker_ws)

worker['first_name'] = worker['first_name'].str.rstrip()
    
Output:

first_name
 Monika
 Niharika
 Vishal
 Amitah
 Vivek
 Vipul
 Satish
 Geetika
 Agepi
