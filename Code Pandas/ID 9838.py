>.<

Title: Employees Without First Names 'Vipul' or 'Satish' or Last Name Containing a 'c'
Link: https://platform.stratascratch.com/coding/9838-find-details-of-workers-excluding-those-with-the-first-name-vipul-or-satish?code_type=2
Level: Easy

Find information on employees who do not have the first names 'Vipul' or 'Satish' or a last name that contains a 'c'.

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

worker_filter = worker[(worker['first_name']!= 'Vipul') & (worker['first_name']!= 'Satish') * (worker['last_name']).str.contains('c',case=False,na=False)]

worker_filter['fullname'] = worker_filter['first_name'] + ' ' + worker_filter['last_name']

worker_filter['fullname']
    
Output:

fullname
Geetika Chauhan
Moe Acharya
