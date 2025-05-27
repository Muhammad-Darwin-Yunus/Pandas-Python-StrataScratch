>.<

Title: Find all companies with more than 10 employees
Link: https://platform.stratascratch.com/coding/9807-find-all-companies-with-more-than-10-employees?code_type=2
Level: Easy

Find all companies with more than 10 employees. Output all columns.

Data google_adwords_earnings:
business_type: text
n_employees: bigint
year: bigint
adwords_earnings: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

google = pd.DataFrame(google_adwords_earnings)

google_employee = google[google['n_employees']>10]
    
Output:

business_type  |  n_employees  |  year  |  adwords_earnings
media                10000        2018        123456789
handyman              5000        2018        1001001
handyman              1500        2018        5040032
transport              3200        2018        7865490
