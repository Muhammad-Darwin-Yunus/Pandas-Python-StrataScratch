>.<

Title: Find the top 3 jobs with the highest overtime pay rate
Link: https://platform.stratascratch.com/coding/9988-find-the-top-3-jobs-with-the-highest-overtime-pay-rate?code_type=2
Level: Easy

Get the job titles of the 3 employees who received the most overtime pay
Output the job title of selected records.

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

salary_group = salary.groupby('jobtitle')['overtimepay'].sum().reset_index(name='most_overtimepay')

salary_sort = salary_group.sort_values(by='most_overtimepay',ascending=False).head(3)
    
Output:

jobtitle                          |  most_overtimepay
CAPTAIN III (POLICE DEPARTMENT)          95628.72
Deputy Sheriff                            76031.16
EMT/Paramedic/Firefighter                74246.42
