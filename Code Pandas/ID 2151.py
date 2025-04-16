>.<

Title: Number of Hires During Specific Time Period
Link: https://platform.stratascratch.com/coding/2151-number-of-hires-during-specific-time-period?code_type=2
Level: Easy

You have been asked to find the number of employees hired between the months of January and July in the year 2022 inclusive.
Your output should contain the number of employees hired in this given time frame.

Data employees:
department: text
first_name: text
id: bigint
joining_date: date
last_name: text
salary: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

employees = pd.DataFrame(employees)

employees_date = employees[(employees['joining_date']>'2022-01-01') & (employees['joining_date']<'2022-07-31')]

employees_count = employees_date.shape[0]

result = pd.DataFrame({'number_of_employees':[employees_count]})
    
Output:

number_of_employees
3
