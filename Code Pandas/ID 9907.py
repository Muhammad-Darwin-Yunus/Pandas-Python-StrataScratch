>.<

Title: Not Referred Employees
Link: https://platform.stratascratch.com/coding/9907-not-referred-employees?code_type=2
Level: Easy

Find employees that are not referred by the manager id 1.
Output the first name of the employee.

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

employee_filter = employee[employee['manager_id']!=1]

employee_filter['first_name']
    
Output:

first_name
Jennifer
Laila
Sarrah
Suzan
Mandy
Britney
Jack
Ben
Molly
Nicky
Monika
Mick
Shandler
Jason
Celine
Michale
Adam
John
