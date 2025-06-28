>.<

Title: Find all messages which have references to either user 2 or 3
Link: https://platform.stratascratch.com/coding/9767-find-all-messages-which-have-references-to-either-user-2-or-3?code_type=2
Level: Easy

Find all messages which have references to either user 2 or 3.

Data facebook_messages_sent:
sender: bigint
message_id: bigint
text: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
facebook = pd.DataFrame(facebook_messages_sent)

facebook_text = facebook[facebook['text'].str.contains('2|3',case=False,na=False)]

facebook_text['message_id']
    
Output:

message_id
1
3
4
