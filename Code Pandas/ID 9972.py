>.<

Title: Find the base pay for Police Captains
Link: https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains?code_type=2
Level: Easy

Find the base pay for Police Captains.
Output the employee name along with the corresponding base pay.

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

pay = pd.DataFrame(sf_public_salaries)

pay_filter = pay[pay['jobtitle'].str.contains('Police',case=False,na=False)]

pay_filter[['employeename','basepay']]
    
Output:

employeename        |  basepay
PATRICIA JACKSON        99722
TERESA BARRETT        188328.08
ANNA BROWN             102571.24
DOUGLAS MCEACHERN      194566.01
JOHN LOFTUS            188341.62
