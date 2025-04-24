>.<

Title: Employees With Bonuses
Link: https://platform.stratascratch.com/coding/9903-employees-with-bonuses?code_type=2
Level: Easy

Find employees whose bonus is less than $150.
Output the first name along with the corresponding bonus.

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

employee_filter = employee[employee['bonus']<150]

employee_filter[['first_name','bonus']]
    
Output:

first_name  |  bonus
Britney          100
Jack            100
Ben              100
Nicky            100
Monika          100
Adam            100
John            100
