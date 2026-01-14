>.<

Title: Inactive Free Users
Link: https://platform.stratascratch.com/coding/2018-inactive-free-users?code_type=2
Level: Easy

Return a list of users with status free who didn’t make any calls in Apr 2020.

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
rc_merge = rc_calls.merge(rc_users,how='left',left_on='user_id',right_on='user_id')

rc_filter = rc_merge[(rc_merge['status']=='free') & (rc_merge['call_date'].dt.month==4) & (rc_merge['call_date'].dt.year==2020)]['user_id']
    
Output:

user_id
1218
1950
1339
1859
1884
1859
1859
1857
