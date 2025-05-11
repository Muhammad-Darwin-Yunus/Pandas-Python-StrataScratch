>.<

Title: Employees With Salary Between Given Range
Link: https://platform.stratascratch.com/coding/9843-find-all-workers-whose-salary-lies-between-100000-and-500000?code_type=2
Level: Easy

Find all workers whose salary lies between 100,000 and 500,000 inclusive.

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

worker_salary = worker[(worker['salary']>=100000) & (worker['salary']<=500000)]

worker_salary['fullname'] = worker_salary['first_name'] + ' ' + worker_salary['last_name']

worker_salary['fullname']
    
Output:

fullname
Monika Arora
Vishal Singhal
Amitah Singh
Vivek Bhati
Vipul Diwan
