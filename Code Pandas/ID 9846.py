>.<

Title: Full Names of Employees With Salaries in a Specific Range
Link: https://platform.stratascratch.com/coding/9846-find-the-full-name-of-workers-whose-salaries-50000-and-100000?code_type=2
Level: Easy

Find the full name of workers whose salaries range from 50,000 to 100,000 inclusive.
Output the worker's first name and last name in one column along with their salaries.

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

worker_salary = worker[(worker['salary']>50000) & worker['salary']<100000]

worker_salary['fullname'] = worker_salary['first_name'] + worker_salary['last_name']

worker_salary[['fullname','salary']]
    
Output:

fullname      |  salary
MonikaArora      100000
NiharikaVerma    80000
SatishKumar      75000
GeetikaChauhan    90000
AgepiArgon        90000
MoeAcharya        65000
NayahLaghari      75000
JaiPatel          85000
