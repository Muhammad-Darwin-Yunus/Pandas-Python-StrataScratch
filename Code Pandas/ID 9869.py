>.<

Title: Total Salary by Department
Link: https://platform.stratascratch.com/coding/9869-find-the-total-salary-of-each-department?code_type=2
Level: Easy

You have been asked to calculate the total salary for each department.
Provide the salary as well as the corresponding department.

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

worker_filter = worker.groupby('department').agg(total_salary=('salary','sum')).reset_index()
    
Output:

department  |  total_salary
HR                550000
Admin              1260000
Account            350000
