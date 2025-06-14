>.<

Title: Find all actions which occurred more than once in the weblog
Link: https://platform.stratascratch.com/coding/9771-find-all-actions-which-occurred-more-than-once-in-the-weblog?code_type=2
Level: Easy

Find all actions which occurred more than once in the weblog.

Data facebook_web_log:
user_id: bigint
timestamp: timestamp
action:text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_web_log)

facebook_action = facebook['action'].value_counts()

facebook_counts = facebook_action[facebook_action>1].index

facebook_name = facebook[facebook['action'].isin(facebook_counts)][['action']].drop_duplicates()
    
Output:

action
page_load
scroll_down
scroll_up
page_exit
