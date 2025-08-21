>.<

Title: Count the number of speakers per each language
Link: https://platform.stratascratch.com/coding/9669-count-the-number-of-speakers-per-each-language?code_type=2
Level: Easy

Count the number of speakers for each language.
Sort the result based on the number of speakers in descending order.

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

playbook_users_language = playbook_users.groupby('language')['user_id'].count().reset_index(name='number_of_speakers')

playbook_users_sort = playbook_users_language.sort_values('number_of_speakers',ascending=False)

playbook_users_sort[['number_of_speakers','language']]
    
Output:

number_of_speakers  |  language
109                    english
29                      spanish
14                      japanese
12                      french
11                      german
11                      russian
9                      arabic
7                      chinese
6                      italian
6                      indian
5                      portugese
