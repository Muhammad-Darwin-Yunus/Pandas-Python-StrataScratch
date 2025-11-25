>.<

Title: User Growth Rate
Link: https://platform.stratascratch.com/coding/2052-user-growth-rate?code_type=2
Level: Easy

Find the growth rate of active users for Dec 2020 to Jan 2021 for each account.
The growth rate is defined as the number of users in January 2021 divided by the number of users in Dec 2020.
Output the account_id and growth rate.

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

sf_events['record_date'] = pd.to_datetime(sf_events['record_date'])

monthly_active_user = (sf_events[(sf_events['record_date'] >= '2020-12-01') &(sf_events['record_date'] <= '2021-01-31')].assign(month = sf_events['record_date'].dt.to_period('M').dt.to_timestamp()).groupby(['account_id', 'month'])['user_id'].nunique().reset_index(name='user_active'))

dec_users = monthly_active_user[monthly_active_user['month'] == pd.Timestamp('2020-12-01')][['account_id', 'user_active']].rename(columns={'user_active': 'user_active_dec'})

jan_users = monthly_active_user[monthly_active_user['month'] == pd.Timestamp('2021-01-01')][['account_id', 'user_active']].rename(columns={'user_active': 'user_active_jan'})

result = (pd.merge(jan_users, dec_users, on='account_id').assign(growth_rate = lambda df: (df['user_active_jan'] / df['user_active_dec']).round(2))[['account_id', 'growth_rate']])
    
Output:

account_id  |  growth_rate
A1                1
A2                2
A3                0.5
