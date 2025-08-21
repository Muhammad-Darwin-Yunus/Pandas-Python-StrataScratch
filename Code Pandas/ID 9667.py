>.<

Title: Count users that speak English, German, French or Spanish
Link: https://platform.stratascratch.com/coding/9667-count-users-that-speak-english-german-french-or-spanish?code_type=2
Level: Easy

How many users speak English, German, French or Spanish?
Note: Users who speak more than one language are counted only once.

Data playbook_users:
activated_at: datetime
company_id: bigint
created_at: timestamp
language: text
state: text
user_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

playbook_users = pd.DataFrame(playbook_users)

playbook_users_language = playbook_users.groupby('language')['user_id'].nunique().reset_index(name='total_users')

playbook_users_filter = playbook_users_language[playbook_users_language['language'].isin(['english','german','french','spanish'])]

playbook_users_filter[['total_users','language']]
    
Output:

total_users	language
109	english
12	french
11	german
29	spanish
