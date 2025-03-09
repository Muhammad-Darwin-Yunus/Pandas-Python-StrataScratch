>.<

Title: Benefits Of Employees Called Patrick
Link: https://platform.stratascratch.com/coding/9974-benefits-of-employees-called-patric?code_type=2
Level: Easy

Find benefits that people with the name 'Patrick' have.
Output the full employee name along with the corresponding benefits.

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

employee = pd.DataFrame(sf_public_salaries)

benefit_employee = employee[employee['employeename'].str.contains('Patrick',case=False,na=False)]

benefit_employee[['employeename','benefits']]
    
Output:

employeename          |  benefits
Patrick F Mcpartland          5.01
Patrick Crane                34143.72
Patrick Martinez              33194.97
Patrick T Truong              31360.09
Patrick Kennedy                40093.21
Emilia C Patrick                373.71
Patrick S Renshaw              30691.14
Emilia C Patrick              21067.97
Patrick T Truong            34506.78
