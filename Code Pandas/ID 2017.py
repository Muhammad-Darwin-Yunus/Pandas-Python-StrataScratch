>.<

Title: Paid Users In April 2020
Link: https://platform.stratascratch.com/coding/2017-paid-users-in-april-2020?code_type=2
Level: Easy

How many paid users had any calls in Apr 2020?

Data rc_calls:
call_date: datetime
call_id: bigint
user_id: bigint

Data rc_users:
company_id: bigint
status: text
user_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
rc_merge = rc_calls.merge(rc_users,how='left',on='user_id')

rc_filter = rc_merge[(rc_merge['call_date'].dt.month==4) & (rc_merge['call_date'].dt.year==2020) & (rc_merge['status']=='paid')]['user_id'].count()

rc_fix = pd.DataFrame({'paid_users':[rc_filter]})
    
Output:

paid_users
7
