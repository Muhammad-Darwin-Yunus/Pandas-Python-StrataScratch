>.<

Title: MacBookPro User Event Count
Link: https://platform.stratascratch.com/coding/9653-count-the-number-of-user-events-performed-by-macbookpro-users?code_type=2
Level: Easy

Count the number of user events performed by MacBookPro users.
Output the result along with the event name.
Sort the result based on the event count in the descending order.

Data playbook_events:
user_id: bigint
occurred_at: timestamp
event_type: text
event_name: text
location: text
device: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

playbook_events = pd.DataFrame(playbook_events)

playbook_events_event = playbook_events.groupby('event_name')['user_id'].count().reset_index(name='event_count')

playbook_events_sort = playbook_events_event.sort_values('event_count',ascending=False)

playbook_events_sort[['event_name','event_count']]
    
Output:

event_name	event_count
home_page	25
login	18
view_inbox	16
like_message	12
search_autocomplete	9
send_message	8
search_run	3
enter_email	2
create_user	2
complete_signup	1
enter_info	1
search_click_result_3	1
search_click_result_8	1
search_click_result_9	1
