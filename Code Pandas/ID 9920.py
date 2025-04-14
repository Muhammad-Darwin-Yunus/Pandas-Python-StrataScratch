>.<

Title: Sales Dept Salaries
Link: https://platform.stratascratch.com/coding/9920-sales-dept-salaries?code_type=2
Level: Easy

Find employees in the Sales department who achieved a target greater than 150.
Output first names of employees.
Sort records by the first name in descending order.

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

employee_filter = employee[(employee['department']=='Sales') & (employee['target']>150)]

employee_sort = employee_filter.sort_values(by='first_name',ascending=False)

employee_sort['first_name']
    
Output:

first_name
Tom
Suzan
Sarrah
Nicky
Morgan
Monika
Mick
Max
Mark
Mandy
Laila
Joe
Jennifer
Jack
Henry
Britney
Antoney
Adam
