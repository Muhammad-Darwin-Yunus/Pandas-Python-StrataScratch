>.<

Title: Account Registrations
Link: https://platform.stratascratch.com/coding/2126-account-registrations?code_type=2
Level: Easy

Find the number of account registrations according to the signup date.
Output the year months (YYYY-MM) and their corresponding number of registrations.

Data noom_signups:
signup_id: text
started_at: date
plan_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

noom_signups = pd.DataFrame(noom_signups)

noom_signups['started_at'] = pd.to_datetime(noom_signups['started_at'])

noom_signups_fix = noom_signups.groupby(noom_signups['started_at'].dt.to_period('M')).size().reset_index(name='number_of_account_registrations')

noom_signups_fix['year_months'] = noom_signups_fix['started_at']

noom_signups_fix[['year_months','number_of_account_registrations']]
    
Output:
year_months  |  number_of_account_registrations
2018-10                  1
2018-11                  4
2018-12                  1
2019-01                  3
2019-02                  3
2019-04                  1
2019-05                  2
2019-06                  1
2019-07                  1
2019-08                  1
2019-09                  4
2019-10                  1
2019-12                  1
2020-01                  1
