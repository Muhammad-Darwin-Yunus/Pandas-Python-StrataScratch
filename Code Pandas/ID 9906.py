>.<

Title: Number of Employees Per Department
Link: https://platform.stratascratch.com/coding/9906-number-of-employees-per-department?code_type=2
Level: Easy

Find the number of employees in each department.
Output the department name along with the corresponding number of employees.
Sort records based on the number of employees in descending order.

Data employee:
address: text
age: bigint
bonus: bigint
city: text
department: text
email: text
employee_title: text
first_name: text
id: bigint
last_name: text
manager_id: bigint
salary: bigint
sex: text
target: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

employee = pd.DataFrame(employee)

employee_filter = employee.groupby('department').agg(employees=('id','count')).reset_index()

employee_sort = employee_filter.sort_values(by='employees',ascending=False)
    
Output:

department  |  employees
Sales            22
Management        4
Audit             4
