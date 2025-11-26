>.<

Title: Monthly Active Users
Link: https://platform.stratascratch.com/coding/2051-monthly-active-users?code_type=2
Level: Easy

Find the monthly active users for January 2021 for each account.
Your output should have account_id and the monthly count for that account.

Data sf_events:
account_id: text
record_date: date
user_id: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
sf_events = pd.DataFrame(sf_events)

sf_events_record_date = sf_events[(sf_events['record_date'].dt.year ==2021) & (sf_events['record_date'].dt.month == 1)]

sf_events_group = sf_events_record_date.groupby('account_id')['user_id'].count().reset_index()
    
Output:

account_id  |  active_users
A1                  4
A2                  4
A3                  1
