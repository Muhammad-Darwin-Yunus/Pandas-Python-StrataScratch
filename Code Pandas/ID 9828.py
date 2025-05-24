>.<

Title: First Three Characters of First Name
Link: https://platform.stratascratch.com/coding/9828-print-the-first-three-characters-of-the-first-name?code_type=2
Level: Easy

Print the first three characters of the first name.

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

worker['first_name'] = worker['first_name'].str[:3]
    
Output:

first_name
Mon
Nih
Vis
Ami
Viv
Vip
Sat
Gee
Age
Moe
Nay
Jai
