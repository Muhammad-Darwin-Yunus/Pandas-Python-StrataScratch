>.<

Title: METROPOLITAN TRANSIT AUTHORITY' Employees
Link: https://platform.stratascratch.com/coding/9975-metropolitan-transit-authority-employees?code_type=2
Level: Easy

Find all employees with a job title that contains
'METROPOLITAN TRANSIT AUTHORITY' and output the employee's name along with the corresponding total pay with benefits.

Data sf_public_salaries:
agency: text
basepay: double
benefits: double
employeename: text
id: bigint
jobtitle: text
notes: datetime
otherpay: double
overtimepay: double
status: text
totalpay: double
totalpaybenefits: double
year: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

salary = pd.DataFrame(sf_public_salaries)

salary_group = salary[salary['jobtitle'].str.contains('METROPOLITAN TRANSIT AUTHORITY',case=False,na=False)]

salary_group[['employeename','totalpaybenefits']]
    
Output:

employeename    |  totalpaybenefits
EDWARD REISKIN      230827.12
NATHANIEL FORD      567595.43
