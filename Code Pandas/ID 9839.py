>.<

Title: Admin Department Workers
Link: https://platform.stratascratch.com/coding/9839-find-all-workers-that-work-in-the-admin-department?code_type=2
Level: Easy

Find all workers and their details that work in the Admin department.

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

worker['department'] = worker['department'].str.strip().str.lower()

worker_admin = worker[worker['department'] == 'admin']
    
Output:

worker_id  |  first_name  |  last_name  |  salary  |  joining_date        |  department
2	              Niharika        Verma      80000      2014-06-11 00:00:00	      Admin 
4	              Amitah          Singh      500000     2014-02-20 00:00:00	      Admin 
5	              Vivek           Bhati      500000      2014-06-11 00:00:00	    Admin 
8              Geetika         Chauhan      90000      2014-04-11 00:00:00      Admin 
9	              Agepi          Argon        80000      2015-04-10 00:00:00      admin
