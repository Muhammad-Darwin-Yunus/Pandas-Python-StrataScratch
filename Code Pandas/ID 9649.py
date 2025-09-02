>.<

Title: Count the number of accounts used for logins in 2016
Link: https://platform.stratascratch.com/coding/9649-count-the-number-of-accounts-used-for-logins-in-2016?code_type=2
Level: Easy

How many accounts have performed a login in the year 2016?

Data product_logins:
account_id: bigint
employer_key: text
login_date: date

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

product_logins = pd.DataFrame(product_logins)

product_logins_year = product_logins[product_logins['login_date'].dt.year == 2016]

product_logins_account = product_logins_year['account_id'].nunique()

product_logins_fix = pd.DataFrame({'number_of_accounts_2016':[product_logins_account]})
    
Output:

number_of_accounts_2016
73
