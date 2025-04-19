>.<

Title: Average Salaries
Link: https://platform.stratascratch.com/coding/9917-average-salaries?code_type=2
Level: Easy

Compare each employee's salary with the average salary of the corresponding department.
Output the department, first name, and salary of employees along with the average salary of that department.

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

employee['avg_salary'] = employee.groupby('department')['salary'].transform('mean')

employee[['department','first_name','salary','avg_salary']]
    
Output:

department  |  first_name  |  salary  |  avg_salary
Audit            Shandler      1100          950
Audit            Jason         1000          950
Audit            Celine        1000          950
Audit            Michale        700          950
Management        Katty        150000        175000
Management        Richerd      250000        175000
Management        George        100000        175000
Management        Allen        200000        175000
Sales            Monika        1000          1336.36
Sales            Sam            1000          1336.36
Sales            Mick           2200          1336.36
Sales            Adam          1300          1336.36
Sales            Mark          1200          1336.36
Sales            John          1500	          1336.36
Sales            Joe            1000          1336.36
Sales            Henry          2000          1336.36
Sales            Max            1300          1336.36
Sales            Nicky          1400          1336.36
Sales            Molly          1400          1336.36
Sales            Morgan          1200          1336.36
Sales            Antoney        1300          1336.36
Sales            Tom            1200          1336.36
Sales            Ben            1300          1336.36
Sales            Jack            1300          1336.36
Sales            Britney        1200          1336.36
Sales            Mandy          1300          1336.36
Sales            Suzan          1300          1336.36
Sales            Sarrah         2000          1336.36
Sales            Laila          1000          1336.36
Sales            Jennifer        1000          1336.36
