>.<

Title: Departments With 5 Employees
Link: https://platform.stratascratch.com/coding/9911-departments-with-5-employees?code_type=2
Level: Easy

Find departments with at more than or equal 5 employees.

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

employee_filter = employee.groupby('department').agg(total_employees=('id','count')).reset_index()

employee_count = employee_filter[employee_filter['total_employees']>=5]
    
Output:

department  |  total_employees
Sales              22
