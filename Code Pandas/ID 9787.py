>.<

Title: User Scroll Up Events
Link: https://platform.stratascratch.com/coding/9787-user-scroll-up-events?code_type=2
Level: Easy

Find all users that have performed at least one scroll_up event.

Data facebook_web_log:
user_id: bigint
timestamp: timestamp
action: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_web_log)

facebook_action = facebook[facebook['action']=='scroll_up']['user_id']
    
Output:

user_id
0
2
1
