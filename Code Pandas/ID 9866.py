>.<

Title: Highest Salary & Full Name
Link: https://platform.stratascratch.com/coding/9866-highest-salary-and-full-name?code_type=2
Level: Easy

Your output should include the full name of the employee(s) with the highest salary in one column and the corresponding salary in the other.

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

worker['fullname'] = worker['first_name'] + worker['last_name']

worker_salary = worker['salary'].max()

result_worker = pd.DataFrame({
    'fullname':[worker.loc[worker['salary'] == worker_salary,'fullname'].values[0]],
    'highest_salary':[worker_salary]
});
    
Output:

fullname    |  highest_salary
MonikaArora        500000
