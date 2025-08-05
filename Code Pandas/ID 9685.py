>.<

Title: Companies With Chinese Speakers
Link: https://platform.stratascratch.com/coding/9685-companies-with-chinese-speakers?code_type=2
Level: Easy

Find companies that have at least 2 Chinese speaking users.

Data playbook_users:
user_id: bigint
created_at: timestamp
company_id: bigint
language: text
activated_at: datetime
state: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

playbook_users = pd.DataFrame(playbook_users)

playbook_users_language = playbook_users[playbook_users['language']=='chinese']

playbook_users_company = playbook_users_language.groupby('company_id')['user_id'].nunique()

playbook_users_count = playbook_users_company[playbook_users_company >= 2].index

playbook_users_final = pd.DataFrame({'company_id':playbook_users_count})
    
Output:

company_id
4
